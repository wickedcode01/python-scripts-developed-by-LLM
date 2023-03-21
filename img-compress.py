import os
from PIL import Image
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog


def compress_image(infile, outfile, quality):
    try:
        with Image.open(infile) as im:
            im.save(outfile, optimize=True, progressive=True, quality=quality)
        return True
    except Exception as e:
        print(e)
        return False


def compress_images_in_folder(folder_path, quality):
    for root, dirs, files in os.walk(folder_path):
        for file in tqdm(files, desc="Compression Progress"):
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                infile = os.path.join(root, file)
                outfile = os.path.join(
                    root, file[:-4] + '-compressed' + file[-4:])
                compress_image(infile, outfile, quality)
                before_size = os.path.getsize(infile)
                after_size = os.path.getsize(outfile)
                print(
                    f"Before Compression Size: {before_size}, After Compression Size: {after_size}, File Path: {outfile}")


if __name__ == '__main__':
    quality = int(input('Please enter the compression rate (1-100):'))
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    if os.path.isdir(file_path):
        compress_images_in_folder(file_path, quality)
    elif os.path.isfile(file_path):
        outfile = os.path.join(os.path.dirname(file_path), os.path.basename(file_path)[
                               :-4] + '-compressed' + os.path.basename(file_path)[-4:])
        compress_image(file_path, outfile, quality)
        before_size = os.path.getsize(file_path)
        after_size = os.path.getsize(outfile)
        print(
            f"Before Compression Size: {before_size}, After Compression Size: {after_size}, File Path: {outfile}")
    else:
        print('Input error, please run the program again')
