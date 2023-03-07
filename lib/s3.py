from pulumi_aws import s3
import pulumi

class CxS3():
    def __init__(self, parent_component_instance: pulumi.ComponentResource):
        self.parent = parent_component_instance

        self.bucket: s3.Bucket = s3.Bucket('my-bucket',
            tags={
                'name': 'test3653636'
            },
            opts=pulumi.ResourceOptions(parent=self.parent)
        )