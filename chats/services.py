"""This is a module with functions removed from the view file"""

def set_name_group(obj_first, obj_second):
    """The function sets the group names for the chat"""

    if obj_first.user.id > obj_second.id:
        thread_name = f'chat_{obj_first.user.id}-{obj_second.id}'
    else:
        thread_name = f'chat_{obj_second.id}-{obj_first.user.id}'
    return thread_name
