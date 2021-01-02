import re

def arithmetic_arranger(problems, option=False):
    firstLine = str()
    secondLine = str()
    thirdLine = str()
    fourthLine = str()
    spaceBetween = '    '

    if len(problems) > 5:
        return 'Error: Too many problems.'
    for p in problems:
        if re.search('\\*', p) or re.search('/', p):
            return "Error: Operator must be '+' or '-'."
        if re.search('[a-zA-Z]', p):
            return 'Error: Numbers must only contain digits.'

        firstOperand = re.findall('\\d+', p)[0]
        secondOperand = re.findall('\\d+', p)[1]
        operator = re.findall('\\+|-', p)[0]
        result = str(int(firstOperand) + int(secondOperand) if operator == '+' else int(
            firstOperand) - int(secondOperand))

        if len(firstOperand) > 4 or len(secondOperand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if len(firstOperand) >= len(secondOperand):
            length = len(firstOperand) + 2
        else:
            length = len(secondOperand) + 2
        spaceFirstLine = length - len(firstOperand)
        spaceSecondLine = length - 2 - len(secondOperand)
        spaceFourthLine = length - len(result)

        # first line represent first operand
        for n in range(spaceFirstLine):
            firstLine += ' '
        firstLine += firstOperand

        # second line represent operator and second operand
        secondLine += operator
        secondLine += ' '
        for n in range(spaceSecondLine):
            secondLine += ' '
        secondLine += secondOperand

        # third line represend string '--' equal to length of each problem
        for n in range(length):
            thirdLine += '-'

        # fourth line represend the result of each problem
        for n in range(spaceFourthLine):
            fourthLine += ' '
        fourthLine += result

        # add space between problem (when it not the last problem)
        if (problems.index(p) != len(problems) - 1):
            firstLine += spaceBetween
            secondLine += spaceBetween
            thirdLine += spaceBetween
            fourthLine += spaceBetween

    # config the returnstring depend option
    if option:
        returnString = firstLine + '\n' + secondLine + '\n' + thirdLine + '\n'+fourthLine
    else:
        returnString = firstLine + '\n' + secondLine + '\n' + thirdLine
        
    return returnString
