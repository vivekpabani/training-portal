import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import (create_abs_path,
                    is_valid_path,
                    is_topic_file,
                    is_topic_dir,
                    get_topic_first_file,
                    get_topic_prev_file,
                    get_topic_next_file,
                    get_relative_path,
                    get_dir_name,
                    get_subdirs)


def home(request, in_path=None):

    abs_path = create_abs_path(in_path)

    if not is_valid_path(abs_path):
        messages.warning(request, "Requested page does not exist.")
        return redirect('/')

    context = dict()

    # if current path is a file from a topic
    # get prev and next page links and pass as context.

    if is_topic_file(abs_path):
        context['is_file'] = True
        context['current_file'] = abs_path

        prev_file = get_topic_prev_file(abs_path)
        if prev_file:
            context['prev_file'] = get_relative_path(prev_file)

        next_file = get_topic_next_file(abs_path)
        if next_file:
            context['next_file'] = get_relative_path(next_file)

    # if current path is a topic directory
    # get the first page and call this function again.
    # it will render that page with first condition in next call.

    elif is_topic_dir(abs_path):
        topic_first_file = get_topic_first_file(abs_path)

        return redirect('/' + get_relative_path(topic_first_file))

    # if current path is a dir with sub dirs or topic dirs
    # get list of non empty sub dirs and display.

    else:
        context['is_dir'] = True
        context['title'] = get_dir_name(abs_path).title()
        dirs = list(map(get_relative_path, get_subdirs(abs_path)))
        context['dirs'] = dirs

    return render(request, 'portal/home.html', context)
