import sys
sys.path.append('../../')
from lib.s3 import CxS3, CxS3Options
from main import MyComponent

class CxS3Component(MyComponent):
    def __init__(self, name, **opts):
        super().__init__(self.__class__.__name__, name, opts)

        opts: CxS3Options = {
            'bucket_name': 'my-test-bucket'
        }
        my_bucket = CxS3(self, opts)

        self.print_outputs({
            'bucket_name': my_bucket.bucket.bucket
        })

# create the custom s3 bucket component
CxS3Component('my-s3-component')
