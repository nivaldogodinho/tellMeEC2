#Classe que busca as informações
import boto3

REGION_NAME='us-east-1'
EC2 = boto3.resource('ec2',REGION_NAME)
CLIENT = boto3.client('ec2')

for instance in EC2.instances.all():

    print("\n\t################## INSTANCE INFO #####################")
    print(f"\tInstance ID: {instance.id}"
          f"\tAMI ID: {instance.image_id}"
          f"\tState: {instance.state['Name']}"
          f"\n\tPriv. IP: {instance.private_ip_address}"
          f"\tPub. IP: {instance.public_ip_address}"
          f"\n\tPriv. DNS: {instance.private_dns_name}"
          f"\tPub. DNS: {instance.public_dns_name}"
        
    )

    print("\n\t##################### VPC INFO ###################")
    print(f"\tVPC ID: {instance.vpc_id}"
          f"\tSubnet ID: {instance.subnet_id}"
    )

    for i in range(len(instance.security_groups)):
        print(f"\tSG Name: {instance.security_groups[i]['GroupName']}"
              f"\tSG ID: {instance.security_groups[i]['GroupId']}"
        )

        #Necessário pegar o método correto para pegar o NACL
        print(f"\tNACL Name: {instance.security_groups[i]['GroupName']}"
              f"\tNACL ID: {instance.security_groups[i]['GroupId']}"
        )