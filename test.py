import requests
import unittest
try:
    from mock import Mock
except:
    from unittest.mock import Mock

BASE = "http://127.0.0.1:8080/"

class APICheck(unittest.TestCase):
    def test_backlog_get(self):
        response = requests.patch(BASE + "sumthing", {})
        print(response.json())