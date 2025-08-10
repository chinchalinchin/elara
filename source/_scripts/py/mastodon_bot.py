# lambda_function.py

# NOTE #1: there is a bug in mastodon.notifications(id=...). It *DOES NOT* return the 
#       expected dictionary when passed a single ID. For some reason, the Mastodon 
#       client library returns a list of strings when called with a Single ID,
#       making it unusable. The REPL shell output below demonstrates this bug, 
#       
#       >>> import mastodon
#       >>> import os
#       >>> mast = mastodon.Mastodon(
#           client_id=os.getenv('MASTODON_CLIENT_ID'),
#           client_secret=os.getenv('MASTODON_CLIENT_SECRET'),
#           access_token=os.getenv('MASTODON_ACCESS_TOKEN'),
#           api_base_url=os.getenv('MASTODON_API_BASE_URL'))
#       >>> notes = mast.notifications()
#       >>> print(notes)
#           [Notification({'id': '55', 'type': 'admin.sign_up', ... }), ... ]
#       >>> mast.notifications(id=55)
#           ['id', 'type', 'created_at', 'group_key', 'account']
#       >>> mast.notifications(id='55')
#           ['id', 'type', 'created_at', 'group_key', 'account']
#
#   Therefore, the following lines are a hacky workaround until the client library is updated.
#
#   Here is the GitHub issue I have opened about this: https://github.com/halcy/Mastodon.py/issues/416
# 
#  IMPORTANT: DO NOT ATTEMPT TO FIX THIS. I WILL FIX IT WHEN MASTODON.PY IS UPDATED.

import json
import os
import pprint
from datetime import datetime
from google import genai
from jinja2 import Environment, FileSystemLoader
from mastodon import Mastodon
from pydantic import BaseModel, Field, TypeAdapter
from typing import Literal, Optional, Union, Any
import boto3
from mypy_boto3_dynamodb.service_resource import Table


MASTODON_SECRET_PREFIX                          = "prod/agn/mastodon-bot" 
GEMINI_SECRET_NAME                              = "cumberland-cloud/gemini"
GEMINI_MODEL                                    = "gemini-2.5-flash"
DYNAMODB_TABLE_NAME                             = "cc-prd-agn-mastodon-bot"


APP                                             = {
    "global_timeline_limit"                     : 10,
    "local_timeline_limit"                      : 5,
    "hashtag_limit"                             : 15,
    "toots_limit"                               : 10
}

# --- Pydantic Models ---


class StatusPost(BaseModel):
    """Model for posting a new status or a reply."""
    function                                    : Literal['status_post']
    status                                      : str = Field(
        max_length                              = 500, 
        description                             = "The content of the status update that will be posted."
    )
    in_reply_to_id                              : Optional[str] = Field(None, 
        description                             = "The ID of the status update being replied to."
    )
    scheduled_at                                : Optional[datetime] = Field(None, 
        description                             = "Schedule the post for a future date and time."
    )
    memory                                      : Optional[str] = Field(None, 
        description                             = "Data to persist across executions.",
        max_length                              = 1000
    )


class StatusReblog(BaseModel):
    """Model for reblogging a status."""
    function                                    : Literal['status_reblog']
    id                                          : str = Field(
        description                             = "The ID of the status to reblog."
    )
    memory                                      : Optional[str] = Field(None, 
        description                             = "Data to persist across executions.",
        max_length                              = 1000
    )


class StatusFavourite(BaseModel):
    """Model for favouriting a status."""
    function                                    : Literal['status_favourite']
    id                                          : str = Field(
        description                             = "The ID of the status to favourite."
    )
    memory                                      : Optional[str] = Field(None, 
        description                             = "Data to persist across executions."
    )


BotResponse = Union[StatusPost, StatusReblog, StatusFavourite]


# --- Helper Functions ---


def log(*msg) -> Any:
    """Print logs to the AWS CloudWatch log stream"""

    for m in msg:
        if isinstance(m, dict):
            pprint.pprint(m)
        else:
            print(m)
    return 
    

