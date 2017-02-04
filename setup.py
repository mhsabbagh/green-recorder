#!/usr/bin/python
# -*- coding: utf-8 -*-
from distutils.core import setup

from subprocess import call

data_files = [ ("lib/green-recorder", ["ui.glade"]),
                     ("share/applications", ["green-recorder.desktop"]) ] 

setup(name = "green-recorder",
      version = "1.0.0",
      description = "Record your desktop easily using a simple GUI",
      author = "M.Hanny Sabbagh", 
      author_email = "mhsabbagh@outlook.com",
      url = "https://green-project.github.io/green-recorder/",
      license='GPLv3',
      scripts=['green-recorder'],
      data_files=data_files)
