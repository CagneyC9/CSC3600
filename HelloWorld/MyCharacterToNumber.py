# For this program, I just want a to be 1 b to be 2 and so forth.
# From that point I will be able to move it up and down this range
# My end goal is that it works and if it works well then I can start to implement
# keeping it between 1 and 26 always
import string
bool = False
badSub = False
# Funny = 0
Change = int(input("Put a substitution value: "))
if Change < 0 or Change > 26:
    badSub = True

dict = {}
user_string = input("Put a string here: ")
String_Num = ""
Decoder = ""

for i, char in enumerate(string.ascii_lowercase):
    dict[i] = char
    # Our Dictionary

for val in user_string.lower():
    # if badSub:
    #     break
    if val.isdigit() or badSub:
        if val.isdigit():
            bool = True
            break
        elif badSub:
            break
    for key, value in dict.items():
        if val == value:
            PreviousValue = str(key + 1 + Change)
            FixedValue = int(PreviousValue)
            if FixedValue > 26:
                while FixedValue > 26:
                    FixedValue = FixedValue - 26
            elif FixedValue < 0:
                while FixedValue < 0:
                    FixedValue = FixedValue + 26

            # Funny += FixedValue
            Decoder += dict[FixedValue - 1]
            Decoder += " "
            String_Num += str(FixedValue)
        # For spaces
            String_Num += " "
if badSub:
    print("Your Substitution value should be a value between 0-26")
if bool:
    print("Your Substitution has numbers in it")
else:
    if not bool:
        print(Decoder)
        print(String_Num)
# print("Numerical Value of Name", str(Funny))
