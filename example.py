#!/usr/bin/python3

'''

This program sends two emails to yourself.

The first email contains a short text.

The second email demonstrates how to send 
a multi-line message with two image attachments.

'''

import mailupdater

def main():
    username = input("Enter username: ")

    # The program uses Gmail as the default host.

    service = mailupdater.Service(username)

    # Send one email.

    with service.create("Hello world") as email1:
        email1.write("Python is great for sending emails.")

    # Send another email.

    with service.create("GANs can generate this horse") as email2:

        email2.write('''Hello!

        These images of a horse
        and a car are actually
        generated by a GAN 
        called ChainGAN. It
        was trained on CIFAR10.
        ''')

        email2.attach("samples/horse.png")
        email2.attach("samples/car.png")

        # Writing to the email multiple times is supported.

        email2.write("Please enjoy it.")
        email2.write("Regards,\n\nMr. Onion\n")

if __name__ == "__main__":
    main()