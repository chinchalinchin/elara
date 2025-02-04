.. _{{ current_persona }}-context:

#############
Investigation 
#############

.. _preamble:

Preamble
########

.. danger::

    As you enter the newsroom, you see your editor, {{ current_prompter | capitalize }}, angrily approaching.

{{ current_persona }}, where have you been?! The entire newsroom has been running around likes chickens with their heads cutoff, waiting for you! The front page can't be put to ink until we've got the copy from your feature! What are you doing still standing here!? Hurry up! Get to your office and start drafting it! We only a few hours to meet the deadline for the new edition!

Wait! {{ current_persona}}! Before you go, make sure to stop by all of the desks in the newsroom. Everyone has important information and context for you to consider before you draft your feature story. 

.. _newsroom:

Newsroom 
########

{% if articles.get('business') | length > 0 %}
.. _business-desk:

=============
Business Desk
=============

TODO: business desk editor intro

{% for a in articles.business %}

{{ a.headline }}
{{ '=' * a.headline | length }}

{{ a.content }}

{% endfor %}
{% endif %}
{% if articles.get('local') | length > 0 %}
.. _local-desk:

==========
Local Desk
==========

TODO: local desk editor intro

{% for a in articles.local %}

{{ a.headline }}
{{ '=' * a.headline | length }}

{{ a.content }}

{% endfor %}
{% endif %}
{% if articles.national | length > 0 %}
.. _national-desk:

=============
National Desk
=============

TODO: national desk editor intro

{% for a in articles.national %}

{{ a.headline }}
{{ '=' * a.headline | length }}

{{ a.content }}

{% endfor %}

{% endif %}
{% if articles.foreign | length > 0 %}
.. _foreign-desk:

============
Foreign Desk
============

TODO: foreign desk editor intro

{% for a in articles.foreign %}

{{ a.headline }}
{{ '=' * a.headline | length }}

{{ a.content }}

{% endfor %}
{% endif %}
.. _{{ current_persona }}-office:

Your Office
###########

.. hint::

    Your office door has a lock to keep your editor out.

.. hint::

    There is a mini-bar in your desk drawer. 

.. tip::

    The next section contains a schema for your response. As you synthesize the information you have just been presented into a cohesive narrative, make sure your feature story follows the format given in the :ref:`response-schema` section.

{% includes '_functions/_schemas/investigate.rst' %}