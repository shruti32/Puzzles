from collections import OrderedDict

class DefaultListOrderedDict(OrderedDict):
    def __missing__(self,k):
        self[k] = []
        return self[k]

keys=['blk','pri','ani']
vals1=['blocking','primary','anim']
vals2=['S1','S2']
dic = DefaultListOrderedDict()
for i,key in enumerate(keys):
    dic[key].append(vals1[i])
    dic[key].append(vals2[i])

print (dic)