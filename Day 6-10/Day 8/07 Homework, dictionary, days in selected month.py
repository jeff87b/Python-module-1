dict_1 = {'january': 31, 'february': '28 or 29 (if leap year)', 'march': 31, 'april': 30, 'may': 31, 'june': 30, 'july': 31, 'august': 31, 'september': 30, 'october': 31, 'november': 30, 'december': 31}

chooseMonth = input("Enter month: ")
chooseMonth = chooseMonth.lower()
while True:
    try: print(dict_1[chooseMonth])
    except: print("Example: July")
    chooseMonth = input()
    chooseMonth = chooseMonth.lower()
