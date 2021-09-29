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
    
list_for_data_count = []    
with open("data.txt", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        if line == "\n":
            continue
        else:
            list_for_data_count.append(line.split(' || '))
    #print(len(set(list_for_data_count)))
    #print(list_for_data_count)
    
list_for_data_articles_count = []
for i in list_for_data_count:
    list_for_data_articles_count.append(i[2])
print(len(set(list_for_data_articles_count)))