from MemoryManagement import Memory

class VirtualBlocks:
    def __init__(s,block,args,mem):
        s.block = block
        s.args = args
        s.mem    = mem

    def run(s):
        return s.block(*s.args)

class Include:
    def __init__(s,header,mem):
        s.global_, s.memory,s.outer = mem
        s.type = Include
        include = header[0]
        s.vm = Memory()

        if include == 'time':
            from time import time
            s.module = {'function':[VirtualBlocks(time,(),s.vm)],'args':[''],'mem':s.vm}
            s.run = lambda:s.global_.overwrite('time',s.module)

        elif include == 'Python':
            s.global_.writeTemp('Python',None)
            s.run = lambda:None

        elif include == 'JavaScript':
            s.global_.writeTemp('JavaScript',None)
            s.run = lambda:None