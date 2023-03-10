from pulumi_aws import s3
import pulumi
from typing import TypedDict, Required

class CxS3Options(TypedDict):
    bucket_name: Required[str]

class CxS3():
    def __init__(self, parent_component_instance: pulumi.ComponentResource, bucket_opts: CxS3Options):
        self.parent = parent_component_instance

        self.bucket: s3.Bucket = s3.Bucket(
            resource_name=bucket_opts.get('bucket_name'),
            tags={
                'name': 'test3653636'
            },
            opts=pulumi.ResourceOptions(parent=self.parent)
        )

        pulumi.export(f'{self.bucket._type}:arn', self.bucket.arn)