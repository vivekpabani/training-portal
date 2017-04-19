from django import template
import os

register = template.Library()


@register.simple_tag
def get_dir_name(dir_path):
    """
    Return the directory name without parent path.
    """

    return os.path.basename(os.path.normpath(dir_path))
