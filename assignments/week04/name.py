#รับข้อมูล "ชื่อจริง (ภาษาอังกฤษ)" จากผู้ใช้
#นับจำนวนสระในข้อความดังกล่าว

name = "Warunyuporn"
letters = list(name)
print(letters)
number = 0
for char in letters:
    if char =='a' or char == 'A':
        number = number + 1

    if char =='e' or char == 'E':
        number = number + 1

    if char =='i' or char == 'I':
        number = number + 1

    if char =='o' or char == 'O':
        number = number + 1

    if char =='U' or char == 'U':
         number = number + 1

print("You have", number ,"vowels in your text.")