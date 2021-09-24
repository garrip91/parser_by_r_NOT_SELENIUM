import csv


with open('vot.txt', 'r', encoding='UTF-8') as f1:
    r = f1.readline()
    #print(r)
    
    with open('result.txt', 'w', encoding='UTF-8') as f2:
        for i in f1:
            f2.write(f1.readline())
            print(i)