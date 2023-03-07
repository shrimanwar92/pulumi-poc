import sys
sys.path.append('../../')
from lib.s3 import CxS3
from main import MyComponent

class CxS3Component(MyComponent):
    def __init__(self, name, **opts):
        super().__init__(self.__class__.__name__, name, opts)

        my_bucket = CxS3(self)

        self.print_outputs({
            'bucket_name': my_bucket.bucket.bucket,
            'bucket_arn': my_bucket.bucket.arn
        })

b = CxS3Component('ss')
