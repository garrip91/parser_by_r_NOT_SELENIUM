from collections import Counter


########### ОТКРЫВАЕМ ИСХОДНЫЙ ФАЙЛ С ДАННЫМИ НА ЧТЕНИЕ: ###########
# with open('data_for_check.txt', 'r', encoding='UTF-8') as source:
with open('data.txt', 'r', encoding='UTF-8') as source:
    #print(source.readlines())
############################### 2.- ###############################

    ######## ЦИКЛОМ СЧИТАЕМ КОДЫ ТОВАРОВ: ########
    articles = []
    for line in source:
        line = line.split(' || ')
        articles.append(line[2])
    ##############################################
    
    #print(articles)
    print([F'{item, count}' for item, count in Counter(articles).items() if count > 1])
