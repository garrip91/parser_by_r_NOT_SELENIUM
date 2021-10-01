file = 'data.txt'
file2 = 'data2.txt'

appended_articles = []  # список, для добавления артиклов
appended_lines = []  # список, для добавления всех строк из файла

with open(r"data.txt", encoding="utf-8") as search:  # открываем файл и читаем его
    for line in search:  # проходимся по каждой строке
        line = line.rstrip()  # убираем отступы справа
        appended_lines.append(line)  # добавляем в список весь поправленный текст
        appended_articles.append(line.split('||')[2])  # добавляем в список только артиклы

sorted_list = sorted(set(appended_articles), key=appended_articles.index)  # убираем совпадения и сортируем по порядку, в артикли были изначально

for srt_list in sorted_list:  # начинаем цикл перебора отсортированных артиклов
    for ap_lines in appended_lines:  # цикл по списку нашего текста
        if srt_list in ap_lines:  # если есть совпадение
            open(file2, 'a', encoding='utf-8').writelines(ap_lines + '\n')  # записываем в файл
            break  # выходим из цикла, тем самым записывая только первое совпадение, остальные отсекаем
