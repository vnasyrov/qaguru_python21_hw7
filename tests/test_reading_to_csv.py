import zipfile
import csv

from tests.test_archiving_to_zip import ZIP_PATH


def test_read_csv():
    with zipfile.ZipFile(ZIP_PATH) as zip_file: # открываем архив
        with zip_file.open("1mb.csv") as csv_file: # открываем файл в архиве
            content = csv_file.read().decode('utf-8-sig') # читаем содержимое файла и декодируем его если в файле есть символы не из английского алфавита
            csvreader = list(csv.reader(content.splitlines())) # читаем содержимое файла и преобразуем его в список
            second_row = csvreader[1] # получаем вторую строку
            print(second_row)
            assert second_row[0] == '1'  # проверка значения элемента в первом столбце второй строки
            assert second_row[1] == 'Miss Laurianne Bins IV' # проверка значения элемента во втором столбце второй строки