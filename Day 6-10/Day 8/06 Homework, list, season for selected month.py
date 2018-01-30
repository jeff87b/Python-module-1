seasonList = [["January", "February", "December"], ["March", "April", "May"], ["June", "July", "August"], ["September", "October", "November"]]


chooseMonth = input("Enter month: ")
for months in seasonList[0]:
    if months == chooseMonth:
        print("Winter")
for months in seasonList[1]:
    if months == chooseMonth:
        print("Spring")
for months in seasonList[2]:
    if months == chooseMonth:
        print("Summer")
for months in seasonList[3]:
    if months == chooseMonth:
        print("Autumn")

