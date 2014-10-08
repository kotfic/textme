from setuptools import setup, find_packages

setup(
    name="textme",
    version="0.0",
    author="Christoper Kotfila",
    author_email="kotfic@gmail.com",
    license="GPL",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "textme = textme:main"
        ]
    }
)
