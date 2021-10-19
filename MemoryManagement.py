class _:
    pass

from random import randint
def print(*args):
    pass


class Memory:
    count = 0
    def __init__(s,*args):
        Memory.count += 2
        s.i = 0
        s.name = Memory.count #Only for debug
        s.index = []
        # s.mem = {}  # dict for now
        s.scope = {}
        s.temporary = {}
        s.instances = {0:{}}

    def initInstance(s,i):
        s.i = i
        s.instances[i] = {}



    def overwrite(s, var, item):
        print(f'\nOverwrite<{s.name, s.instances[s.i]}>\n')

        s.instances[s.i][var] = item

    def all(s,i=_):
        if i == _:
            return str(f'----Memory<{[f"({str(v)}:{str(x)})" for v,x in zip(s.instances.keys(),s.instances.values())]}>')
        return f'Memory<{s.instances[i]}>'

    def getFromId(s,var,i):
        return s.instances[i][var]

    def get(s,var):
        # if s.mem.__contains__(var):
        #     print(s.name,'name',s.all(),'++++',s.i,'+++++++++++++++++++++++++---x')
            return 4#s.instances[s.i][var]
        # return s.scope[var]
    def has(s,val):
        # print(s.name,'name','Has',s.all(), '++++', s.i, '+++++++++++++++++++++++++---x')
        return val in s.instances[s.i]

    def using(s,mem):
        # This will be massively inefficient
        # copying each element in memory
        # print(mem.mem,"---------------------------")

        s.instances[s.i].update(mem.mem.items())
        return s


    def temp(s):
        return s.temporary

    def writeTemp(s,val,Module):
        s.temporary[val] = Module



class Instance:
    def __init__(s,memory,i):
        s.mem = memory
        s.i = i