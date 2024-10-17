#1) მოხარებელს შეეკითხეთ მისი სახელი,გვარი ასაკი და იმეილი, შემდეგ კი შემოტანილი მნიშვნელობები დაბეჭდეთ ტერმინალში. გამოიყენეთ ეტიკეტი, რომ მიანიშნოთ მომხარებელს თუ რა უნდა შემოიტანოს კონკრეტულ შესაყვან ველში.
name=str(input("enter your name: "))
lastname=str(input("enter your lastname: "))
age=str(input("enter your age: "))
email=str(input("enter your email: "))
print("hellow your name is: "+ name +" "+"your lastname is: "+lastname+" "+"your age is: "+age+" "+"your email is: "+email)

#2)მომხარებელს შემოატანინეთ ორი რიცხვი და გამოიყენეთ ყველა არითმეტიკული ოპერაცია ამ ორ რიცხვს შორის.
num1=int(input("enter number1: "))
num2=int(input("enter number2: "))
print( num1+num2)
print( num1*num2)
print( num2-num1)
print( num2/num1)

#3)კომენტარებით ახსენით თუ რა არის input-ი და output-ი, ასევე რისთვის გამოიყენება ისინი

#input-არის პროცესი, როდესაც კომპუტერში შედის რაღაც ინფორმაცია.
#output-არის პროცესი, როდესაც კომპიუტერიდან(ხშირშემთხვევაში input-ის საპასუხოდ) გამოდის რაღაც ინფორმაცია პითონში, input()-ფუნქცია გამოიტანს შესაყვან ველს.
#input გამოიყენება იმისთვის რომ ჩვენ კომპიუტერს მივაწოდოთ საჭირო ინფორმაცია, ეს ფუნქცია გვეხმარება პითონში იმისთვის რომ მივიღოთ მომხარებლისგან საჭირო ინფორმაცია და გამოვიყენოთ მომავალში
#output გამოიყენება იმისთვის რომ კომპიუტერმა მოგვაწოდოს საჭირო ინფორმაცია 

#4)შექმენით კალკულატორის პროგრამა სადაც მომხარებელი შემოიტანს ორ რიცხვს და 4 არითმეტიკული ოპერაციიდან ერთერთს. შეასრულეთ ამ ორ რიცხვს შორის არჩეული არითმეტიკული ოპერაცია

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
operation=input("enter en operator (+, -, *, /,): ")
if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("invalid operator")