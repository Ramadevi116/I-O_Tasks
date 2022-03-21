def trailingzeros(input1):
    fac=1
    for i in range(1,input1+1):
        fac=fac*i
    count=0
    length=len(str(fac))
    for i in range(length):
        if(i==0):
            count+=1
    return(count)
n=int(input())
trailingzeros(n)
print(trailingzeros(n))
            
      
