import gzip
import http
import logging

import requests
import urllib3

import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class GithubRetry(Framework.TestCase):
    def setUp(self):
        self.setPerPage(10)
        self.enableRetry(github.GithubRetry())
        super().setUp()

        https_request = urllib3.connection.HTTPSConnection.request
        https_getresponse = urllib3.connection.HTTPSConnection.getresponse

        last_request = []

        def request(connection, method, url, body=None, headers=None):
            logging.getLogger(__name__).info(f'intercepted request: {method} {url}')
            last_request.append(requests.Request(method, url))
            return https_request(connection, method, url, body=body, headers=headers)

        def getresponse(connection):
            req = last_request.pop()
            resp = https_getresponse(connection)
            if resp.status == 200:
                logging.getLogger(__name__).info(f'intercepted getresponse with 200')
            else:
                logging.getLogger(__name__).info(f'intercepted getresponse with {resp.status}: {resp.reason}')
                #response = requests.adapters.HTTPAdapter.build_response(None, req, resp)
                #content = gzip.decompress(response.content) if resp.headers.get('Content-Encoding') == 'gzip' else response.content
                #logging.getLogger(__name__).info(content)
            return resp

        urllib3.connection.HTTPConnection.request = request
        urllib3.connection.HTTPConnection.getresponse = getresponse

    def testPrimaryRateLimitHandling(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))

    def testSecondaryRateLimitHandling(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))
        self.assertTrue(False)

    def testSecondaryRateLimitHandling1(self):
        issues = self.g.search_issues("is:issue rate limit")
        with self.assertRaises(github.RateLimitExceededException):
            self.assertEqual(1, len([issue for issue in issues]))
