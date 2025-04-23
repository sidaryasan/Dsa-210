import os
from collections import defaultdict

def extract_type(line):
    start = line.find('type="')
    if start == -1:
        return ""
    start += len('type="')
    end = line.find('"', start)
    if end == -1:
        return ""
    return line[start:end]

def split_by_category(input_file):
    if not os.path.exists(input_file):
        print("Girdi dosyası bulunamadı!")
        return

    file_handles = defaultdict(lambda: None)

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            type_name = extract_type(line)
            if not type_name:
                continue

            file_name = f"{type_name}.txt"
            if file_handles[type_name] is None:
                file_handles[type_name] = open(file_name, 'w', encoding='utf-8')
            file_handles[type_name].write(line)

    for f in file_handles.values():
        if f:
            f.close()

    print("Tüm kayıtlar kategorilere göre ayrıldı.")

# Kullanım
split_by_category("filtered_by_date.txt")
