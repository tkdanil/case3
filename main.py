## main стартовый модуль проекта

from functions import format_docx, change_format 
import os 
 
def main(): 
    # Вызов функции change_format() 
    change_format ("C:\\Users\\Alex2\\кейс 3") 
 
def change_format(folder_path): 
    # Проход по всем файлам в папке 
    for filename in os.listdir("C:\\Users\\Alex2\\кейс 3"):  
        if filename.endswith('.docx'):  
            file_path = os.path.join("C:\\Users\\Alex2\\кейс 3", filename)  
            format_docx(file_path)  
            print(f"Форматирование завершено для: {filename}") 
 
# Инициализация скрипта 
if __name__- "__main__": 
    main()