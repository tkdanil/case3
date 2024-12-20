# project_1

# Есть 5 документов в формате .docx. Напишите скрипт, который изменит во всех документах:
# - шрифт – Times New Roman
# - размер шрифта – 14
# - межстрочный интервал – 1,5
# Используйте библиотеку python-docx

# Ссылка на файлы:
# https://drive.google.com/drive/folders/1zGuYE9Decw6_iS7T3WKfdzncTE51ZvOP?usp=sharing
import os
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import OxmlElement

# Функция для изменения формата документа
def format_docx(file_path):
    doc = Document(file_path)
