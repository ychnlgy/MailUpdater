# MailUpdater

A Python module for easily sending mail updates to yourself.

This program only works for Gmail at the moment.

For the program to work, **you must enable [less secure app access](https://myaccount.google.com/security).**

## Quickstart

```python3

import mailupdater

username = input("Email address: ")

service = mailupdater.Service(username)

with service.create("Hello world") as email:
    email.write("Python is great for sending emails.")

# A new email will appear in your inbox.

```

You can also attach files and send multiple emails:

```python3

import mailupdater

username = input("Email address: ")

service = mailupdater.Service(username)

with service.create("Vacation pix") as email:
    email.write("See attachments.")
    email.attach("file.txt")
    email.attach("image.png")
    email.write("These are my vacation pictures.")

with service.create("Reminder") as email:
    email.write("Did you see the previous email I sent?")

# Two new emails will appear in your inbox.

```

## Installation

```bash
pip3 install mailupdater
```

## Testing

Do:

```python3

import mailupdater

mailupdater.test()

```

Then follow the instructions of the program.

If the program finishes successfully, then you should see two new emails in your inbox.

