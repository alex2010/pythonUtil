import os
import shutil



def search_files(path, ext, size=0.5 * 1024 * 1024, mode='greater'):
    if not path or not ext:
        raise ValueError("Please provide both path and extension.")
    files = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            if filename.lower().endswith(ext):
                file_size = os.path.getsize(file_path)  # convert to MB
                if (mode == 'greater' and file_size > size) \
                        or (mode == 'less' and file_size < size) \
                        or (mode == 'equal' and file_size == size):
                    files.append({'path': file_path, 'size': file_size, 'name': filename})
    return files


def copy_files(file_list, dest_path, remove_original=False):
    try:
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        for file_dict in file_list:
            file_path = file_dict['path']
            file_name = file_dict['name']
            shutil.copy(file_path, os.path.join(dest_path, file_name))
            if remove_original:
                os.remove(file_path)
    except Exception:
        return False
    return True


def prompt():
    path = input("Enter path: ") or '/Users/alexwang/Downloads'
    ext = input("Enter extension, default is psd: ") or 'psd'
    size_str = input("Enter size (in byte), default is 1024 * 1024: ") or 1024 * 1024
    mode = input("Enter mode (greater, less, equal), default is greater: ").lower() or 'greater'
    try:
        size = float(eval(size_str))
    except ValueError:
        print("Invalid size, defaulting to 1 MB")
    try:
        files = search_files(path, ext, size, mode)
    except ValueError:
        print(ValueError)
        return
    print("Results:")
    for file in files:
        print(f"{file['name']} ({file['size'] / (1024 * 1024):.0f}MB, {file['size']} byte)")
        print(file['path'])
        print()

    new_path = input("Copy files to new path? ")

    if new_path:
        is_keep = input("Remove old files? Enter y for yes: ") or False
        copy_files(files, new_path, is_keep)


prompt()
