#!/usr/bin/env python3
import os
from dotenv import load_dotenv

load_dotenv()

import aws_cdk as cdk

from ec2_cdk.ec2_instance_stack import EC2InstanceStack

cdk_env = cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION'))

app = cdk.App()

app = cdk.App()
EC2InstanceStack(
    app, 
    'Ec2DeployStack',
    env=cdk_env
)

app.synth()