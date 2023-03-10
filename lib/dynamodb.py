import pulumi
from pulumi_aws import dynamodb
from typing import TypedDict

class CxDynamodbOpts(TypedDict):
    table_name: str
    read_capacity: int
    write_capacity: int

class CxDynamoDB():
    def __init__(self, parent: pulumi.ComponentResource, dbopts: CxDynamodbOpts):
        self.dynamodb: dynamodb.Table = dynamodb.Table(
            resource_name=dbopts['table_name'],
            attributes=[
                dynamodb.TableAttributeArgs(
                    name='Id',
                    type='S'
                )
            ],
            hash_key='Id',
            read_capacity=dbopts.get('read_capacity'),
            write_capacity=dbopts.get('write_capacity'),
            opts=pulumi.ResourceOptions(parent=parent)
        )

        pulumi.export(f'{self.dynamodb._type}:arn', self.dynamodb.arn)