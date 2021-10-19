from Expressions import Expression
from Exception import *
from GrammerUtils import *

# def pr(*args):
#
#     print(args,'--------------13')
#     return args[0]

# def print(*a):
#     pass

class Compound:
    def __init__(s, block, head, memory):
        s.memory = memory
        s.block = block
        s.type = 'compound'
        s.returnIndex = len(block)

        for x,line in enumerate(block):
            if line.type == 'return':
                s.returnIndex = x+1
                break

        s.block = s.block[:s.returnIndex]

        if head == 'main':
            s.run = lambda: [line.run() for line in s.block]

        elif head[0] == 'if':
            exp = Expression(head[2:],memory)


            ###########################################################

            s.run = lambda:[line.run() for line in s.block][0] if exp.evaluate() \
                else None


            ###########################################################
        elif head[0] == 'else':

            # exp =

            s.run = lambda: [line.run() for line in s.block][0] if exp.evaluate() \
                else None

        elif head[0] == 'Python':
            s.run = lambda:print('blk\n\n\n',block,'----')



        elif head[0] == 'while':
            # assert Falsemmmmmmm
            val = Expression(defaulter(head,'void'),memory)

            ...

            s.run = lambda: whileloop(s.block,val)

            ...

        elif head[0] == 'for':
            val = Expression(head[2:], memory)

            ...

            def liner():
                for x in range(val.evaluate()):
                    pass
                    # import dis
                    # dis.dis(line.run)
                    for line in s.block:


                        line.run()


            s.run = lambda:liner()

            ...

        # If function this must be the last

        elif head[1] == '(': # Fis it later # Functions
            args = head[head.index('(')+1:rindex(head,')')]
            print(args,'++++++++++++===')
            # args = Expression(args,memory,NonCallable=True)

            s.args = [x[0] if len(x)>0 else '' for x in split(args,',')]


            # s.memory = memory[1]
            s.mem = memory[2] # Double bounding is the way to fix this

            theFunction = head[0], {'function': block, 'args':s.args ,'mem':memory[1]}

            s.run = lambda:none(s.mem.overwrite(*theFunction),memory[1].overwrite(*theFunction))


        else:
            print('Not Defined',head)

            assert Fals
def pr(*args):
    print(*args,'cccc---------')
    return args[0]
def none(*args):
    pass

def whileloop(block,exp):
    while exp.evaluate():
        for line in block:
            line.run()