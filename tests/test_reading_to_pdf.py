import io
import zipfile
from pypdf import PdfReader

from tests.test_archiving_to_zip import ZIP_PATH

def test_reading_to_pdf():

    expected_word = "File Details"

    with zipfile.ZipFile(ZIP_PATH) as zip_file:  # открываем архив
        with zip_file.open("1mb.pdf") as pdf_file:  # открываем файл в архиве
            reader = PdfReader(io.BytesIO(pdf_file.read())) # преобразуем байты в объект PDF (PdfReader)
            text = reader.pages[0].extract_text() # извлекаем текст из первой страницы и записываем в переменную 'text'
            print(text)

            if expected_word in text:
                print(f"✅ Словосочетание '{expected_word}' найдено в PDF!")
            else:
                print(f"❌ Словосочетание '{expected_word}' не найдено в PDF!")

            # assert "File Details" in text
