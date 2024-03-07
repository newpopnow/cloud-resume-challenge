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
    Custom SSL certificate: resume.oncloud.io.vn

Origin:
    Origin domain: S3 bucket
    Origin access: Legacy (OAI) -> Yes, update the bucket policy

# Dynamodb
    Create table
    
# Lambda function