from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


setup(
    name="aws_requests_auth-stubs",
    maintainer="Yonatan Greenfeld",
    maintainer_email="yonatangreenfeld97@gmail.com",
    description="PEP 561 type stubs for aws-requests-auth",
    url="https://github.com/YonatanGreenfeld/aws-requests-auth-stubs",
    license="MIT",
    version="0.4.3",
    packages=["aws_requests_auth-stubs"],
    # PEP 561 requires these
    install_requires=[
        "aws-requests-auth>=0.4.3",
        "botocore-stubs>=1.27.42",
        'typing_extensions>=3.7.4; python_version<"3.8"',
    ],
    package_data=find_stubs("aws_requests_auth-stubs"),
    zip_safe=False,
)
