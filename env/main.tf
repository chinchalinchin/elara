terraform {
    backend "s3" {
        bucket                  = "cumberland-cloud-terraform-state"
        key                     = "web/elara/terraform.tfstate"
        region                  = "us-east-1"
    }
}

provider "aws" {
    region                      = "us-east-1"
}

data "aws_iam_policy_document" "web_policy" {
  
  statement {
    effect                  = "Allow"
    actions                 = [ "s3:GetObject"]
    resources               = [ "*" ]

    principals {
      type                  = "*"
      identifiers           = [ "*" ]
    }
  }
}

module "bucket" {
    source                      = "github.com/cumberland-terraform/storage-s3.git"
    
    platform                    = {
        client                  = "CUMBERLAND CLOUD"
        environment             = "PRODUCTION"
    }
    
    s3                          = {
        purpose                 = "Hosting of static web content for the Elara website"
        suffix                  = "elara"
        kms_key                 = {
            aws_managed         = true
        }
        website_configuration   = {
            enabled             = true
        } 
    }
}