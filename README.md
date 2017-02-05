# Green Recorder

![alt text](https://raw.githubusercontent.com/green-project/green-recorder/master/Green%20Recorder.png)

## About

A simple yet functional desktop recorder for Linux systems. Built using Python, GTK+ 3 and ffmpeg. Currently it supports recording audio and video on almost all Linux interfaces. However, **Wayland support (GNOME session) is expected to be added soon**.

The following formats are currently available: **avi**, **mp4**, **flv**, **wmv** and **nut**. You can stop the recording process easily by middle-clicking the recording icon in the notifications area.

## Download

### Ubuntu 16.04/16.10

Make sure you have enabled the multiverse and universe repositories before trying to install the program from the PPA (to be able to download the dependencies). You can install Green Recorder from the following PPA:

    sudo add-apt-repository ppa:mhsabbagh/greenproject
    sudo apt install green-recorder

### Fedora 25

The program requires ffmpeg, which isn't available in Fedora's official repositories. You need to activate the rpmfusion repository and install the **ffmpeg** package first: https://rpmfusion.org/

Green Recorder is available to install from a Fedora Copr repository for Fedora 25:

     sudo dnf copr enable mhsabbagh/greenproject 
     sudo dnf install green-recorder

### Other Distributions

The source code is available to download via: https://github.com/green-project/green-recorder/archive/master.zip. You can simply download it and install the dependencies on your distribution (gir1.2-appindicator3, gawk, python-gobject, python-urllib3, x11-utils, ffmpeg). And then run: 

    sudo python setup.py install
    
## Contact

The program is released under GPL 3. For contact: mhsabbagh[at]outlook.com.
