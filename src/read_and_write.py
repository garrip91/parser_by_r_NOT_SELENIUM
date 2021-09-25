with open('vot.txt', 'r', encoding='UTF-8') as source:
    #print(source.readlines())
    
    with open('result.txt', 'w', encoding='UTF-8') as target:
        for line in source:
            target.write(line)
            #print(line)