# functions модуль дляимпорта функций для решения задачи
   # Сохраняем изменения 
   doc.save(file_path) 
# Путь к папке с документами 
folder_path = '"C:\\Users\\Alex2\\кейс 3"'  # Замените на путь к вашей папке
# Проходим по всем файлам в папке 
for filename in os.listdir("C:\\Users\\Alex2\\кейс 3"): 
    if filename.endswith('.docx'): 
        file_path = os.path.join("C:\\Users\\Alex2\\кейс 3", filename) 
        format_docx(file_path) 
        print(f"Форматирование завершено для: {filename}")   