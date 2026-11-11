import random


def Button_task(inp, out):
    ABC = ['Q', 'W', 'E', 'R', 'T', 'U', 'Y', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C',
           'V', 'B', 'N', 'M']
    button_input = inp.get()  # Считываем информацию из поля ввода
    #
    first = [button_input[0], button_input[1], button_input[2]]
    second = [button_input[3], button_input[4], button_input[5]]
    random.shuffle(first)
    random.shuffle(second)
    #
    block1 = ''
    block2 = ''
    for i in first:
        block1 += str(i)
    chislo = int(block1)
    block1 += random.choice(ABC) + random.choice(ABC)
    for i in second:
        block2 += str(i)
    chislo += int(block2)
    block2 += random.choice(ABC) + random.choice(ABC)
    block3 = str(chislo)
    while len(block3) <4:
        block3 = '0' + block3
    result = block1 + '-' + block2 + '-' + block3
    out.config(text=result)
