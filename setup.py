from setuptools import setup

packages = []
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="fastapi-random-git-tips",
    version="0.1.0",
    description="Random git tips with FastApi",
    url="http://github.com/atrakic/fastapi-random-git-tips.git",
    author="Admir Trakic",
    author_email="xomodo@gmail.com",
    license="MIT",
    include_package_data=True,
    install_requires=requirements,
    packages=packages,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
    ],
)
