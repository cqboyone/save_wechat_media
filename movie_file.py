import os
import shutil
import traceback


def movie_dat(src_path, target_path, file):
    print("from=" + repr(src_path))
    print("to=" + repr(target_path))
    print("file=" + repr(file))
    src_file = os.path.join(src_path, file)
    print("源文件完整路径=" + src_file)
    if not os.path.exists(src_file):
        print("源文件不存在，退出任务")
        return
    if not os.path.exists(target_path):
        print("目标路径不存在，创建文件夹")
        os.mkdir(target_path)
    target_file = os.path.join(target_path, file)
    print("目标文件完整路径=" + target_file)
    try:
        shutil.move(src_file, target_file)
    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == "__main__":
    pass
