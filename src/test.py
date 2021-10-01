from datetime import datetime


data_set = set()
articles_set = set()

with open("data.txt", "r", encoding="UTF-8") as f:
    
    for line in f.readlines():
        if line == "\n":
            continue
        else:
            line_list = line.split(' || ')
            data_set.add(line)    
            articles_set.add(line_list[2])
            
    # print(type(data_set))
    # print(len(data_set))
    # print(type(articles_set))
    # print(len(articles_set))
    

data_list = list(data_set)
articles_list = list(articles_set)

# print(type(data_list))
# print(len(data_list))
print(data_list[0])
# print(type(articles_list))
# print(len(articles_list))
# print(articles_list[0])
    
    
with open("unique_data.txt", "a", encoding="UTF-8") as f:
        
    for line1 in data_list:
        for line2 in articles_list:
            if line2 in line1:
                f.write(line1)
                del articles_list[articles_list.index(line2)]
                print(len(articles_list))
            else:
                print(len(articles_list))
            #f.write(F'{line}\n')
        
    # print(type(articles_list))
    # print(len(articles_list))
        