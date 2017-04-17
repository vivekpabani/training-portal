import os

from django.conf import settings


def create_abs_path(in_path):
    """

    """

    in_path = os.path.join(*in_path.split('/'))

    abs_path = (os.sep).join([settings.BASE_DIR, settings.TOPICS_URL, in_path])

    return abs_path

def is_valid_path(abs_path):
    """

    """

    return os.path.exists(abs_path_string)

