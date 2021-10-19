from Tokenizer import tokenize
from Squishify import squishify
from Expressions import Expression
from time import time, sleep
from MemoryManagement import Memory
from Compound_Statement import Compound
from ExcecClasses.Assign import *
from Exception import *
from GrammerUtils import *
from ExcecClasses.include import Include
from ExcecClasses.Literal import CodeLiteral
#
# def print(*a):
#     pass


def run(txt):
    public = Memory()
    # public.overwrite('h', 50)

    # In c convartion, Memory should be pointers

    txt = squishify(txt).split(';')

    _1st_Stage_Compiled = prepare(txt,[public,Memory(),Memory()])
    #print(_1st_Stage_Compiled)
    _1st_Stage_Compiled.run()
    #print(public,'++++++')


def prepare(txt,bothScopes,start=0,stop=None,header='main'):
    if stop is None: stop = len(txt)
    x = start
    Lines = []
    FunctionScope = header[1] == '(' # and header not in registered, while,if when

    # global_= bothScopes
    # private = Memory()

    # bothScopes[2] = bothScopes[0] # outer = global
    global_,private,outer = bothScopes
    bothScopes = [global_,private,outer]

    bothScopes[2] = bothScopes[1]


    if not header[0] in bothScopes[1].temp().keys():
        if FunctionScope:
            bothScopes[1] = Memory()
            FunctionScope = True

            # bothScopes = [global_, private,outer]

        while x < stop:
            line = tokenize(txt[x])

            # For each line in Statement
            if is_compound(line):

                end = index(txt[x:]) + 1

                # Dont Compile if A module owns the header


                compound = prepare(txt,bothScopes,start=x+1,stop=end+x,header=line[:len(line)-3])
                Lines.append(compound)



                x += end - 1

            elif is_setter(line):
                #print(line,"313")
                variator = line.index('=')


                # writeRead = private if FunctionScope else global_
                #print(line[variator + 1:len(line) - 1],'---ss')
                exp = Expression(line[variator + 1:len(line) - 1],bothScopes)
                assign = Assign(line[:variator], exp, bothScopes)

                # #print(Expression(line[variator + 1:len(line) - 1],memory).evaluate())
                Lines.append(assign)

            elif line[0] == 'return' or line[0] == 'yield':
                # _return = line[2:]
                # #print(_return,'return')
                append = defaulter(line,'void')

                Lines.append(Assign('return',Expression(append,bothScopes),bothScopes))

            elif line[0] == 'print':

                append = defaulter(line,'"\n"')

                #print(append,'append')

                Lines.append(Print(Expression(append, bothScopes)))

            elif line[0] == 'new':

                append = defaulter(line,'void')

                Lines.append(Include(append,bothScopes))

            elif line[0] == '~':

                if line[1] == 'outer':

                    bothScopes[1] = bothScopes[2]
                    bothScopes[0] = bothScopes[2]


                elif line[1] == 'global':
                    private = global_
                    outer = global_
                    bothScopes[1] = global_
                    bothScopes[2] = global_
                elif line[1] == 'private':
                    global_ = private
                    outer = private
                    bothScopes[0] = private
                    bothScopes[2] = global_
                else:
                    assert ObjectCallMustBeAssigned






            else:

                if line[0] != '}' and line[0] != ' '  and line[0] != '...' and line[0] != 'ignore' and line[0] != 'pass':
                    print(line, 'line error')

                    # append = defaulter(line, 'void')

                    Lines.append(Assign('', Expression(line, bothScopes), bothScopes))
            x += 1
    else:
        return CodeLiteral(txt[start:stop],header)
        # Lines.append(CodeLiteral(txt[start:stop]))

                    # #print(line,'line')
                    # assert False


    return Compound(Lines, header, memory=bothScopes)


