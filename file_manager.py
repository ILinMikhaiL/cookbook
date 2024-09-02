import os.path

def read_info_file(filename):
    file = open(filename, encoding='utf-8')
    lines = file.read().splitlines()
    print(lines)
    #lines = lines.rstrip('\n')
    return lines
    file.close()

def write_info_file(file_name, lines):
    if os.path.isfile(file_name):
        with open(file_name, 'w') as f:
            f.write('')

    for line in lines:
        str = f"{line}\n"
        with open(file_name, 'a', encoding="utf-8") as f:
            f.write(str)
    f.close()

def compare_files_and_write_file(file_1, file_2, out_file):
    list =[]
    info_file_1 = read_info_file(file_1)
    info_file_2 = read_info_file(file_2)
    if (len(info_file_1) < len(info_file_2)) or (len(info_file_1) == len(info_file_2)):
        list.append(file_1)
        list.append(len(info_file_1))
        list.extend(info_file_1)
        list.append(file_2)
        list.append(len(info_file_2))
        list.extend(info_file_2)
    else:
        list.append(file_2)
        list.append(len(info_file_2))
        list.extend(info_file_2)
        list.append(file_1)
        list.append(len(info_file_1))
        list.extend(info_file_1)
    write_info_file(out_file, list)

compare_files_and_write_file('1.txt','2.txt','3.txt')


