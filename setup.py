from setuptools import setup, find_packages

MAJOR = 0
MINOR = 0
PATCH = 1
VERSION = f"{MAJOR}.{MINOR}.{PATCH}"


def get_install_requires():
    reqs = []
    return reqs


setup(
    name="xx",  # 包名称
    version=VERSION,  # 包版本
    author="Shawn Chen",  # 作者
    author_email="cs@cstos.com",  # 作者邮箱, user_email
    license="Apache",  # 协议缩写
    url="https://github.com/icstos/xx.git",
    description="",  # 工具包简单描述
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.12",
    install_requires=get_install_requires(),  # 工具包的依赖包
    packages=find_packages(),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    package_data={"": ["*.csv", "*.txt", ".toml"]},
    include_package_data=True,
)
