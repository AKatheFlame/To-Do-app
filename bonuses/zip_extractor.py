import zipfile


def extract_archive(filepath, dest_dir):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive('compressed.zip', "D:\Projects\Python\To-Do app\bonuses\dest")
