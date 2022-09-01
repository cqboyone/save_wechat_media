# -*- coding: utf-8 -*-

"""
dat文件和源图片文件就是用某个数按字节异或了一下，异或回来就可以了，
A ^ B = C
B ^ C = A
A ^ C = B
假设png文件头是A，dat文件是C，用A和C文件头的字节异或就可以得出B，因
为图片的格式以png，jpg，gif为主，通过这三种文件格式的头两个字节和待
转换文件的头两个字节一一异或的结果相等就找到B了，同时也知道了文件的
格式
"""

import os
import binascii
import traceback


def get_top_2hex(path):
    """
    获取文件的前两个16进制数
    """
    data = open(path, 'rb')
    hexstr = binascii.b2a_hex(data.read(2))
    return str(hexstr[:2], 'utf8'), str(hexstr[2:4], 'utf8')


"""
JPG文件头16进制为0xFFD8FF
PNG文件头16进制为0x89504E
GIF文件头16进制为0x474946
"""


def parse(dir):
    firstV, nextV = get_top_2hex(dir)
    firstV = int(firstV, 16)
    nextV = int(nextV, 16)
    coder = firstV ^ 0xFF
    kind = 'jpg'

    if firstV ^ 0xFF == nextV ^ 0xD8:
        coder = firstV ^ 0xFF
        kind = 'jpg'
    elif firstV ^ 0x89 == nextV ^ 0x50:
        coder = firstV ^ 0x89
        kind = 'png'
    elif firstV ^ 0x47 == nextV ^ 0x49:
        coder = firstV ^ 0x47
        kind = 'gif'

    return coder, kind


def convert(file_path, to_path):
    if not os.path.exists(file_path):
        print("源文件不存在")
        return
        # 确保目标文件夹存在
    if not os.path.exists(to_path):
        os.mkdir(to_path)

    coder, kind = parse(file_path)

    dir_name, file_name = os.path.split(file_path)
    file_name = file_name + '.' + kind

    dat = open(file_path, "rb")
    pic = open(os.path.join(to_path, file_name), "wb")
    print("源文件名=" + file_path + "; 目标文件名=" + pic.name)

    print(pic)
    for cur in dat:
        for item in cur:
            pic.write(bytes([item ^ coder]))

    dat.close()
    pic.close()


# 转换多个文件
def do_dir(path, to_path):
    files = os.listdir(path)
    print('total files:{}'.format(len(files)))
    i = 0
    for file_name in files:
        try:
            print('{} ... {}'.format(i, file_name))
            file_path = os.path.join(path, file_name)
            convert(file_path, to_path)
            i += 1
        except Exception as e:
            traceback.print_exc()
            print(e)


# 转换单个文件
def do_file(path, to_path):
    try:
        convert(path, to_path)
    except Exception as e:
        traceback.print_exc()
        print(e)


if __name__ == "__main__":
    pass
