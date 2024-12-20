
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

# Изменяем стиль каждого абзаца в документе
    for paragraph in doc.paragraphs:
        # Устанавливаем шрифт и размер шрифта
        for run in paragraph.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(14)

# Устанавливаем межстрочный интервал на 1.5
        paragraph.paragraph_format.line_spacing = 1.5


# functions модуль дляимпорта функций для решения задачи
   # Сохраняем изменения 
   doc.save(file_path) 

def change_format(folder_path):
    # Проходим по всем файлам в папке
    for filename in os.listdir(folder_path):
        if filename.endswith('.docx'):
            file_path = os.path.join(folder_path, filename)
            format_docx(file_path)
            print(f"Форматирование завершено для: {filename}")