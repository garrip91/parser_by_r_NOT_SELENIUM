import csv

with open('unique_titles.txt', 'r', encoding='UTF-8') as f:
    titles = set(line.strip() for line in f)

with open('unique_data.txt', 'r', encoding='UTF-8') as fin:
    with open('unique_data.txt', 'r', encoding='UTF-8') as fout:
        reader = csv.reader(fin, delimiter="||")
        writer = csv.writer(fout)
        for data in reader:
            if data[1] in titles:
                writer.writerow(data)