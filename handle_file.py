# -*- coding: utf-8 -*-

import os
import ntchat
import movie_file
import time
import dat2pic
from config import config


# 处理文件
def do(message):
    msg_type = message.get("type")
    data = message.get("data")
    from_wxid = data.get("from_wxid")
    room_wxid = data.get("room_wxid")
    print(room_wxid)
    # self_wxid = wechat_instance.get_login_info()["wxid"]
    # 只过滤这几个群
    if not need_save_file(room_wxid):
        return

    # 处理文件
    to_path = config().get("to_path")
    if ntchat.MT_RECV_VIDEO_MSG == msg_type:
        print("处理视频")
        video = data.get("video")
        dir_name, file_name = os.path.split(video)
        # 等待文件生成
        make_sure_file_exists(video)
        dir_video = os.path.join(to_path, "video")
        print("准备存储到：" + dir_video)
        movie_file.movie_dat(dir_name, dir_video, file_name)
    elif ntchat.MT_RECV_IMAGE_MSG == msg_type or ntchat.MT_RECV_PICTURE_MSG == msg_type:
        print("处理图片")
        image = data.get("image")
        # 等待文件生成
        make_sure_file_exists(image)
        dir_pic = os.path.join(to_path, "pic")
        print("准备存储到：" + dir_pic)
        # 图片需要解码
        dat2pic.do_file(image, dir_pic)
        # 后面还要删除源文件
        os.remove(image)


# 是否需要保存文件
def need_save_file(room_wxid):
    room_list = config().get("room_list")
    # 只过滤这几个群
    if room_wxid not in room_list:
        return False
    return True


# 确保文件生成
def make_sure_file_exists(file_path):
    wait_time = 0
    while True:
        if os.path.exists(file_path) or wait_time > 5:
            break
        else:
            time.sleep(1)
            wait_time = wait_time + 1
            continue


if __name__ == "__main__":
    pass
