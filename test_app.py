# test_app.py
import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello from Azure DevOps CI/CD Pipeline!")

if __name__ == "__main__":
    unittest.main()
