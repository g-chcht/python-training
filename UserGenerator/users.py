"""Module to generate users"""
import logging
import os
from faker import Faker

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)

my_fake = Faker()


def get_user():
    """Generate a single user

    Returns:
        string: username
    """
    logging.info("Generating 1 user")
    return my_fake.name()


def get_users(n):
    """Generate multiple users

    Args:
        n (int): number of users

    Returns:
        list[str]: list of users
    """
    logging.info(f"Generating {n} users")
    return [get_user() for _ in range(n)]


if __name__ == "__main__":
    print(get_users(5))
