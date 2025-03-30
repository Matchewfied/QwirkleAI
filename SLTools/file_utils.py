from pathlib import Path


def create_directory(dir_name: str):
    dir_path = Path(dir_name)
    dir_path.mkdir(exist_ok=True)
    return dir_path


def create_sub_folder(main_dir_path: Path, folder_name: str):
    path = main_dir_path / folder_name
    path.mkdir(parents=True, exist_ok=True)
    return path


def create_sub_folders(main_dir_path: Path, folder_names: list):
    paths = [main_dir_path / folder_name for folder_name in folder_names]
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)
    return paths


def make_file_path(dir_path: Path, filename: str):
    return dir_path / filename


def make_file_path_str(dir_path: Path, filename: str):
    return str(make_file_path(dir_path, filename))