def get_json_secret(secret_name: str, suffix: str = None) -> dict:
    """Retrieves a secret stored as a JSON string from AWS Secrets Manager."""

    if suffix is not None:
        secret_name                             = f"{secret_name}/{suffix}"

    session                                     = boto3.session.Session()
    client                                      = session.client(service_name='secretsmanager')
    
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    return json.loads(get_secret_value_response['SecretString'])


def get_plaintext_secret(secret_name: str) -> str:
    """Retrieves a secret stored as plain text from AWS Secrets Manager."""

    session                                     = boto3.session.Session()
    client                                      = session.client(
        service_name                            = 'secretsmanager'
    )
    get_secret_value_response                   = client.get_secret_value(SecretId=secret_name)

    return get_secret_value_response['SecretString']


def get_table() -> Table:
    """Returns the DynamoDB table used for persistence"""

    dynamodb                                    = boto3.resource('dynamodb')

    return dynamodb.Table(DYNAMODB_TABLE_NAME)


def get_mastodon(persona = None) -> Mastodon:
    """Returns the Mastodon client used for the persona"""

    mastodon_secrets                            = get_json_secret(
        secret_name                             = MASTODON_SECRET_PREFIX,
        suffix                                  = persona
    )    

    if not mastodon_secrets:
        if not persona:
            raise ValueError(f"Secret '{MASTODON_SECRET_PREFIX}' is empty or not found.")
        raise ValueError(f"Secret '{MASTODON_SECRET_PREFIX}/{persona}' is empty or not found.")
    
    return Mastodon(
        client_id                               = mastodon_secrets['client_id'],
        client_secret                           = mastodon_secrets['client_secret'],
        access_token                            = mastodon_secrets['access_token'],
        api_base_url                            = mastodon_secrets['api_base_url']
    )


def render_context(context_vars: dict) -> str:
    """Renders the Jinja2 template."""
    
    template_dir                                = os.path.join(os.path.dirname(__file__), 'context')
    env                                         = Environment(
        loader                                  = FileSystemLoader(template_dir)
    )
    template                                    = env.get_template('template.rst')
    context                                     = template.render(context_vars)
    
    log("---- Generated Context ----", context)

    return context


def generate_toot(context: str) -> str:
    """Generates content using the Gemini API."""

    gemini_api_key                              = get_plaintext_secret(GEMINI_SECRET_NAME)

    if not gemini_api_key:
        raise ValueError(f"Secret '{GEMINI_SECRET_NAME}' is empty or not found.")

    try:
        client                                  = genai.Client(
            api_key                             = gemini_api_key,
            http_options                        = genai.types.HttpOptions(
                api_version                     = 'v1alpha'
            )
        )
        config                                  = {
            "safety_settings"                   : [
                genai.types.SafetySetting(
                    category                    = 'HARM_CATEGORY_HATE_SPEECH',
                    threshold                   = 'BLOCK_NONE',
                ),
                genai.types.SafetySetting(
                    category                    = 'HARM_CATEGORY_HARASSMENT',
                    threshold                   = 'BLOCK_NONE',
                ),
                genai.types.SafetySetting(
                    category                    = 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
                    threshold                   = 'BLOCK_NONE',
                ),
                genai.types.SafetySetting(
                    category                    = 'HARM_CATEGORY_DANGEROUS_CONTENT',
                    threshold                   = 'BLOCK_NONE',
                ),
                genai.types.SafetySetting(
                    category                    = 'HARM_CATEGORY_CIVIC_INTEGRITY',
                    threshold                   = 'BLOCK_NONE',
                ),
            ],
            "response_mime_type"                : "application/json",
            "response_schema"                   : BotResponse
        }

        response                                = client.models.generate_content(
            model                               = GEMINI_MODEL,
            contents                            = context,
            config                              = genai.types.GenerateContentConfig(**config)
        )

        log("---- GEMINI RESPONSE ----", response)

        if hasattr(response, 'parsed') and response.parsed:
            return response.parsed
        
        return TypeAdapter(BotResponse).validate_json(response.text)

    except Exception as e:
        log("---- GEMINI API ERROR ----", e)
        raise e
    

