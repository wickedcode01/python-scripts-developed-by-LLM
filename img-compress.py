import os
from PIL import Image
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def compress_image(infile, outfile, quality):
    try:
        with Image.open(infile) as im:
            im.save(outfile, optimize=True,progressive=True,quality=quality)
        return True
    except Exception as e:
        print(e)
        return False

def compress_images_in_folder(folder_path, quality):
    for root, dirs, files in os.walk(folder_path):
        for file in tqdm(files, desc="压缩进度"):
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                infile = os.path.join(root, file)
                outfile = os.path.join(root, file[:-4] + '-compressed' + file[-4:])
                compress_image(infile, outfile, quality)
                before_size = os.path.getsize(infile)
                after_size = os.path.getsize(outfile)
                print(f"压缩前大小：{before_size}，压缩后大小：{after_size}，文件路径：{outfile}")

if __name__ == '__main__':
    quality = int(input('请输入压缩率（1-100）：'))
    file_path = filedialog.askopenfilename()
    if os.path.isdir(file_path):
        compress_images_in_folder(file_path, quality)
    elif os.path.isfile(file_path):
        outfile = os.path.join(os.path.dirname(file_path), os.path.basename(file_path)[:-4] + '-compressed' + os.path.basename(file_path)[-4:])
        compress_image(file_path, outfile, quality)
        before_size = os.path.getsize(file_path)
        after_size = os.path.getsize(outfile)
        print(f"压缩前大小：{before_size}，压缩后大小：{after_size}，文件路径：{outfile}")
    else:
        print('输入有误，请重新运行程序')
