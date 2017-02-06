# Green Recorder

![alt text](https://raw.githubusercontent.com/green-project/green-recorder/master/Green%20Recorder.png)

## About

A simple yet functional desktop recorder for Linux systems. Built using Python, GTK+ 3 and ffmpeg. Currently it supports recording audio and video on almost all Linux interfaces. However, **Wayland support (GNOME session) is expected to be added soon**.

The following formats are currently available: **avi**, **mp4**, **flv**, **wmv** and **nut**. You can stop the recording process easily by right-clicking the icon and choosing "Stop Record". Or middle-clicking the recording icon in the notifications area (but doesn't work on all interfaces).

This is a recording sample using this program: [https://www.youtube.com/watch?v=RxXetUgtvrw](https://www.youtube.com/watch?v=RxXetUgtvrw)

**REMEMBER:** This is the first public version. It's in its very early stages. Please be patience.

## Download

### Ubuntu 16.04/16.10/17.04

Make sure you have enabled the multiverse and universe repositories before trying to install the program from the PPA (to be able to download the dependencies). You can install Green Recorder from the following PPA:

    sudo add-apt-repository ppa:mhsabbagh/greenproject
    sudo apt update
    sudo apt install green-recorder

### Fedora 24/25

Green Recorder is available to install from a Fedora Copr repository for Fedora 25:

     sudo dnf copr enable mhsabbagh/greenproject 
     sudo dnf install green-recorder

### Other Distributions

The source code is available to download via: [https://github.com/green-project/green-recorder/archive/master.zip](https://github.com/green-project/green-recorder/archive/master.zip). You can simply download it and install the dependencies on your distribution (gir1.2-appindicator3, gawk, python-gobject, python-urllib3, x11-utils, ffmpeg). And then run: 

    sudo python setup.py install
    
## TODO:

There's a big list of things to do right now. I might work on it if a lot of people need this program and its functionality:

* Add support for recording on Wayland (GNOME Shell Wayland Session, it offers a screencast tool, can be used).
* Add a checking method to see if ffmpeg already working properly or not before launching the tray.
* Add more possible formats supported by ffmpeg.
* Support more options like including the mouse pointer, recording a specific area and choosing input audio stream.
    
## Contact

The program is released under GPL 3. For contact: mhsabbagh[at]outlook.com.
