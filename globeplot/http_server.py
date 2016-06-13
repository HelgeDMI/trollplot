import os
import posixpath
import urllib
import threading
from pkg_resources import resource_filename
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

BASE = resource_filename('globeplot', '')
ROOT = os.path.join(os.path.split(BASE)[0], 'webgl_globe')

# modify this to add additional routes
ROUTES = (
    # [url_prefix ,  directory_path],
    ['', ROOT],  # empty string for the 'default' match
)


class RequestHandler(SimpleHTTPRequestHandler):
    """
    Adapted from:
    https://www.huyng.com/posts/modifying-python-simplehttpserver
    """
    def translate_path(self, path):
        """translate path given routes"""

        # set default root to cwd
        root = os.getcwd()

        # look up routes and set root directory accordingly
        for pattern, rootdir in ROUTES:
            if path.startswith(pattern):
                # found match!
                path = path[len(pattern):]  # consume path up to pattern len
                root = rootdir
                break

        # normalize path and prepend root directory
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = posixpath.normpath(urllib.unquote(path))
        words = path.split('/')
        words = filter(None, words)

        path = root
        for word in words:
            drive, word = os.path.splitdrive(word)
            head, word = os.path.split(word)
            if word in (os.curdir, os.pardir):
                continue
            path = os.path.join(path, word)

        return path



class GlobePlotServer(object):
    """
    Adapted from http://stackoverflow.com/a/19578604
    """

    server = None
    keep_alive = 4  # the webserver is only up for 4 seconds

    def __init__(self):

        if not GlobePlotServer.server:
            GlobePlotServer.server = HTTPServer(('localhost', 8000), RequestHandler)
            self.thread = threading.Thread(target=GlobePlotServer.server.serve_forever)
            self.thread.daemon = True

    def __enter__(self):
        if GlobePlotServer.server:
            self.up()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # http://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
        self.down()

    def up(self):
        if GlobePlotServer.server and self.thread:
            self.thread.start()
            print('Starting server on port {}'.format(GlobePlotServer.server.server_port))
        else:
            print('Server already running on port {}'.format(0))
        GlobePlotServer.keep_alive = 4

    def down(self):
        if GlobePlotServer.server:
            # This is currently necessary to give the webserver time enough
            # to serve the page...
            # TODO: Figure out how to improve this
            print('Will stop server in {} seconds'.format(GlobePlotServer.keep_alive))            
            import time
            time.sleep(GlobePlotServer.keep_alive)
            
            GlobePlotServer.server.shutdown()
            print('Stopping server on port {}'.format(GlobePlotServer.server.server_port))
            GlobePlotServer.server = None
