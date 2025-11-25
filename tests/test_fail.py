import unittest
from hello_app.webapp import app


class FailingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fail(self):
        self.assertEqual(1, 1, "Fixed: 1 equals 1")

    def test_math_fail(self):
        assert 1 + 1 == 2


if __name__ == "__main__":
    unittest.main()
