import unittest

from src.tests.tests import DogTests

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader

# Add test cases
suite.addTest(loader.loadTestsFromTestCase(DogTests))

# Run tests
runner = unittest.TextTestRunner()
runner.run(suite)
