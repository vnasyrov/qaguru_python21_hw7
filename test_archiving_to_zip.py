import os
import zipfile
from zipfile import ZipFile

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'tmp') # делаем склейку пути к текущей директории и папки tmp

with ZipFile("/Users/user/PycharmProjects/qaguru_python21_hw7", 'w') as zip_file: # создаем архив
    zip_file.write("/Users/user/PycharmProjects/qaguru_python21_hw7/tmp/1mb.csv", arcname='test_1mb.csv') # добавляем файл в архив
    zip_file.close()

# def create_archive():
#     if not os.path.exists('название папки в которой будет архив и его путь'): # проверяем существует ли папка
#         os.mkdir('название папки в которой будет архив и его путь') # создаем папку если её нет
#     with zipfile.ZipFile('название файла для архива и его путь', 'w') as zf: # создаем архив
#         for file in 'файлы которые нужно добавить в архив': : # добавляем файлы в архив
#             add_file = os.path.join('путь к файлам которые добавляют в архив', file) # склеиваем путь к файлам которые добавляют в архив
#             zf.write(add_file, os.path.basename(add_file)) # добавляем файл в архив
#     yield