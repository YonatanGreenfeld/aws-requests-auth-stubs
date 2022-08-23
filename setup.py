import os

from setuptools import setup


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, "", 1)
            stubs.append(path)
    return {package: stubs}


with open("README.md") as f:
    readme = f.read()

setup(
    name="aws_requests_auth-stubs",
    version="0.4.3.1",
    author="Yonatan Greenfeld",
    author_email="yonatangreenfeld97@gmail.com",
    description="PEP 561 stubs for aws-requests-auth",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/YonatanGreenfeld/aws-requests-auth-stubs",
    license="MIT",
    packages=["aws_requests_auth-stubs"],
    python_requires=">=3.7",
    # PEP 561 requires these
    install_requires=[
        "aws-requests-auth>=0.4.3",
        "botocore-stubs>=1.27.42",
        "types-requests>=2.25.0",
        'typing_extensions>=3.7.4; python_version<"3.8"',
    ],
    package_data=find_stubs("aws_requests_auth-stubs"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
    ],
)
