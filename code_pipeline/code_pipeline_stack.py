from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class CodePipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        bucket = s3.Bucket(self, "MyfirstBucket", versioned=True,
                           bucket_name="demo-bucket-beyond-the-cloud-98979867hhh",
                           block_public_access=s3.BlockPublicAccess.BLOCK_ALL)