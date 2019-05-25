#!/usr/bin/python
from distutils.core import setup
from subprocess import call
from glob import glob
from os.path import splitext, split

data_files = [ ("share/green-recorder", ["ui/ui.glade"]),
                    ("share/pixmaps", ["data/green-recorder.png"]),
                     ("share/applications", ["data/green-recorder.desktop"]) ] 

po_files = glob("po/*.po")
for po_file in po_files:
  lang = splitext(split(po_file)[1])[0]
  mo_path = "locale/{}/LC_MESSAGES/green-recorder.mo".format(lang)
  call("mkdir -p locale/{}/LC_MESSAGES/".format(lang), shell=True)
  call("msgfmt {} -o {}".format(po_file, mo_path), shell=True)
locales = map(lambda i: ('share/'+i, [i+'/green-recorder.mo', ]), glob('locale/*/LC_MESSAGES'))

data_files.extend(locales)

setup(name = "green-recorder",
      version = "3.2.3",
      description = "Record your desktop easily using a simple GUI",
      author = "M.Hanny Sabbagh", 
      author_email = "mhsabbagh@outlook.com",
      url = "https://github.com/foss-project/green-recorder/",
      license='GPLv3',
      scripts=['green-recorder'],
      data_files=data_files)
