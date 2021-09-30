import pandas as pd
import numpy as np

file ='data.txt'
file2 = 'data_result.txt'

uniqlines = set(open(file,'r', encoding='utf-8').readlines())
prefix = ["11-2113"]
newlst = filter(lambda s: s[0] == prefix[0] and s[1] == prefix[1], uniqlines)
print(newlst)