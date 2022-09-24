#!/bin/bash

aws ec2 run-instances --image-id ami-07651f0c4c315a529 --count 1 --instance-type t2.micro --key-name aws-ec2