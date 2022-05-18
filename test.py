import requests
import unittest
try:
    from mock import Mock
except:
    # python3
    from unittest.mock import Mock

BASE = "http://127.0.0.1:8001/"

class APICheck(unittest.TestCase):
    def test_backlog_get(self):
        response = requests.patch(BASE + "video/2", {})
        print(response.json())