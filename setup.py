from setuptools import setup

setup(
    name="mailupdater",
    version="1.0.0",
    description="Easily send mail updates to yourself.",
    url="https://github.com/ychnlgy/MailUpdater",
    author="Yuchen Li",
    author_email="ychnlgy@gmail.com",
    license="MIT",
    py_modules=[
        "mailupdater",
        "example",
        
        "src/__init__",
        "src/Email",
        "src/EmailService",
    ],
)
