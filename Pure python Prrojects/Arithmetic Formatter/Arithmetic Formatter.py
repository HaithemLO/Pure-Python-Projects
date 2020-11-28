def arithmetic_arranger(problems, statprint=False):
    # check problem list
    firstLine = ''
    secondLine = ''
    sumx = ''
    lines = ''
    # maximal problems is 5
    if len(problems) >= 6:
        return 'Error: Too many problems.'
    # split problem to separate components
    for p in problems:
        x,y,z = p.split()

        # check the length of the number, max 4 digits
        if (len(x) > 4 or len(z) > 4):
            return "Error: Numbers cannot be more than four digits."
        

        # check the input as valid digits
        if not x.isnumeric() or not z.isnumeric():
            return "Error: Numbers must only contain digits."

        if (y == '+' or y == '-'):
            if y == "+":
                sums = str(int(x) + int(z))
            else:
                sums = str(int(x) - int(z))
            # set length of sum and top, bottom and line values
            length = max(len(x), len(z)) + 2
            top = str(x).rjust(length)
            bottom = y + str(z).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            # add to the overall string
            if s != problems[-1]:
                firstLine += top + '    '
                secondLine += bottom + '    '
                lines += line + '    '
                sumx += res + '    '
            else:
                firstLine += top
                secondLine += bottom
                lines += line
                sumx += res
        else:
            return "Error: Operator must be '+' or '-'."
    # strip out spaces to the right of the string
    firstLine.rstrip()
    secondLine.rstrip()
    lines.rstrip()
    if statprint:
        sumx.rstrip()
        arranged_problems = firstLine + '\n' + secondLine + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = firstLine + '\n' + secondLine + '\n' + lines
    return arranged_problems

print(arithmetic_arranger(["4422 + 815", "99 + 2", "45 + 43", "123 + 49"]))