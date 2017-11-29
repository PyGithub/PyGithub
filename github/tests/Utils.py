import mock
import sys
import unittest

from github.Utils import *

atLeastPython3 = sys.hexversion >= 0x03000000
TESTING_MODULE = "github.Utils"


class Utils(unittest.TestCase):

    def test_is_ipv4_address(self):
        """ Test case to test is_ipv4_address """
        ip = "198.168.1.1"
        self.assertTrue(is_ipv4_address(ip))

    def test_is_ipv4_address_with_invalid(self):
        """ Test case to test is_ipv4_address with invalid IP """
        ip = "github.com"
        self.assertFalse(is_ipv4_address(ip))

    def test_is_valid_cidr(self):
        """ Test case to test is_valid_cidr """
        data = (
            ("192.168.1.1/32", True),
            ("192.168.1.1", False),
            ("192.168.1.1:5000", False),
            ("192.168.1.1/0", False),
            ("192.168.1.1/44", False),
        )
        for ip, expected in data:
            self.assertEqual(is_valid_cidr(ip), expected, "IP {}, must return {}".format(ip, expected))

    def test_address_in_network(self):
        """ Test case to test address_in_network """
        data = (
            ("192.168.1.1", "192.168.1.0/24", True),
            ("192.168.1.1", "192.168.100.0/24", False),
        )
        for ip, net, expected in data:
            self.assertEqual(address_in_network(ip, net), expected, "IP {}, NET {}, must return {}".format(ip, net, expected))

    @mock.patch(TESTING_MODULE + ".os")
    def test_should_bypass_proxies(self, mock_os):
        """ Test case to test address_in_network """
        mock_os.environ = mock.MagicMock(spec=dict)
        environ = {
            'no_proxy': "192.168.1.1,192.168.1.3,.github.com",
            "http_proxy": "http://user:pass@192.168.1.100:8080",
            "https_proxy": "http://user:pass@192.168.1.100:8080",
        }

        def getitem(name):
            return environ[name]

        def setitem(name, val):
            environ[name] = val

        mock_os.environ.__getitem__.side_effect = getitem
        mock_os.environ.get.side_effect = getitem
        mock_os.environ.__setitem__.side_effect = setitem

        data = (
            ("http://192.168.1.1:8080", True),
            ("http://dev.github.com", True),
            ("http://google.com", False),
            ("http://google.com:5000", False),
            ("http://192.168.1.25", False),
            ("http://192.168.1.25:8000", False),
        )
        for ip, expected in data:
            self.assertEqual(should_bypass_proxies(ip), expected, "IP {}, must return {} to bypass proxy".format(ip, expected))
