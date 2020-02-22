from setuptools import setup

setup(
    name="sql-reporter",
    version="0.0.1",
    install_requires=["openpyxl", "MySQL-Python", "boto3"],
    extras_require={
        "develop": ["openpyxl", "MySQL-Python", "boto3"]
    },
    entry_points={
        "console_scripts": [
            "sql-reporter = main:main"
        ]
    }
)