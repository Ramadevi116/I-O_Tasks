input1=input()
input2=[]
for i in input1:
    if i not in input2:
        input2.append(i)
for i in range(len(input2)):
    for j in range(len(input2)):
        if(input2[j]>input2[i]):
           t=input2[i]
           input2[i]=input2[j]
           input2[j]=t
for i in range(0,len(input2)):
    print(input2[i],end="")
    print(input1.count(input2[i]),end="")
