from setuptools import find_packages, setup

setup(
    name="having_a_sip",
    version="0.0.1",
    description="Contain common Python functions which I used.",
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
            "https://github.com/vkhanhqui/having-a-sip",
        "Bug Reports":
            "https://github.com/vkhanhqui/having-a-sip/issues/new",
        "Source Code":
            "https://github.com/vkhanhqui/having-a-sip",
    },
)
