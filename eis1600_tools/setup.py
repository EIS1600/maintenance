#!/usr/bin/env python

from setuptools import setup

setup(name='eis1600_tools',
      version='0.1.0',
      packages=['eis1600_tools',
                'eis1600_tools.mui_handling',
                'eis1600_tools.mui_handling.test'],
      scripts=['eis1600_tools/bin/disassemble_into_mui_files.py'],
      package_data={'eis_tools': ['templates/yaml_template.yml']}
      )
