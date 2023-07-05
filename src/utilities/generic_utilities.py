import logging as logger
import random
import string


def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password.")

    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'test_user'

    random_str = ''.join(random.choices(string.ascii_letters, k=10))

    email = email_prefix + '_' + random_str + '@' + domain

    password = ''.join(random.choices(string.ascii_letters, k=20))

    logger.debug(f"Randomly Generate email/password are:"
                 f"Email: {email}"
                 f"Password: {password}")

    return {'email': email, 'password': password}
