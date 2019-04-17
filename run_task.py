import boto3
def handler(event,context):
  client = boto3.client('ecs')
  response = client.run_task(
  cluster='FG-cluster', # name of the cluster
  launchType = 'FARGATE',
  group = 'service:FG-service-apacheserver',
  taskDefinition='FG-test:2', # replace with your task definition name and revision
  count = 1,
  platformVersion='LATEST',
  networkConfiguration={
        'awsvpcConfiguration': {
            'subnets': [
                'subnet-25daba0b', # replace with your public subnet or a private with NAT
            ],
            'assignPublicIp': 'ENABLED'
        }
    })
  return str(response)
