VALID_DIGITS = {
    'one':1, 
    'two':2, 
    'three':3, 
    'four':4, 
    'five':5,
    'six':6, 
    'seven':7, 
    'eight':8, 
    'nine':9
    }

def parseLine(line: str) -> int:
    count = 0
    l = list(line)
    tbuff = ''
    dbuff = []
    while count < len(line):
        c = l[count]
        
        if c.isdigit():
            dbuff.append(c)
            count += 1
            tbuff = ''
            continue
        
        tbuff += c
        
        for i in VALID_DIGITS.keys():
            if i in tbuff:
                dbuff.append(str(VALID_DIGITS[i]))
                tbuff = ''
                break
        
        count += 1

    val = int((dbuff[0] + dbuff[-1]))

    return val



with open("input.txt") as efile:
    text = efile.read().split('\n')
    total = 0
    for line in text:
       total += parseLine(line)
    print(total)

