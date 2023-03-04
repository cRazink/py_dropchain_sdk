import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="dropchain-sdk",
    version="0.0.1",
    author="DropChain",
    author_email="carter@dropchain.network",
    packages=["dropchain_sdk"],
    description="Build robust web3 applications seamlessly using existing language and frameworks.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="  ",
    license='MIT',
    python_requires='>=3.8',
    install_requires=["requests"]
)