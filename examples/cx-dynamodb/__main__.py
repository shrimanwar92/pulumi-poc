import sys
sys.path.append('../../')
from lib.dynamodb import CxDynamoDB
from main import MyComponent

class CxDynamoDBComponent(MyComponent):
    def __init__(self, name, **opts):
        super().__init__(self.__class__.__name__, name, opts)

        my_table = CxDynamoDB(
            self,
            table_name="my-dd-table"
        )

        self.print_outputs({
            'table_name': my_table.dynamodb.name,
            'table_arn': my_table.dynamodb.arn
        })

# create the custom dynamodb component
CxDynamoDBComponent('my-dynamodb-component')
