#!python3

import os, sys


def is_exclude_dir(current_path, exclude_dirs):
    for d in exclude_dirs:
        print(f'current_path = {current_path} , d = {d}')
        v = current_path.find(d)
        if v > -1:
            return True
    return False


def delete_midiafile(filePath):
    ss = os.path.splitext(filePath)
    if ss[-1] == '.mp4' or ss[-1] == '.avi' or ss[-1] == '.mkv':
        os.remove(filePath)


def rename(dir_path, exclude_dirs, prefix):
    count = 0
    for fn in os.listdir(dir_path):
        if os.path.isdir(fn):
            print('#' * 20)
            print(f'dir = {fn}')
            print('#' * 20)
            continue

        full_path = os.path.join(dir_path, fn)
        if fn.startswith(".") == True:
            delete_midiafile(full_path)
            continue

        ss = os.path.splitext(fn)
        if len(ss) >= 2:
            ext = ss[-1]
            if ext == '.mp4':
                convert_name = dir_path + "/" + prefix + fn
                print(f'rename {fn} to {convert_name} ...')
                os.rename(full_path, convert_name)
                count += 1
    return count

    # for d,s,fs in os.walk(dir_path):
    #     for f in fs:
    #         full_path = os.path.join(d,f)
    #         if is_exclude_dir(full_path , exclude_dirs) is True:
    #             continue
    #
    #         ss = os.path.splitext(full_path)
    #         if len(ss) >= 2:
    #             ext = ss[-1]
    #             if ext == '.mp4':
    #                 print(f'rename to  {f} ...')


if __name__ == '__main__':
    count = rename("/Volumes/rm/tmp", ['JAV'], "[RM]")
    print(f'result count = {count}')
