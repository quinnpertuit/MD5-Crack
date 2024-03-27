# MD5-Crack
MD5 Crack is a tool that aims to crack an MD5 type hash by trying various combinations to find the appropriate keywords.

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Version: 1](https://img.shields.io/badge/Version-1-green.svg)
![Language: BASH](https://img.shields.io/badge/Language-BASH-blue.svg)
![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green.svg)

# Preview
------
```
~/MD5-Crack $ ./run.sh
 _____ ____  ___    _____             _
|     |    \|  _|  |     |___ ___ ___| |_
| | | |  |  |_  |  |   --|  _| .'|  _| '_|
|_|_|_|____/|___|  |_____|_| |__,|___|_,_|
      Author: msverse
      Homepage: https://www.msverse.site
Input hash MD5 ~# 7f138a09169b250e9dcb378140907378
Start Cracking...
Keyword Results ~# MD5
Time required ~# 1.02 Second
```

# MD5 Crack installation
------
```
- apt update && apt upgrade -y
- pkg install git -y
- pkg install python -y
- git clone https://github.com/MSVerse/MD5-Crack
- cd MD5-Crack
- chmod +x crack.py
- ./run.sh
```

# How to set the program tools
------
You can adjust the characters used to try keyword combinations according to your needs.

- Set of lowercase letters and numbers
```
all_chars = string.ascii_lowercase + string.digits
```
- Set of uppercase letters, lowercase letters and numbers
```
all_chars = string.ascii_letters + string.digits
```
- Set of uppercase letters, lowercase letters, numbers and special characters
```
all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{};:'\"<>,.?/\\|"
```
- Set Maximum Length
```
max_length = 100 # Customize
```

# Announcement
------
The longer the keyword, the more time it takes to solve it. You can adjust the maximum length and character for maximum results.

Please make sure your hash is md5 type and if you are not sure run the check.sh script. because the tool will still run even if you enter another type of hash.

# Support Me
[msverse](https://www.msverse.site) Help me by visiting my blog. 
