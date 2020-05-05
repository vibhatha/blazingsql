from pyblazing.apiv2 import S3EncryptionType
from pyblazing.apiv2 import DataType
from pyblazing.apiv2.context import BlazingContext

from cio import getProductDetailsCaller


__version__ = getProductDetailsCaller()["BLAZINGSQL_GIT_COMMIT_HASH"]
__branch_name__ = getProductDetailsCaller()["BLAZINGSQL_GIT_BRANCH"]
__branch_tag__ = getProductDetailsCaller()["BLAZINGSQL_GIT_DESCRIBE_TAG"]
__build_id__ = getProductDetailsCaller()["BLAZINGSQL_GIT_DESCRIBE_NUMBER"]
__compiler_version__ = getProductDetailsCaller()["CXX_COMPILER_ID"] + " " + getProductDetailsCaller()["CXX_COMPILER"] + " " + getProductDetailsCaller()["CXX_COMPILER_VERSION"]
__cuda_flags__ = getProductDetailsCaller()["CMAKE_CUDA_FLAGS"]


def info():
    print("BlazingSQL version (git hash): %s" % __version__)
    print("BlazingSQL branch name: %s" % __branch_name__)
    print("BlazingSQL branch tag: %s" % __branch_tag__)
    print("BlazingSQL build id: %s" % __build_id__)
    print("BlazingSQL compiler version: %s" % __compiler_version__)
    print("BlazingSQL cuda flags: %s" % __cuda_flags__, flush=True)
