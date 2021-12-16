def pascal(rows):
    output=[1]
    for i in range(1,rows):
        l=[1]
        if i>=2:
            for x in range(0,i-1):
                l.append(output[i-1][x]+output[i-1][x+1])
        l.append(1)
        output.append(l)
    return output

rows = 4
print(pascal(rows))
     