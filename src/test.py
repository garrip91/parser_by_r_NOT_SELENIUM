import json


# with open("products.json", "r", encoding="UTF-8") as output:
    # data = json.load(output)
    # print(len(data))    
    
# list_for_products_count = []    
# with open("products.txt", "r", encoding="UTF-8") as f:
    # for line in f.readlines():
        # if line == "\n":
            # continue
        # else:
            # line = line.replace('\n', '')
            # list_for_products_count.append(line)
    #print(len(list_for_products_count))
        
with open("data.txt", "r", encoding="UTF-8") as f:
    list_for_data_count = []
    for line in f.readlines():
        if line == "\n":
            continue
        else:
            line = line.split(' || ')
            line = tuple(line)
            list_for_data_count.append(line)
    list_for_data_count = set(list_for_data_count)
    list_for_data_count = list(list_for_data_count)
    print(list_for_data_count[0])

    list_for_data_articles_count = []
    for i in list_for_data_count:
        list_for_data_articles_count.append(i[2])
    list_for_data_articles_count = set(list_for_data_articles_count)
    list_for_data_articles_count = list(list_for_data_articles_count)
    #print(list(list_for_data_articles_count)[0])
    
    list_for_NEW_data_count = [[None, None, None, None, None]]
    for i in list_for_data_count:
        if i[2] in list_for_data_articles_count:
            if list_for_NEW_data_count[-1][2] != i[2]:
                list_for_NEW_data_count.append(i)
    print(len(list_for_NEW_data_count))