import os
from django.conf import settings


def create_abs_path(in_path):
    """
    Given a relative topic path, create and return an absolute topic path
    using base dir and topics dir urls from settings.
    """

    in_path = os.path.join(*in_path.split('/'))

    return (os.sep).join([get_topics_basedir(), in_path])

def get_relative_path(abs_path):
    """
    Return relative path based on topics base directory. 
    """

    return os.path.relpath(abs_path, start=get_topics_basedir())

def get_topics_basedir():
    """
    Return base directory of the topics created from settings vars.
    """

    return (os.sep).join([settings.BASE_DIR, settings.TOPICS_URL])

def is_valid_path(abs_path):
    """
    A valid path is one which exists, and is without any relative current
    or parent dir tokens. Return true if abs_path is a valid path, else false.
    """

    path_tokens = abs_path.split(os.sep)

    is_valid = not('.' in path_tokens or '..' in path_tokens)

    return is_valid and os.path.exists(abs_path)

def is_topic_dir(abs_path):
    """
    Return true if abs_path is a path to a topic dir, else false. 
    """

    for item in os.listdir(abs_path):
        item_path = (os.sep).join([abs_path, item])

        if os.path.isdir(item_path):
            return False
 
    return True

def is_topic_file(abs_path):
    """
    Return true if abs_path is a path to a topic file, else false. 
    """

    return os.path.isfile(abs_path)

def get_topic_prev_file(abs_file_path):
    """
    Return previous file in topic dir if exists, else None.
    """

    file_name = get_file_name(abs_file_path)
    topic_dir = get_path_dir(abs_file_path)

    if file_name == '0':
        return None

    prev_file_name = str(int(file_name) - 1)
    prev_file_path = (os.sep).join([topic_dir, prev_file_name + '.html'])

    if os.path.exists(prev_file_path):
        return prev_file_path

    return None

def get_topic_next_file(abs_file_path):
    """
    Return next file in topic dir if exists, else None.
    """

    file_name = get_file_name(abs_file_path)
    topic_dir = get_path_dir(abs_file_path)

    next_file_name = str(int(file_name) + 1)
    next_file_path = (os.sep).join([topic_dir, next_file_name + '.html'])

    if os.path.exists(next_file_path):
        return next_file_path
    
    return None

def get_topic_first_file(abs_path):
    """
    Return first file from topic dir.
    For now, it is 1.html.
    """
    if is_topic_file(abs_path):
        topic_dir = get_path_dir(abs_path)
    else:
        topic_dir = abs_path

    return (os.sep).join([topic_dir, '1.html'])

def get_file_name(file_path):
    """
    Return filename without extention from the file_path.
    """

    return os.path.splitext(os.path.basename(file_path))[0]

def get_dir_name(dir_path):
    """
    Return the directory name without parent path.
    """

    return os.path.basename(os.path.normpath(dir_path))

def get_path_dir(path):
    """
    Return directory from the path.
    """

    return os.path.dirname(path)

def get_subdirs(abs_path):
    """
    Return list of non empty sub directories of given dir/path.
    """

    dirs = list()

    for dir in os.listdir(abs_path):
        dir_path = (os.sep).join([abs_path, dir])
        if os.path.isdir(dir_path) and os.listdir(dir_path):
            dirs.append(dir_path)

    return dirs
