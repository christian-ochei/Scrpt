
import sys
from Prepare import run
Debug = False

if not Debug:
    args = sys.argv
    if len(args) == 1:
        print('Scrpt Engine <Build 1.0>\n')
    else:
        file = sys.argv[1]
        with open(file) as file:
            run(file.read())
else:
    file = 'Factorial_Demo.srp'
    with open(file) as file:
        run(file.read())





# import os
#scrpt Factorial_Demo.srp
# os.system('python C:\\Users\\12145\\PycharmProjects\\Experi\\main.py')
