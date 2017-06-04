#!/usr/bin/python
from distutils.core import setup
from subprocess import call

data_files = [ ("share/green-recorder", ["ui/ui.glade"]),
                    ("share/pixmaps", ["data/green-recorder.png"]),
                     ("share/applications", ["data/green-recorder.desktop"]) ] 

setup(name = "green-recorder",
      version = "2.1.5",
      description = "Record your desktop easily using a simple GUI",
      author = "Green Project", 
      author_email = "mhsabbagh@outlook.com",
      url = "https://green-project.github.io/green-recorder/",
      license='GPLv3',
      scripts=['green-recorder'],
      data_files=data_files)
