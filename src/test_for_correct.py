from datetime import datetime

import openpyxl


#book = openpyxl.Workbook()
book = openpyxl.open('ТОВАРЫ_ВАШЕГО_ПОСТАВЩИКА_выбранные.xlsx', read_only=True)
sheets = book.sheetnames
sheet = book[sheets[0]]

#print(sheet['B2':'C4'])
print(sheet.max_row)
print('\n')
print(sheet.max_column)
# for line in range():


book.close()
# data_set = set()

# with open("unique_data.txt", "r", encoding="UTF-8") as f:
    
    # for line in f.readlines():
        # if line == "\n":
            # continue
        # else:
            # line_list = line.split(' || ')
            # data_set.add(line)
      
      
# data_list = list(data_set)
    
    
# with open("unique_data_selected.txt", "a", encoding="UTF-8") as f:
        
    # for line1 in data_list:
        # if line2 in line1:
            # f.write(line1)
            # del articles_list[articles_list.index(line2)]
            # print(len(articles_list))
        # else:
            # print(len(articles_list))