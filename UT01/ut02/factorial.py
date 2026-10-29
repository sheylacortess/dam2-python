def factorial(num):
    acc = 1
    while num > 1:
        #print(num)
        acc = acc * num
        num = num - 1
    print(acc) 

factorial(4) # Resultado: 24