input1 = int(input("Enter a number: "))
min = 0
counter = input1
factor = ""
while(counter >  min):
    if counter != 1:
        factor = factor + str(counter) + "*"
    else:
        factor = factor + str(counter)
    counter = counter - 1
print ("The result", factor)
