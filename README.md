# Reddit Wallpaper
Retrieves the top reddit image of the day from a selected list of subreddits and sets it as wallpaper.

Installation (Windows)
-------------
 - Download latest setup file from here: https://github.com/Der-Eddy/reddit_wallpaper/releases
 - Run the Setup

 Running the script (With installed Python - No Setup)
 -------------
  - Run `python wallpaper.py`

Requirements
-------------

 - Windows 7 or higher or a Linux with Gnome (i.e. Debian)
 - Python 3.3 or higher
 - [requests](http://docs.python-requests.org/en/master/user/install/#install)

Building (Windows)
-------------
 - Install [PyInstaller](http://www.pyinstaller.org/)
 - Run `pyinstaller --windowed --upx-dir={UPX-DIR} --distpath=dist -y --clean --icon icon.ico wallpaper.py`
 - Install [Inno Setup](http://www.jrsoftware.org/isinfo.php)
 - Compile `setup.iss`, you may want to change some parameters like paths

Screenshots
-------------
No GUI version currently available

ToDo
-------------
- [x] Core method
- [ ] GUI
- [ ] Support for more Linux' (i.e. KDE)
- [ ] Autostart functionality
- [ ] Installation through pip
- [x] Standalone installation

License
-------------

    The MIT License (MIT)

    Copyright (c) 2016 Der-Eddy

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    The python module 'requests' is licensed under the Apache License, Version 2.0
    No changes to the core files were made.
    http://www.apache.org/licenses/LICENSE-2.0

    The icon for the `icon.png` and `icon.ico` is taken from Yummygum’s Iconsweets iconset,
    and is used under the terms of its license (http://yummygum.com/work/iconsweets).
