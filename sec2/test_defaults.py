from urllib.request import (HTTPHandler, install_opener, build_opener, addinfourl)
import os
import shutil
import tempfile
from io import StringIO
from defaults import download

ORIGINAL_FOLDER = os.getcwd()

class TestHTTPHandler(HTTPHandler):
    TEST_FOLDER = ''
    """Mock HTTP handler"""
    def http_open(self, req):
        resp = addinfourl(StringIO('test'), '', req.get_full_url(), 200)
        resp.msg = 'OK'
        return resp

    def setup(self):
        """Install the mock HTTP handler for unit tests."""
        install_opener(build_opener(TestHTTPHandler))
        self.TEST_FOLDER = tempfile.mkdtemp()
        os.chdir(self.TEST_FOLDER)

    def teardown(self):
        """Restore the normal HTTP handler."""
        install_opener(build_opener(HTTPHandler))
        # Go back to the original folder.
        os.chdir(ORIGINAL_FOLDER)
        # Delete the test folder.
        shutil.rmtree(self.TEST_FOLDER)

    def test_download(self):
        file = download("http://example.com/file.txt")
        # Check that the file has been downloaded.
        assert os.path.exists(file)
        # Check that the file contains the contents of the remote file.
        with open(file, 'r') as f:
            contents = f.read()
        #print(contents)
        assert contents == 'test'

    def test_download2(self):
        file = download("http://example.com")
        assert os.path.exists(file)