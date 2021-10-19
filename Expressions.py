from ExcecClasses.Literal import CollectionExp,ListCollectionExp,Void
from GrammerUtils import *
from MemoryManagement import Instance
# def print(*args):
#     pass
from time import time

# print(symbols,'sss--+')
#
# def pr(x,v='pr'):
#     print(x,v)
#     return x
#
# def pri(x,v='pr------------------------'):
#     print(x,v)
#     return x

class Idle:
    def __init__(s,a,memory):
        a = Variable(a,memory)
        s.a = a.call
        s.solve = lambda:s.a()


class Operation:
    def oCall(s):
        obj = s.a()
        # print(obj.i,'--cx-+',obj.mem.all())

        s.bval.setMem(obj.mem)
        f = obj.mem
        obj.mem.i = obj.i

        result = s.bval.solve()
        obj.mem.i = f


        obj.mem.i = f
        return result

    def vcall(s):
        v = s.a()
        return v.mem.getFromId(s.bval, v.i)


    def __init__(s, a, oper, b,memory):
        s.aval = a
        s.bval = b


        a = Variable(a,memory)
        b = Variable(b,memory)
        s.a = a.call
        s.b = b.call


        # if not oper == '.':
        #
        # else:
        #     pass

        if oper == '.':
            if isinstance(s.bval,(FunctionCall,ObjectCall)):
                s.solve = lambda:s.oCall()
            else:
                s.solve = lambda:s.vcall()
        elif oper == '-':
            s.solve = lambda: s.a() - s.b()
        elif oper == '+':
            # print(s.call(),ss.a(
            s.solve = lambda: s.a() + s.b()
        elif oper == '*':
            s.solve = lambda: s.a() * s.b()
        elif oper == '/':
            s.solve = lambda: s.a() / s.b()
        elif oper == '**':
            s.solve = lambda: s.a() ** s.b()
        elif oper == '//':
            s.solve = lambda: s.a() // s.b()
        elif oper == '==':
            s.solve = lambda: s.a() == s.b()
        elif oper == '!=':
            s.solve = lambda: s.a() != s.b()
        elif oper == '&&':
            s.solve = lambda: s.a() and s.b()
        elif oper == '||':
            s.solve = lambda: s.a() or s.b()
        elif oper == '%':
            s.solve = lambda: s.a() % s.b()
        elif oper == '^':
            s.solve = lambda: s.a() ^ s.b()
        elif oper == '<':
            s.solve = lambda: s.a() < s.b()
        elif oper == '>':
            s.solve = lambda: s.a() > s.b()
        elif oper == '>=':
            s.solve = lambda: s.a() >= s.b()
        elif oper == '<=':
            s.solve = lambda: s.a() <= s.b()
        elif oper == '@=':
            s.solve = lambda: s.a() in s.b()
        else:
            print('invalid operation -',oper)
            assert False

def none(*a):
    pass

class FunctionCall:
    def __init__(s,name,args,memory):
        s.mem = memory
        s.defualt = memory
        s.name = name
        s.args = args
        print(args)

    def setMem(s,val):
         s.mem = val


    def solve(s): ################################################

        # assert False
        # if isinstance(s.mem,(tuple,list)):
        #     memory = bothScopesCall(s.mem, s.name)# turpleMem((Memory(),)).get(s.name)
        # # else:
        # #     memory = s.mem.getFromId(s.name,s.mem.i)
        # from ExcecClasses.include import VirtualBlocks
        # from time import time
        # memory = {'mem':{},'args':[],'function':VirtualBlocks(time)}
        # function = memory['function']
        # fargs = memory['args']
        # vm = memory['mem']
        #
        # # vm.rehash()
        # ansArgs = s.args.solve()
        #
        # if not type(ansArgs) == list:
        #     ansArgs = [ansArgs]
        #
        #
        # for iArg,oArg in zip(ansArgs,fargs):
        #     vm.overwrite(oArg, iArg) # This Overides arguments
        #
        # for line in function:
        #     x = line.run()
        #     if x is not None:
        #         s.mem = s.defualt
        #         return x
        #
        # s.mem = s.defualt
        return time()

class ObjectCall(FunctionCall):
    count = 2


    def solve(s):
        ObjectCall.count += 1
        i = ObjectCall.count

        memory = bothScopesCall(s.mem, s.name)  # turpleMem((Memory(),)).get(s.name)
        vm = memory['mem']

        vm.initInstance(i)
        print(i,'id')
        vm.id = i

        # s.id = ObjectCall.count
        # vm.rehash()
        ansArgs = s.args.solve()
        fargs = memory['args']


        if not type(ansArgs) == list:
            ansArgs = [ansArgs]

        for iArg, oArg in zip(ansArgs, fargs):
            vm.overwrite(oArg, iArg)  # This Overides arguments
            print(vm.all(i))

        for line in memory['function']:
            print(vm.all(i), 'ccc')
            x = line.run()
            if x is not None:
                vm.i = 0
                assert InitReturnError


        vm.i = 0

        return Instance(vm,i)




    ##############################################################

