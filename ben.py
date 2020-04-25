def control_digit(id):
    s = 0
    for i in range(8):
        digit = int(id[i])
        digit1 = digit * 2 
        if digit1 > 10:
            digit1 = (digit1 % 10) + 1
        else:
            digit1 = digit1
        if i % 2 == 1:
            s = s + digit1
        i = i + 1
    m = 10 - (s % 10)
    return m
print(control_digit(21322307))
