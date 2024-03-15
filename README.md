# cloud-resume-challenge

# HTML & CSS
https://www.codecademy.com/learn/learn-html
https://www.codecademy.com/learn/learn-css
https://www.youtube.com/watch?v=Gz_7uDgwMBk

# Create a S3 bucket
    Bucket permission: Block all public access: On
    Access control list (ACL): Disable (bucket owner enforced)
    Upload: index.html, style.css to bucket

# Cloud front
Distribution:
    Default root object: index.html
    Alternate domain names: resume.oncloud.io.vn
    Custom SSL certificate (request new one): resume.oncloud.io.vn
Origins:
    Origin domain: Amazon S3 which created above
    Origin access: Choose OAC or OAI either (needed update bucket policy)
Domain name (Cloudflare):
    Create a CNAME record point to Cloudfront distribution domain name (eg: d212en38qkctml.cloudfront.net)

Origin:
    Origin domain: S3 bucket
    Origin access: Legacy (OAI) -> Yes, update the bucket policy

# Dynamodb
    Running locally
    Create table
    `aws dynamodb create-table --table-name ItemsTable --endpoint-url http://localhost:8000 --attribute-definitions AttributeName=id,AttributeType=S --key-schema KeyType=HASH,AttributeName=id --provisioned-throughput ReadCapacityUnits=2,WriteCapacityUnits=1
    List table
    `aws dynamodb list-tables --endpoint-url http://localhost:8000
    Put data
    `aws dynamodb put-item --table-name  --item '{ "id": {"S": "1"}, "FirstName": {"S": "Bill"}, "LastName": {"S": "Smith"} }' --return-consumed-capacity TOTAL --endpoint-url http://localhost:8000
    Scan data
    `aws dynamodb scan --table-name http-crud-tutorial-items --endpoint-url http://localhost:8000

# Lambda function

# API Gateway
https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html

# AWS SAM
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html
https://www.youtube.com/watch?v=QBBewrKR1qg


