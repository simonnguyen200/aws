import boto3

def create_instance():
    ec2_client = boto3.client("ec2", region_name="ap-southeast-1")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="aws-ec2"
    )

