lst = [[1,2,3],[2,4,3],[5,2,1],[1,2,7]]
prefix = [1, 2]
newlst = filter(lambda s: s[0] == prefix[0] and s[1] == prefix[1], lst)