def process(context_vars: dict, response: BotResponse, mastodon: Mastodon, state: Table):
    """Process LLM agent's response and post to Mastodon"""

    if response.memory:
        state.update_item(
                Key                             = {
                    'persona'                   : context_vars["persona"]
                },
                UpdateExpression                = "SET memory = :mem",
                ExpressionAttributeValues       = {
                    ':mem'                      : response.memory
                }
            )
        
    if response.function == "status_post":
        mastodon.status_post(
            status                              = response.status,
            in_reply_to_id                      = response.in_reply_to_id,
            scheduled_at                        = response.scheduled_at,
            visibility                          = 'public'
        )

        if response.in_reply_to_id:
            state.update_item(
                Key                             = {
                    'persona'                   : context_vars["persona"]
                },
                UpdateExpression                = "SET last_processed_mention_id = :id",
                ExpressionAttributeValues       = {
                    ':id'                       : response.in_reply_to_id
                }
            )
        return {
            'statusCode'                        : 200,
            'body'                              : json.dumps("status_post called successfully!")
        }
    
    if response.function == "status_reblog":
        mastodon.status_reblog(
            id                                  = response.id,
            visibility                          = "public"
        )
        return {
            'statusCode'                        : 200,
            'body'                              : json.dumps("status_reblog called successfully!")
        }
    
    if response.function == "status_favourite":
        mastodon.status_favourite(
            id                                  = response.id
        )
        return {
            'status'                            : 200,
            'body'                              : json.dumps("status_favourite called successfully!")
        }
    
    return {
        "statusCode"                            : 204,
        "body"                                  : "Nothing happened!"
    }


# --- Main Handler ---


def lambda_handler(event, context):
    """
    Main Lambda function handler.
    """

    mastodon                                    = get_mastodon(event.get('persona'))
    state                                       = get_table()
    current_state                               = state.get_item(
        Key                                     = {
            'persona'                           : event.get('persona')
        }
    ).get('Item', {})

    global_timeline                             = mastodon.timeline_public(limit=APP['global_timeline_limit'])
    local_timeline                              = mastodon.timeline_local(limit=APP["local_timeline_limit"])
    toots                                       = mastodon.account_statuses(mastodon.me()['id'], limit=APP["toots_limit"])
    hashtags                                    = [tag['name'] for tag in mastodon.trending_tags(limit=APP["hashtag_limit"])]
    
    for toot in local_timeline:
        toot['context']                         = mastodon.status_context(toot['id'])

    for toot in toots:
        toot['context']                         = mastodon.status_context(toot['id'])

    last_processed_id                           = current_state.get('last_processed_mention_id')

    if last_processed_id:
        # START: HACK 
        #   SEE NOTE #1. 
        hacked_notifications                    = mastodon.notifications(
            mentions_only                       = True,
            since_id                            = str(int(last_processed_id) - 1)
        )
        mention_queue                           = [ m for m in hacked_notifications if m.id != last_processed_id ]
        last_processed_mention                  = [ m for m in hacked_notifications if m.id == last_processed_id ]

        if last_processed_mention:
            last_processed_mention              = last_processed_mention[0]

        # END: HACK 

    else: 
        mention_queue                           = mastodon.notifications(
            mentions_only                       = True, 
            limit                               = 10
        )
        last_processed_mention                  = None

    context_vars                                = {
        "id"                                    : mastodon.me()['id'],
        "current_date"                          : datetime.now().strftime("%Y-%m-%d"),
        "persona"                               : event.get('persona'),
        "toots"                                 : toots,
        "hashtags"                              : hashtags,
        "local_timeline"                        : local_timeline,
        "global_timeline"                       : global_timeline,
        "mention_queue"                         : mention_queue,
        "last_processed_mention"                : last_processed_mention,
        "memory"                                : current_state.get('memory')
    }

    context                                     = render_context(context_vars)
    response                                    = generate_toot(context)
    
    return process(context_vars, response, mastodon, state)