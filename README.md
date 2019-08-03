# This project is archived, it's no longer under development. As the original developer, the work of maintaining and updating this program takes too much of my time, which I was giving for free, and I am no longer interested in working with things like ffmpeg/wayland/GNOME's screencaster or solving the issues related to them or why they don't work. If you would like to continue development, please feel free to fork the project according to the GPL license.

# Green Recorder

![Green Recorder](https://i.ibb.co/b1831W0/Screenshot-from-2019-03-21-12-21-02.png)

## About

A simple desktop recorder for Linux systems. Built using Python, GTK+ 3 and ffmpeg. It supports recording audio and video on almost all Linux interfaces. Also, Green Recorder is the **first desktop program to support Wayland display server on GNOME session**.

The following formats are currently supported: **mkv**, **avi**, **mp4**, **wmv**, **gif** and **nut** (And only WebM for Wayland's GNOME session). You can stop the recording process easily by right-clicking the icon and choosing "Stop Record". Or middle-clicking the recording icon in the notifications area (but doesn't work on all interfaces).

You can choose the audio input source you want from the list. You can also set the default values you want by simply changing them in the interface, and the program will save them for you for the next time you open it.

### How it works?

It uses the D-Bus API to connect to the built-in screencasting tool in GNOME Shell. It uses this to record video. To record audio, it launches an instance of ffmpeg in the background. After the recording is finished, it merges the two files into the WebM file.

For Xorg, it uses ffmpeg only for both audio and video.

By default, On Wayland only, Green Recorder uses the V8 encoder instead of the default V9 encoder in GNOME Shell because of the CPU & RAM consumption issue with V9. Which - now - should also give you better performance. On Xorg, each format uses its own default encoder.

Also, for GIF format, Green Recorder first records the required video as a raw video. And then it generated the GIF image from the raw video. In this way, you'll get an optimized GIF image size which is at least 10x better than the normal ffmpeg recording.

### Localization

Green Recorder supports localization. If you want to translate the program into your language, fork the repository on GitHub and create a new file under "po" folder with your language ISO code (like fr.po, de.po, cs.po..). And translate the strings from there.

Alternatively, you can open the green-recorder.pot file using programs like PoEdit and start translating.

## Download

### Ubuntu 18.04/18.10/19.04 or Linux Mint 19/19.1

Make sure you have enabled the multiverse and universe repositories before trying to install the program from the PPA (to be able to download the dependencies). You can install Green Recorder from the following PPA:

    sudo add-apt-repository ppa:fossproject/ppa
    sudo apt update
    sudo apt install green-recorder

### Arch Linux

You can install Green recorder using your [AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers):

    yaourt -S green-recorder-git

### Other Distributions

The program requires the pydbus python module, install it first:

    sudo pip install pydbus
    
The source code is available to download via: [https://github.com/green-project/green-recorder/archive/master.zip](https://github.com/green-project/green-recorder/archive/master.zip). You can simply download it and install the dependencies on your distribution (gir1.2-appindicator3, gawk, python-gobject, python-urllib3, x11-utils, ffmpeg, pydbus, pulseaudio, xdg-open (or xdg-utils), python-configparser, imagemagick). And then run: 

    sudo python setup.py install

Make sure you are running it with Python 2. It doesn't work currently with Python 3.
    
## License

The program is released under GPL 3.
