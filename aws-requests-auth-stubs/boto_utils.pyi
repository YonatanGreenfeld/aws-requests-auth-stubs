import sys
from botocore.session import Session

from .aws_auth import AWSRequestsAuth

from typing import Optional

if sys.version_info <= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class Credentials(TypedDict):
    aws_access_key: str
    aws_secret_access_key: str
    aws_token: str


def get_credentials(credentials_obj: Optional[Session] = None):
    ...


class BotoAWSRequestsAuth(AWSRequestsAuth):
    def __init__(self, aws_host: str, aws_region: str, aws_service: str):
        ...
