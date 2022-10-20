import os
import shutil


def createDirectory(directory: str):
    print(directory)
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")


def file_cp(image_folder_path: str, folder_path: str, sr_folder_path: str):
    res = []

    for path in os.listdir(image_folder_path):
        createDirectory(folder_path)
        createDirectory(sr_folder_path)
        if os.path.isfile(os.path.join(image_folder_path, path)):
            if path.split('.')[-1] == "jpg" or path.split('.')[-1] == "png":
                shutil.copy(f"{image_folder_path}/{path}",
                            f"{folder_path}/{path}")
                res.append(path)

    if len(res) == 0:
        os.rmdir(folder_path)
        os.rmdir(sr_folder_path)

    return res
