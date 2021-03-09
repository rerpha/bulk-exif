import argparse
from exif import Image
from glob import  glob

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--raw", help="whether or not to edit raw files")
    # parser.add_argument("--make,-m")
    # parser.add_argument("--model,-b")
    # parser.add_argument("--lens,-l")
    # parser.add_argument("--film,-f")
    parser.add_argument('files', nargs='+')
    args = parser.parse_args()

    for _arg in args.files:
        for filename in glob(_arg):
            with open(filename, "rb") as file:
                image = Image(filename)
