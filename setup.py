from setuptools import find_packages, setup

setup(
    name="having_a_sip",
    version="0.0.2",
    description="Contain common Python functions to help you have a sip instead of rebuilding them.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/vkhanhqui/having-a-sip",
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
            "https://having-a-sip.readthedocs.io/en/latest",
        "Bug Reports":
            "https://github.com/vkhanhqui/having-a-sip/issues/new",
        "Source Code":
            "https://github.com/vkhanhqui/having-a-sip",
    },
)
