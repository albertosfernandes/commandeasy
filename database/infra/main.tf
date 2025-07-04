provider "aws {
    region "us-east-1"
    access-key      = "access-key"
    secret_key      = "secret"
    skip_credentials_validation =   true
    endpoints {
        dynamodb = "http://localhost:8000"
    }
}

resource "aws_dynamodb_table" "comandos"
{
    name    = "ComandosTable
    billing_mode    =   "PAY_PER_REQUEST"
    hash_key        = "id"

    attribute {
        name = "id"
        type = "S" 
    }

    tags = {
        Environment = "local"
        Projeto = "CommandEasy"
    }
}