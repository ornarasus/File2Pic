# File2Pic
**About the project:** A script encoding/decoding a file to/from an image

**Technology stack**
* *Image Processing*: Pillow

# Screenshots:
*TODO*

# Installation:
```bash
git clone https://github.com/ornarasus/File2Pic.git
cd File2Pic/
pip3 install -r requirements.txt
```

# Usage
```
usage: file2pic.py [-h] [-d] input output

Encoding file (up to 2.5 GB) in picture

positional arguments:
  input         Input file's path
  output        Output file's path

options:
  -h, --help    show this help message and exit
  -d, --decode  Decoding file from picture
```

# Usage Examples
1) Encode file.zip to pic.png `python3 file2pic.py file.zip pic`
1) Decode file.zip from pic.png `python3 file2pic.py -d pic file.zip`
