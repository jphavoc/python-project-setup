import unittest
import sys
import os
# Adds 'src'-folder to PYTHONPATH to allow module imports
sys.path.append(os.path.abspath(os.path.dirname(__file__).replace('/test', '')))

      
def suite():
    # Create suite object
    suite = unittest.TestSuite()
    # Add tests to suite
    #suite.addTest(...)
    # ...
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    # Run tests
    runner.run(test_suite)
    