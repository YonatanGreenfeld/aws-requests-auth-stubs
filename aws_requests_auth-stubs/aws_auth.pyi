import sys
from typing import overload

if sys.version_info >= (3, 8):
    from typing_extensions import TypedDict
else:
    from typing import TypedDict

from requests import PreparedRequest
from requests.auth import AuthBase

AwsAuthHeader = TypedDict(
    "AwsAuthHeader",
    {
        "Authorization": str,
        "x-amz-date": str,
        "x-amz-content-sha256": bytes,
    },
)

AwsAuthHeaderWithToken = TypedDict(
    "AwsAuthHeaderWithToken",
    {
        "Authorization": str,
        "x-amz-date": str,
        "x-amz-content-sha256": bytes,
        "X-Amz-Security-Token": str,
    },
)

def sign(key: bytes, message: str) -> bytes: ...
def getSignatureKey(key: str, dateStamp: str, regionName: str, serviceName: str) -> bytes: ...

class AWSRequestsAuth(AuthBase):
    aws_access_key: str
    aws_secret_access_key: str
    aws_host: str
    aws_region: str
    service: str
    aws_token: str | None = ...

    def __init__(
        self,
        aws_access_key: str,
        aws_secret_access_key: str,
        aws_host: str,
        aws_region: str,
        aws_service: str,
        aws_token: str | None = ...,
    ) -> None: ...
    def get_aws_request_headers_handler(self, r: PreparedRequest): ...
    @overload
    def get_aws_request_headers(
        self, r: PreparedRequest, aws_access_key: str, aws_secret_access_key: str, aws_token: None
    ) -> AwsAuthHeader: ...
    @overload
    def get_aws_request_headers(
        self, r: PreparedRequest, aws_access_key: str, aws_secret_access_key: str, aws_token: str
    ) -> AwsAuthHeaderWithToken: ...
    @classmethod
    def get_canonical_path(cls, r: PreparedRequest) -> str: ...
    @classmethod
    def get_canonical_querystring(cls, r: PreparedRequest) -> str: ...
