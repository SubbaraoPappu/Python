n=5
cmbl="*"
for i in range (1,n):
    pstr=''
    for j in range(1,n):
        pstr=pstr+cmbl
    print (pstr)

n=5
for i in range (1,n):
    for j in range(1,n):
        print("*",end="")
    print()