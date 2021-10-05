def main():
    # Множество для сохранения результатов
    result = set()

    # Открываем файл с названиями
    with open("unique_titles.txt", "r", encoding="UTF-8") as file:
        # Собираем названия в множество
        titles = {line.strip() for line in file.readlines()}

    # Открываем файл с данными по товарам
    with open("unique_data.txt", "r", encoding="UTF-8") as file:
        # Проходим по всем строкам
        for line in file.readlines():
            # Берем название из строки
            title = line.split(" || ")[1]
            # Если название в множестве с названиями
            if title in titles:
                # Добавляем строку к результату
                result.add(line)

    # Открываем файл, куда запишем результаты
    with open("unique_results.txt", "w", encoding="UTF-8") as file:
        # Проходимся по каждой отобранной строке
        for line in result:
            # Записываем строку
            file.write(line)


if __name__ == '__main__':
    main()
