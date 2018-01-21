from setuptools import setup


setup(name='my-project',
      version='0.0.1',
      packages=['src'],
      entry_points={
          'console_scripts': [
              'my-project = src.__main__:main'
          ]
      },
      )
