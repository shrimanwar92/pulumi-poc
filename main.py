"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import Provider as AwsProvider
from typing import TypedDict, NotRequired

class MyComponentOptions(TypedDict):
    region: NotRequired[str]

class MyComponent(pulumi.ComponentResource):
    def __init__(self, component_name, name, opts: MyComponentOptions):
        super().__init__(f"pkg:index:{component_name}", name, opts)

        self.provider = AwsProvider('aws-provider',
                                    region=opts.get('region') or "us-west-2")

    def print_outputs(self, output_dict):
        for key, value in output_dict.items():
            pulumi.export(key, value)

