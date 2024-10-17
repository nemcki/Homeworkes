#2)კომენტარებით ახსენით რა არის კონკადინაცია და მოიყვანეთ მაგალითები
#კონკადინაცია არის 2 სტრინგის მიმატება ანუ 2 სიტყვის გადაბმა 
#მაგალითად ერთერთი კონკადინაციის მაგალითია 
#print("giorgi"+"iadze")

#3)მომხარებელს შემოატანინეთ რიცხვი ერთიდან შვიდამდე, შემოტანილი რიცხვის მიხედვით დაპრინტეთ კვირის დღე.(მაგალითად მომხარებელმა შემოიტანა 4 >>> "Thursday")
num1=input("enter a number 1, 2, 3, 4, 5, 6, 7,:")
if num1 == "1":
    print("Monday")
elif num1 == "2":
    print("Tuesday")
elif num1 == "3":
    print("Wednesday")
elif num1 == "4":
    print("Thursday")
elif num1 == "5":
    print("Friday")
elif num1 == "6":
    print("Saturday")
elif num1 == "7":
    print("Sunday")
else:
    print("invalid operator")

#4)მომხარებელს შემოატანინეთ ორი რიცხვი, შეინახეთ ორივე ცვლადში. მოახდინეთ მათ შორის შედარება და შედეგი(True or False) გამოიტანეთ ტერმინალში
num1=int(input("enter number1:"))
num2=int(input("enter number2:"))
print(num1>=num2)

#5)მომხარებელს შემოატანინეთ თავისი ასაკი, თუ ის არის 18 წლის ან ზემოთ დაპრინტეთ "You are adult", სხვა შემთხვევაში დაპრინტეთ "You are kid"
age=int(input("enter your age: "))
if age > 18 :
    print("You are adult ")
elif age < 18 :
    print("you are kid ")
else:
    print("invalid operator ")

#6)მომხარებელს შემოატანინეთ 4 რიცხვი. შეინახეთ ისინი ცვლადებში და დაბეჭდეთ მათი საშუალო არითმეტიკული
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
num3=int(input("enter number3: "))
num4=int(input("enter number4: "))
print((num1+num2+num3+num4)/4)

#7)გააკეთეთ 3-3 მაგალითი int() და str() ფუნქციებზე
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
print(num1+num2)

age=int(input("enter your age:"))  #აქ მომხმარებელს შემოვატანინეე თავისი ასაკი 
print(age+20)   #აქ კი მომხმარებლის მითითებულ ასაკს დავუმატე 20 წელი 

num1=int("10")
num2=int("5")
print(num1/num2)

num1=str(10)
num2=str(5)
print(num1+num2)

age=26
print("your age is "+str(age))

is_adult=True
print("the user is adult: "+str(is_adult))

