import os
import zipfile

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE) # получаем абсолютный путь к текущей директории где находится файл с которым работаем

PROJECT_ROOT = os.path.dirname(CURRENT_DIRECTORY)  # поднимаемся на уровень выше (в корень проекта)
RESOURCES_DIR = os.path.join(PROJECT_ROOT, 'resources')  # resources в корне проекта
TMP_DIR = os.path.join(RESOURCES_DIR, 'tmp')  # resources/tmp
ARCHIVE_DIR = os.path.join(RESOURCES_DIR, 'archive')  # resources/archive

TMP_DIR = os.path.abspath(TMP_DIR) # делаем путь абсолютным
ARCHIVE_DIR = os.path.abspath(ARCHIVE_DIR) # делаем путь абсолютным
ZIP_PATH = os.path.join(ARCHIVE_DIR, "files.zip") # делаем склейку пути к директории archive с файлом "files.zip"

def test_create_zip():
    if not os.path.exists(ARCHIVE_DIR):
        os.makedirs(ARCHIVE_DIR)
    with zipfile.ZipFile(ZIP_PATH, "w") as zf:
        for file in ["1mb.csv", "1mb.pdf", "1mb.xlsx"]:
            add_file = os.path.join(TMP_DIR, file)
            zf.write(add_file, os.path.basename(add_file))