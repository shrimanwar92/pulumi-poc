import sys
sys.path.append('../../')
from lib.dynamodb import CxDynamoDB, CxDynamodbOpts
from main import MyComponent

class CxDynamoDBComponent(MyComponent):
    def __init__(self, name, **opts):
        super().__init__(self.__class__.__name__, name, opts)

        opts: CxDynamodbOpts = {
            'table_name': 'my-ddb-table',
            'read_capacity': 1,
            'write_capacity': 1
        }

        my_table = CxDynamoDB(self, opts)

        self.print_outputs({
            'table_name': my_table.dynamodb.name,
            'table_arn': my_table.dynamodb.arn
        })

# create the custom dynamodb component
CxDynamoDBComponent('my-dynamodb-component')
