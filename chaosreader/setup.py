# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='chaosreader-rapid7-plugin',
      version='1.0.2',
      description='The plugin is used to trace sessions and fetch application data from snoop or tcpdump logs',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_chaosreader']
      )
