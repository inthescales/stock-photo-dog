"""Unit tests for the stock-photo-dog bot"""

import unittest

from src.tests.tests import DogTests

if __name__ != '__main__':
    sys.exit(0)

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

# Add test cases
suite.addTest(loader.loadTestsFromTestCase(DogTests))

# Run tests
runner = unittest.TextTestRunner()
runner.run(suite)
