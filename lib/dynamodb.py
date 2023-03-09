import pulumi
from pulumi_aws import dynamodb

class CxDynamoDB():
    def __init__(self, parent: pulumi.ComponentResource, **dbopts):
        self.dynamodb: dynamodb.Table = dynamodb.Table(
            resource_name=dbopts['table_name'],
            attributes=[
                dynamodb.TableAttributeArgs(
                    name='Id',
                    type='S'
                )
            ],
            hash_key='Id',
            read_capacity=1,
            write_capacity=1,
            opts=pulumi.ResourceOptions(parent=parent)
        )