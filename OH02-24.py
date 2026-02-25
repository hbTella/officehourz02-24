print("Hello World!")

age = 25
year = 2026

# operators(+,-,*,/,%,**)
#Addition
print(age+5)
#Subtraction
print(age-5)
#Multiplication
print(age*3)
#Division
print(age/4)
#reminder
print(age%4)
#power
print(age**2)

#String - single quotes or double quotes, its the same
name='Hima'
othername="Hima"

sentence = 'This is a sentence'
doulikecheese = "I don't like cheese"

print(name)
print(othername)
print(sentence)
print(doulikecheese)

# Lists
mygradesinschool = ['A','C+','D','B','D-']
mygradesinschool.append("B+")
print(mygradesinschool)
mygradesinschool.append("D-")
print(mygradesinschool)

# Dictionary
student = {
    "name": "abc",
    'age': 20,
    'favoriteActivity': "Jaming to sick beats",
    "FavoriteSoda": "Coke",
    "Grades": ["A+","A+","A+"]
}

print(student)
print(student["favoriteActivity"])
print(student["FavoriteSoda"])

# for loops
for eachElement in range(1, 11): print(eachElement)
# shorthand for loop
for i in range(1, 11): print(i)

for eachGrade in mygradesinschool: print(eachGrade)
for i in mygradesinschool: print(i)

# for eachElement in range(1, 21):
#     if eachElement % 2 == 0:
#         print(eachElement)

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

numbers = [1, 56, 85, 32, 0]

total = 0
for num in numbers:
    total += num
    print("The total sum of numbers is:", total)

total = 0
for num in numbers:
    total += num
print("The total sum of numbers is:", total)    

for i in range(5, 0, -1):
    print(i)    


names = ["Colton","Qasmi","Mesganaw","vasantha","Selam","Hima","Monika","Yamrot","Lucky"]

for name in names:
    if len(name) > 6:
     print(name)

for num in numbers:
    if num % 2 ==0:
        print(num, "is even")
    else:
        print(num,"is odd")


         

 