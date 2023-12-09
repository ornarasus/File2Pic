# File2Pic
**About the project:** A script encoding/decoding a file to/from an image

**Technology stack**
* *Image Processing*: Pillow

# Installation:
```bash
git clone https://github.com/ornarasus/File2Pic.git
cd File2Pic/
pip3 install -r requirements.txt
```

# Usage
```
usage: file2pic.py [-h] [-d] file_path picture_name

Encoding file (up to 2.5 GB) to picture

positional arguments:
  file_path     Absolute/relative path to the file
  picture_name  ONLY picture's name

options:
  -h, --help    show this help message and exit
  -d, --decode  decoding file from picture
```

# Usage Examples
1) Encode file.zip to pic.png `python3 file2pic.py file.zip pic`
1) Decode file.zip from pic.png `python3 file2pic.py -d file.zip pic`
