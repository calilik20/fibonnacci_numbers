a = 1
b = 1

fibonnacci= [a,b]

for i in range(10):
    print("a:",a,"b:",b)

    a,b=b,a+b

    fibonnacci.append(b)

print((fibonnacci))