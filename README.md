# Green Recorder

![Green Recorder](http://i.imgur.com/jrnNy17.png)

## About

A simple yet functional desktop recorder for Linux systems. Built using Python, GTK+ 3 and ffmpeg. It supports recording audio and video on almost all Linux interfaces. Also, Green Recorder is the **first desktop program to support Wayland display server on GNOME session**.

The following formats are currently supported: **mkv**, **avi**, **mp4**, **wmv** and **nut** (And only WebM for Wayland's GNOME session). You can stop the recording process easily by right-clicking the icon and choosing "Stop Record". Or middle-clicking the recording icon in the notifications area (but doesn't work on all interfaces).

Green recorder uses the default audio device you have to record. So if you want to change the audio input source, you just need to change it from the system-side (using **pavucontrol** for example).

By default, On Wayland only, Green Recorder uses the V8 encoder instead of the default V9 encoder in GNOME Shell because of the CPU & RAM consumption issue with V9. Which - now - should also give you better performance. On Xorg, each format uses its own default encoder.

This is a recording sample for DOTA 2 running on Wayland: [https://www.youtube.com/watch?v=kwCRBoOdJzU](https://www.youtube.com/watch?v=kwCRBoOdJzU)

## Download

### Ubuntu 16.04/16.10/17.04 or Linux Mint 18/18.1

Make sure you have enabled the multiverse and universe repositories before trying to install the program from the PPA (to be able to download the dependencies). You can install Green Recorder from the following PPA:

    sudo add-apt-repository ppa:mhsabbagh/greenproject
    sudo apt update
    sudo apt install green-recorder

### Debian

You can grab the Debian packages directly from the PPA itself and install it on any Debian distribution. You mainly need the "green-recorder" package and "python-pydbus". Other dependancies (like ffmpeg) are probably in Debian repositories: http://ppa.launchpad.net/mhsabbagh/greenproject/ubuntu/pool/main/

### Fedora 24/25/26

Unfortunately, Fedora removed our Copr repo because of it's depending on ffmpeg without any notification or message. Users who would like to use Green Recorder on Fedora should try the steps under "Other Distributions" section below.
     
### Arch Linux

You can install Green recorder using your [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers):

    yaourt -S green-recorder-git

### Other Distributions

The program requires the pydbus python module, install it first:

    sudo pip install pydbus
    
The source code is available to download via: [https://github.com/green-project/green-recorder/archive/master.zip](https://github.com/green-project/green-recorder/archive/master.zip). You can simply download it and install the dependencies on your distribution (gir1.2-appindicator3, gawk, python-gobject, python-urllib3, x11-utils, ffmpeg, pydbus). And then run: 

    sudo python setup.py install

Make sure you are running it with Python 2. It doesn't work currently with Python 3.
    
## Contact

The program is released under GPL 3. For contact: mhsabbagh[at]outlook.com.
