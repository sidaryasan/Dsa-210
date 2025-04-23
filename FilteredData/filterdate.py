def is_date_in_range(line):
    keyword = 'startDate="'
    start = line.find(keyword)
    if start == -1:
        return False

    start += len(keyword)
    date_str = line[start:start + 10]  # "2024-09-01" gibi

    return "2024-09-01" <= date_str <= "2025-04-23"

def filter_by_date(input_filename="output.txt", output_filename="filtered_by_date.txt"):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile, \
             open(output_filename, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if is_date_in_range(line):
                    outfile.write(line)
        print(f"Filtreleme tamamlandı. Çıktı dosyası: {output_filename}")
    except FileNotFoundError:
        print("Dosyalar açılamadı!")

# Kullanım
filter_by_date()
