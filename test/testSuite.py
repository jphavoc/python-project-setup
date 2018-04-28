import unittest
import sys
from pathlib import Path
# Adds 'src'-folder to the PATH to allow module imports
sys.path.append(str(Path('../src').resolve()))
# Add here furhter imports, that my live in /src

      
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
    