import boto3

REGION_NAME='sa-east-1'
client = boto3.client('ec2',region_name=REGION_NAME)

#print("teste")
print("Instances Information:")
for instances in client.describe_instances()['Reservations']:
      for instance in instances['Instances']:
            print('InstanceId:' ,(instance['InstanceId']))
            print('InstanceType:' ,(instance['InstanceType']))
            print('KeyName:' ,(instance['KeyName']))
            print('LaunchTime:' ,(instance['LaunchTime']))
            print('Placement:' ,(instance['Placement']))
            print('SubnetId:' ,(instance['SubnetId']))
            print('VPCId' ,(instance['VpcId']))
            print('SecurityGroups:' ,(instance['SecurityGroups']))
            print('Tags:' ,(instance['Tags']))
            print('\n')
print("Security Group Information:")
for sgs in client.describe_security_groups()['SecurityGroups']:
      #for sg in sgs['0']:
      print('Description:' ,(sgs['Description']))
      print('SecurityGroupID' ,(sgs['GroupId']))
      print('SecurityGroupName' ,(sgs['GroupName']))
      print('IpPermissions:' ,(sgs['IpPermissions']))
      print('VPCId:' ,(sgs['VpcId']))
      print('\n')
for vpcs in client.describe_vpcs()['Vpcs']
      print()

            
           
      
            
