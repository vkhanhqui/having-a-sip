from setuptools import find_packages, setup

setup(
    name="common_functions",
    version="0.0.1",
    description="Contain common Python functions which I used.",
    url="git@github.com:vkhanhqui/common-python-functions.git",
    author="Steve",
    author_email="vkhanhqui@gmail.com",
    license_files=("LICENSE"),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,
    install_requires=[
    ],
    python_requires=">=3.9",
    project_urls={
        "Documentation":
            "https://github.com/vkhanhqui/common-python-functions",
        "Bug Reports":
            "https://github.com/vkhanhqui/common-python-functions/issues/new",
        "Source Code":
            "https://github.com/vkhanhqui/common-python-functions",
    },
)
