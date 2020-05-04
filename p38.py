def is_pand(n):
    stri = str(n)
    for i in range(len(stri)):
        if stri[i] in stri[:i]+stri[i+1:]:
            return(False)
    return(True)

def concat(n,m):
    return(int(str(n) + str(m)))

''' due to text, we know the number must start with 9
due to 95*2 being 190, that number must start with 91,92,93 or 94
due to 91XX*2 containing 1, it must be 92,93 or 94
'''
largest = 0

for i in range(2,10000):
    base = concat(9,i)
    number = base
    j =2
    new = 0
    while is_pand(new):
        new = concat(number,j*base)
        #print(new)
        if is_pand(new) and '0' not in str(new):
            number=new
        j += 1
    if len(str(number))==9:
        largest = number

print(largest)
