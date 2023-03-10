import os
import boto3
from pulumi import automation

os.environ["PULUMI_CONFIG_PASSPHRASE"] = "test"

def test():
    stack = automation.select_stack(
        stack_name='dev',
        work_dir=os.path.join(os.path.dirname(__file__))
    )

    outputs = stack.outputs()
    arn = outputs['aws:dynamodb/table:Table:arn'].value.replace("table/", "")
    
    resource_name = arn.split(":")[-1]
    client = boto3.client('dynamodb')
    response = client.describe_table(
        TableName=resource_name,
    )

    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
            