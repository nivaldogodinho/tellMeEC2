import boto3


client = boto3.client('ec2',region_name='us-east-1')

response = client.describe_instances()

#Informações sobre a Instancia ec2#

for info in response['Reservations']:
    for instance in info['Instances']:
        instance_id = instance ['InstanceId']
        instance_type = instance ['InstanceType']
        instance_priv_ipv4 = instance ['PrivateIpAddress']
        instance_subnetid = instance ['SubnetId']
        instance_vpcid = instance ['VpcId']
        instance_state_name = instance ['State']['Name']
        instance_state_code = instance ['State']['Code']
        instance_availability_zone = instance ['Placement']['AvailabilityZone']
        instance_security_name = instance ['SecurityGroups'] [0]['GroupName']
        print(f'{instance_id} - {instance_type} - {instance_state_name} - {instance_priv_ipv4} - {instance_availability_zone} - {instance_security_name} - {instance_subnetid} - {instance_vpcid} - {instance_priv_ipv4}')


#Informações do Security Group #  

        response=client.describe_security_groups()
print(f'{response}')
        
