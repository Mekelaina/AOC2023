

with open("input.txt") as efile:
    text = efile.read().split('\n')
    total = 0
    for line in text:
        buff = []
        for char in line:
            if char.isdigit():
                buff.append(char)
        val = buff[0] + buff[-1]
        total += int(val)
    print(total)