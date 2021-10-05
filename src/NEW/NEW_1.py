# with open("unique_data.txt", "r", encoding="UTF-8") as f1:
    
    # data = []
    # result = []
    # for line in f1.readlines():
        # if line == "\n":
            # continue
        # else:
            # data.append(line)
            # with open("unique_titles.txt", "r", encoding="UTF-8") as f2:
                # for i in f2.readlines():
                    # if i == "\n":
                        # continue
                    # else:
                        # if i in line:
                            # #result.append(line)
                            # with open("RESULT.txt", "a", encoding="UTF-8") as f3:
                                # f3.write(F'{line}\n')
            
    # print(data[:5])
    
    
with open('unique_data.txt', 'r', encoding='UTF-8') as f:
    #data = f.read().split("\n").strip()
    #data = f.read().split("\n")
    data = [line.strip() for line in f.readlines()]
    print(data[:5])
    print(type(data))

with open('unique_titles.txt', 'r', encoding='UTF-8') as f:
    #titles = f.read().split("\n").strip()
    #titles = f.read().split("\n")
    titles = [line.strip() for line in f.readlines()]

result = []
for title in titles:
    for row in data:
        if title in row:
            result.append(row)

with open('RESULT.txt', 'w', encoding='UTF-8') as f:
    f.writelines(result)
    
    
    
    
    
    
    #print(result)
      
    
    
# with open("unique_data.txt", "a", encoding="UTF-8") as f:
        
    # for line1 in data_list:
        # for line2 in articles_list:
            # if line2 in line1:
                # f.write(line1)
                # del articles_list[articles_list.index(line2)]
                # print(len(articles_list))
            # else:
                # print(len(articles_list))