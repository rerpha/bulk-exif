import argparse
from typing import BinaryIO
from exif import Image
from glob import glob

RAW_FILE_EXTS = (".raw", ".dng", ".nef")


def apply_exif_edits(
    file: BinaryIO,
    make: str,
    model: str,
    lens_make: str,
    lens_model: str,
    film: str,
    iso: int,
    focal_length: int,
):
    image = Image(file)
    image.make = make
    image.model = model
    # Not working on 3.10.4
    # image.lens_make = lens_make
    # image.lens_model = lens_model
    if film:
        pass
    if focal_length:
        image.focal_length = focal_length
    image.iso = iso
    return image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r", "--raw", help="whether or not to edit raw files", type=bool, default=False
    )
    parser.add_argument("-m", "--make", required=True)
    parser.add_argument("-b", "--model", required=True)
    parser.add_argument("-l", "--lens-make", required=True)
    parser.add_argument("-L", "--lens-model", required=True)
    parser.add_argument("-i", "--iso", type=int, required=True)
    parser.add_argument("-f", "--film")
    parser.add_argument("-F", "--focal-length", type=int)
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()

    for _arg in args.files:
        for filename in glob(_arg):
            if filename.lower().endswith(RAW_FILE_EXTS) and not args.raw:
                print(f"ignoring {filename}, not JPG!")
            with open(filename, "rb") as in_file, open(filename, "wb") as out_file:
                image = apply_exif_edits(
                    in_file,
                    args.make,
                    args.model,
                    args.lens_make,
                    args.lens_model,
                    args.film,
                    args.iso,
                    args.focal_length,
                )
                if "y" in input(f"overwrite {filename}?").lower():
                    out_file.write(image.get_file())
