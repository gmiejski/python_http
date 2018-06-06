import os
import uuid

website_download_url = 'http://www.readlet.io/'
directory = '/tmp/cats'


def url_get():
    cat_name = str(uuid.uuid4())
    savefile = os.path.sep.join([directory.rstrip(os.path.sep), cat_name])
    import urllib.request
    download = urllib.request.urlretrieve
    download(website_download_url, savefile)


def clear_directory():
    pass
