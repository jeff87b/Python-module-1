import random
minimum = int(input("Enter the lower range"))
maximum = int(input("Enter å higher range"))

name = "Hans"
print(len(name))

random1 = (random.randint(minimum,maximum))
print (random1)
if (len(name)>random1):
    print('wow')
else:
    print("Annet svar")
