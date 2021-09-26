c = 0
with open('products.txt', 'r', encoding='UTF-8') as f:
    for line in f.readlines():
        if line == "\n":
            continue
        else:
            c += 1
        
print(c)