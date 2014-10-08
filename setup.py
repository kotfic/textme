from setuptools import setup

setup(
    name="textme",
    version="0.0",
    author="Christoper Kotfila",
    author_email="kotfic@gmail.com",
    license="GPL",
    py_modules=['textme'],
    entry_points={
        "console_scripts": [
            "textme = textme:main"
        ]
    }
)

