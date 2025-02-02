terraform {
    backend "s3" {
        bucket                          = "cumberland-cloud-terraform-state"
        key                             = "web/elara/terraform.tfstate"
        region                          = "us-east-1"
    }
}

provider "aws" {
    region                              = "us-east-1"
}

locals {
    platform                            = {
        client                          = "CUMBERLAND CLOUD"
        environment                     = "PRODUCTION"
    }
    kms                                 = {
        aws_managed                     = true
    }
}

module "bucket" {
    source                              = "github.com/cumberland-terraform/storage-s3.git"
    
    platform                            = local.platform
    kms                                 = local.kms
    s3                                  = {
        purpose                         = "Hosting of static web content for the Elara Protocol website"
        suffix                          = "elara"
        website_configuration           = {
            enabled                     = true
        } 
    }
}

module "distribution" {
    source                              = "github.com/cumberland-terraform/network-cdn.git"
    
    platform                            = local.platform
    kms                                 = local.kms
    s3                                  = module.bucket.bucket[0]
    cdn                                 = {
        domain                          = "elara.chinchalinchin.com"
        name                            = "elara"
    }

}


module "build" {
    source                              = "github.com/cumberland-terraform/orchestrate-build.git"

    platform                            = local.platform
    kms                                 = {
        aws_managed                     = true
    }
    connection                          = {
        provider_type                   = "GitHub"
    }
    pipeline                            = {
        source_stage                    = {
            action                      = {
                configuration           = {
                    FullRepositoryId    = "https://github.com/chinchalinchin/elara"
                    BranchName          = "pypi"
                }
            }
        }
    }
    secrets                             = [ "cumberland-cloud/pypi" ]
    suffix                              = "elara"
}