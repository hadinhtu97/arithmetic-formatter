import re


def arithmetic_arranger(problems, option=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for p in problems:
        if(re.search('\\*', p) or re.search('/', p)):
            return "Error: Operator must be '+' or '-'."
        if(re.search('[a-zA-Z]', p)):
            return 'Error: Numbers must only contain digits.'
    pass
