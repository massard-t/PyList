# coding: utf-8
def g_timestamp(name):
    matches = re.search("/\d{8}/", name)
    if matches:
        return matches.group(0)[1:-1]
    return False
