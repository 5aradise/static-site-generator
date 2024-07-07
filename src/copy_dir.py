import os
import shutil


def copy_dir(src: os.path, dst: os.path):
    if not os.path.exists(src):
        raise Exception("Source path doesnt exist:", src)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_dir_r(src, dst)


def copy_dir_r(src: os.path, dst: os.path):
    if os.path.isfile(src):
        shutil.copy(src, dst)
        return

    os.mkdir(dst)
    for src_entrie in os.listdir(src):
        copy_dir_r(os.path.join(src, src_entrie),
                   os.path.join(dst, src_entrie))
