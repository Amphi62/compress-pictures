def build_name(name: str) -> str:
    if '/' in name:
        return name.split('/')[-1]

    if '\\' in name:
        return name.split('\\')[-1]

    return name


def get_start_url(url_file: str) -> str:
    """
    Remove the last element of an url
    :param url_file: url of our file
    :return: url without last element
    """
    if '/' in url_file:
        path = url_file.split('/')
        return '/'.join(path[:-1])
    else:
        path = url_file.split('\\')
        return '\\'.join(path[:-1])

