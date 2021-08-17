from pprint import pprint
import boto3
import json

def lambda_handler(event, context):
    
    ec2 = boto3.client('ec2',region_name='sa-east-1')
    #Lista info do SG
    sg_info = ec2.describe_security_groups()
    pprint(sg_info)
    #Lista infos do ACL
    sg = ec2.describe_network_acls()
    pprint(sg)