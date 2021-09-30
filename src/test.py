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
    # print(len(set(list_for_products_count)))
        
with open("data_result.txt", "r", encoding="UTF-8") as f:
    
    #list_for_data_count = []
    for line in f.readlines():
        if line == "\n":
            continue
        else:
            #line = line.split(' || ')
            #list_for_data_count.append(line)
            print(line)
    #new_list_for_data_count = []
#    for_in_for = [print(line[2]) for line in list_for_data_count for j in line]
    # for i in list_for_data_count:
        # new_list_for_data_count.append(i[2])
    # #print(len(set(new_list_for_data_count)))