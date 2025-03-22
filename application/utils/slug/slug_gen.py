from django.utils.text import slugify
from random import SystemRandom
import string


def generate_random_slug(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits, k=k
        )
    )

def new_slug(text, k=5):
    return slugify(text) + '-' + generate_random_slug(k)
