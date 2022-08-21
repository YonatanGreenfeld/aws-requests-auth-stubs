from typing import Optional
import sys

if sys.version_info <= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from requests import PreparedRequest
from requests.auth import AuthBase

AwsAuthHeader = TypedDict('AwsAuthHeader',
                          {
                              'Authorization': str,
                              'x-amz-date': str,
                              'x-amz-content-sha256': bytes,
                              'X-Amz-Security-Token': str,
                          },
                          total=False)


def sign(key: bytes, message: str) -> bytes:
    ...


def getSignatureKey(key: str, dateStamp: str, regionName: str, serviceName: str) -> bytes:
    ...


class AWSRequestsAuth(AuthBase):
    aws_access_key: str
    aws_secret_access_key: str
    aws_host: str
    aws_region: str
    service: str
    aws_token: Optional[str] = None

    def __init__(self,
                 aws_access_key: str,
                 aws_secret_access_key: str,
                 aws_host: str,
                 aws_region: str,
                 aws_service: str,
                 aws_token: Optional[str] = None
                 ) -> None:
        ...

    def get_aws_request_headers_handler(self, r: PreparedRequest):
        ...

    def get_aws_request_headers(self, r: PreparedRequest, aws_access_key: str, aws_secret_access_key: str,
                                aws_token: str) -> AwsAuthHeader:
        ...

    @classmethod
    def get_canonical_path(cls, r: PreparedRequest) -> str:
        ...

    @classmethod
    def get_canonical_querystring(cls, r: PreparedRequest) -> str:
        ...
