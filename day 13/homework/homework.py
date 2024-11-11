#2) for ციკლით მომხარებელს შემოატანინეთ 5 ელემენტი სიაში და დაბეჭდეთ სია

numbers = []

for i in range(5):
    i = int(input("Enter numbers> "))
    numbers.append(i)

print(numbers)




#3) შექმენით ხილების სია, სადაც გექნებათ მინიმუმ 3 ელემენტი. მომხარებელს შემოატანინეთ თავისი საყვარელი ხილი, 
#თუ სიის ბოლო ელემენტის ინდექსი არის ლუწი ჩაამატეთ შემოტანილი ხილი სიაში, სხვა შემთხვევაში არ ჩაამატოთ

fruits = ["apple", "pineaple", "pear", "banana"]

fav_fruit = input("Enter your fav fruit> ")

if (len(fruits) - 1) % 2 == 0:
    fruits.append(fav_fruit)


print(fruits)



#4) შექმენით სია შემდგარი სახელებისგან. მომხარებელს შემოატანინეთ მისი სახელი, თუ მისი სახელი იქნება 5 სიმბოლოს ტოლი ან მეტი.
#ჩაამატეთ სიაში, სხვა შემთხვევაში დაუბეჭდეთ "Name is too short"

name = ["nika", "luka", "danieli", "irakli", "ilia"]

username = input("Enter your name> ")


if len(username) >= 5:
    name.append(username)
else:
    print("Name is too short")

print(name)



#5) შექმენით სია შემდგარი 10 ელემენტისგან. დაპრინტეთ ის და მომხარებელს შემოატანინეთ რიცხვი 1-დან 10-ჩათვლით. 
#შემდეგ წაშალეთ სიის ის ელემენტი რომელი რიცხვიც გადმოგეცათ და დაპრინტეთ განახლებული სია

list = ["elemet1", "elemet2", "elemet3", "elemet4", "elemet5", "elemet6", "elemet7", "elemet8", "elemet9", "elemet10"]

print(list)

user_num = int(input("Enter number 1-10> "))

if 1 <= user_num <= 10:
    list.pop(user_num - 1)
    print(list)
else:
    print("numer is out of range")



#6) კომენტარებით ახსენით რა არის ინდექსი და მოიყვანეთ მაგალითი

#ინდექსი არის სიის, კოლექციის, ლისტის მისამართი თუ რომელ ინდექსეაა შემდეგი ელემენტი, ინდექსის ათვლა იწყება 0-იდან 

# მაგ: list=[giorgi, luka, nika,]   ლუკას ინდექსი არის N2