class Expression:
    def __init__(self, source,memory,**kwargs):



        if source[0] == '*':
            source = source[1:]
            self.type = 'star'
        else:
            self.type = 'var'

        print(memory, 'ssmemory')

        if not kwargs.__contains__('NoneCallable'):
            kwargs['NoneCallable'] = False
        self.NoneCallable = kwargs['NoneCallable']
        # print(source, "++----------------------------------------------+")
        operation = source
        par = operation[:]
        start = 0

        # This solves for parenthesis and [,(

        while ')' in operation or ']' in operation:

            stop = 0

            if ')' in operation:
                stop = operation.index(')')
                par = operation[:stop]
                start = rindex(par[:], '(') + 1
                par = par[start:]

            if ']' in par:
                stop = par.index(']')+start

                par = par[:par.index(']')]
                start = rindex(par[:], '[') + 1
                par = par[start:]
                start+=len(par)-2

            print(par,'-=---par')

            if operation[start-1] == '[':
                ans = ListCollectionExp([*calculate(par,memory)])

            else:
                ans = CollectionExp([*calculate(par,memory)])
            print(ans, "ans-------")

            # For functions, arrays

            if (start-1)>0 and type(operation[start-2]) == str and anActualVariableName(operation[start-2]) and operation[start-2].isalnum:
                _name = operation[start-2]
                del operation[start-1:stop + 1]

                if isinstance(ans,CollectionExp):
                    if operation[start-3] == '~':
                        operation[start - 2] = ObjectCall(_name, ans, memory)
                        del operation[start-3]

                    else:
                        operation[start-2] = FunctionCall(_name,ans,memory)


            else:
                del operation[start:stop+1]
                operation[start-1] = ans

            print(operation,'operation')




        self.opr = CollectionExp([*calculate(operation,memory)])

        print(self.opr, '33')


    def evaluate(self):
        return self.opr.solve()# if len(val)<2 else val # Removed for speed will cause bugs sooner


    # def vars(self):
    #     return [x for x in self.opr.solve()]



class Variable:
    def __init__(self,var,memory):
        if type(var) == var:
            assert anActualVariableName(var)
        print(memory, "memmm1--")
        memory = memory
        print(memory,"memmm--")



        self.var = var



        typ = type(var)
        print(var,'----var')
        print(type(var))

        if isinstance(var, (Operation,CollectionExp,ListCollectionExp,Expression,FunctionCall)):
            if type(var) == list and len(var) == 1:
                self.call = lambda:self.var.solve()[0]
            else:
                self.call = lambda:self.var.solve()
        else:


            if not typ == str: self.call = lambda:var
            else: # Will always be string from here

                # You will have class issues from here make sure its float Literal only
                if '.' in var:
                    self.num = float(var)
                    self.call = lambda:self.num

                elif var.isdigit():
                    self.num = int(var)
                    self.call = lambda: self.num

                elif var.isalnum and (var[0] != '\'' and var[0] != '"'):
                    self.memory = memory
                    # print(memory,'mm')
                    self.v_name = var # This should be some pointer in c++ conversion
                    # print(var,'varp')
                    if var == 'true':
                        self.call = lambda:True
                    elif var == 'false':
                        self.call = lambda:False
                    elif var == 'void':
                        self.call = lambda:Void
                    else:
                        self.call = lambda:bothScopesCall(self.memory,self.v_name)
                elif var[0] == '\'':
                    self.call = lambda:self.var


                else:
                    assert False


def bothScopesCall(mem,var):
    # print(mem[1].i,'--------i,',mem[1].get(var))
    #
    if mem[1].has(var):
        return mem[1].get(var)
    if mem[2].has(var):
        return mem[2].get(var)
    return mem[0].get(var)



def calculate(literal: list,memory):


    literal = split(literal, ',')

    print(literal, 'litr')
    # print(literal,"llll")
    for operation in literal:
        oprs = []
        for c in operation:
            if c in operators: oprs.append(operators.index(c))

        if len(oprs)>0:
            oprs.sort()
            oprs = oprs[::-1]
            if len(oprs) == 0:
                yield operation
                continue

            while len(oprs) > 0:
                pos = operation.index(operators[oprs[0]])


                oper = operation[pos] # Might need to work on this for speed

                # This allows for -6,-2,etc

                if (oper == '-' or oper == '+') and pos==0:
                    oper, b = operation[pos:pos + 2]
                    a = 0

                else:
                    print(operation[pos - 1:pos + 2],'----22')
                    a, oper, b = operation[pos - 1:pos + 2]

                    # I added it hear for out of bound errors
                    operation.pop(pos - 1)

                ans = Operation(a, oper, b, memory)
                # -----------------------------------------------

                operation.pop(pos - 1)
                operation.pop(pos - 1)

                operation.insert(pos - 1, ans)
                del oprs[0]

            yield operation[0]
            continue

        else:
            print(operation,'42')
            yield Idle(operation[0] if len(operation)>0 else
                       operation
                       ,memory)
            continue


