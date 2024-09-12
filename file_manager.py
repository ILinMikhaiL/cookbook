import os.path
from pathlib import Path


#Получить список txt файлов в директории
def get_list_txt_files(_directory):
    txt_files = []

    for file in os.listdir(directory):
        if file.endswith(".txt"):
            txt_files.append(file)

    return txt_files


#Получить список текста файла
def get_list_text_file(filename):
    file = open(filename, encoding='utf-8')
    lines = file.read().splitlines()
    file.close()
    return lines


#def get_number_of_lines_file(filename):
#    lines = get_list_text_file(filename)
#    return len(lines)


# Очистка файла
def clear_existing_file(file_name):
    with open(file_name, 'w') as f:
        f.write('')
    return f


# Получить кортедж файла (имя файла, кол-во строк, список текста файла)
def get_turtle_info_file(name_file):
    list_text_file = get_list_text_file(name_file)
    number_row = int(len(list_text_file))
    file_name_and_number_row_text = (name_file, number_row, list_text_file)
    return file_name_and_number_row_text


# Отсортировать кортедж файлов по возврастанию кол-ва строк текста в файле
def sorted_name_files_ascending_rows(name_files):
    list_file_row = []

    for file in files:
        file_name_and_number_row_text = get_turtle_info_file(name_files)
        list_file_row.append(file_name_and_number_row_text)

    sorted_file_text = sorted(list_file_row, key = lambda x: x[1])
    return sorted_file_text


# Получить общий список для записи в файл
def get_general_list_of_lines_to_write(files):
    list_txt_new = []

    list_turtle_files = sorted_name_files_ascending_rows(files)

    for list_txt in list_turtle_files:
        list_txt_new.append(list_txt[0])
        list_txt_new.append(list_txt[1])
        list_txt_new.extend(list_txt[2])
    return list_txt_new


#Запись в файл
def write_text_outfile(files, outfile):
    if os.path.isfile(outfile):
        f = clear_existing_file(outfile)

    lines = get_general_list_of_lines_to_write(files)

    for line in lines:
        str = f"{line}\n"
        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str)


if __name__ == "__main__":
    # Получить путь к директории проекта
    directory = Path(__file__).resolve().parents[0]

    # Получаем список txt файлов
    list_files = get_list_txt_files(directory)

    #Выполнить запись в файл согласно условию задачи 3
    write_text_outfile(list_files, "outfile.txt")


