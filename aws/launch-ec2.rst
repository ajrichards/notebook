https://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-keypairs.html

   ~$ aws ec2 create-key-pair --key-name AwsKeyPair --query 'KeyMaterial' --output text > AwsKeyPair.pem
   ~$ mv AwsKeyPair.pem ~/.aws/
   ~$ chmod 400 ~/.aws/AwsKeyPair.pem


1. sign into the console
2. click on ec2
3. go through and launch an instance

then use ssh

ssh ubuntu@ec2-xx-xxx-xx-xxx.us-west-2.compute.amazonaws.com -i ~/.aws/AwsKeyPair.pem
   
   
To delete the key-pair

   ~$ aws ec2 delete-key-pair --key-name AwsKeyPair
