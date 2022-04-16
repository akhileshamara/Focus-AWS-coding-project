# Focus-AWS coding project
 Full stack application managed using AWS

##Project Setup
- First, to setup of the project upload the Cloudformation.yml to api-gateway in your AWS account. 

    If needed, please change the hardcoded S3 bucket names and DynamoDB table names.Currently the resource names are hardcoded as below in cloudformation.yml:

        S3 input bucket : akhi-input-bucket
        S3 output bucket : akhi-output-bucket
        S3 bucket for script: akhi-fovus-scripts
        DynamoDB input table : Dynamo_input-s3-db
        DynamoDB output table : Dynamo_output-s3-db

- After upload procedd to create stack by keeping all default configuration given by AWS. After successful creation of stack, you can see all the resources created.

- Get the URL for the post request from (ApiGateway -> Stages-> prod) and update the url in the fetch operation of index.html(line no.62).create the bucket **fovus-frontend** and grant full permission to the bucket and upload index.html file provided. upload ec2scripts.py to s3 bucket(create the bucket akhi-fovus-scripts).

The setupt is complete now. You can upload files with a custom input text and click upload. The files are saved into s3 buckets and dynamo db.