#Classe que busca as informações
import boto3

REGION_NAME='us-east-1'
EC2 = boto3.resource('ec2',REGION_NAME)
CLIENT = boto3.client('ec2')

for instance in EC2.instances.all():

    print("\t################## INSTANCE INFO #####################")
    print("\tInstance ID: {0}\tAMI ID: {1}\tState: {2}".format(
        instance.id,instance.image_id,
        instance.state['Name'],
    ))

    print("\tPriv. IP: {0}\tPub. IP: {1}".format(
        instance.private_ip_address,
        instance.public_ip_address
    ))

    print("\tPriv. DNS: {0}\tPub. DNS: {1}".format(
        instance.private_dns_name,
        instance.public_dns_name,
    ))

    print("\n\t##################### VPC INFO ###################")
    print("\tVPC ID: {0}\tSubnet ID: {1}".format(
        instance.vpc_id,instance.subnet_id
    ))

    for i in range(len(instance.security_groups)):
        print("\tSG Name: {0}\tSG ID: {1}".format(
            instance.security_groups[i]['GroupName'],
            instance.security_groups[i]['GroupId']
        ))

        print("\tNACL Name: {0}\tNACL ID: {1}".format(
            instance.security_groups[i]['GroupName'],
            instance.security_groups[i]['GroupId']
        ))