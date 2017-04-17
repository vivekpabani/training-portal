import os

from django.conf import settings


def create_path_string(in_path):
    """

    """

    in_path_string = os.path.join(*in_path.split('/'))

    abs_path_string = (os.sep).join([settings.BASE_DIR, settings.TOPICS_URL, in_path_string])

    return abs_path_string

def is_valid_path(path_string):
    """

    """

    return os.path.exists(path_string)
