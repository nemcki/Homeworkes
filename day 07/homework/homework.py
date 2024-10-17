#2) შექმენით ცვლადები და შეინახეთ სხვადასხვა მონაცემთა ტიპის მნიშვნელობები. შემდეგ შეამოწმეთ თითოეული ცვლადის მონაცემთა ტიპი.
num1=5.5
num2=10
num3="giorgi"
print(type(num1))
print(type(num2))
print(type(num3))

#3) მომხარებელს შემოატანინეთ რიცხვი და შეამოწმეთ მისი ტიპი, ისე რომ დაგიბრუნდეთ integer
num1=int(input("enter number: "))
print(type(num1))

#4)გააკეთეთ 5-5 მაგალთი შედარების ოპერატორებზე

print(5 >= 5)
print(10 > 5)
print(10 == 10)
print(3 < 5 )
print(3 <= 5)

#5)დაბეჭდეთ ყველა შესაძლო ვარიანტი and და or ოპერატორებზე

print(5 > 3 and 4 > 2)
print(5 > 3 and 3 > 5)
print(8 < 5 and 10 > 15)

print(5 > 3 or 3 > 2)
print(3 > 5 or 5 > 3)
print(5 < 4 or 5 > 6)

#6)მომხარებელს შემოატანინეთ მისი ასაკი, როგორც სტრინგი და დაბეჭდეთ მისი ტიპი. შემდეგ შეუცვალეთ მას მონაცემთა ტიპი ჯერ integer-ად, შემდეგ float-ად (ყოველ გარდაქმნაზე დაბეჭდეთ შედეგი)

age = input("please enter your age: ")
print(type(age))

age = int(age)
print(type(age))

age = float(age)
print(type(age))

#7) მომხარებელს შემოატანინეთ მისი საყვარელი რიცხვი და გაიგეთ არის თუ არა ის ლუწი

num = int(input("please enter your favourite number: "))

if num %2 == 0:
    print("your number is even")
else:
    print("your number is odd")

#8)მომხარებელს შემოატანინეთ მისი ასაკი და სახელი, შემდეგ შეამოწმეთ არის თუ არა ის სრულწლოვანი და უდრის თუ არა მისი სახელი თქვენს სახელს

my_name = "giorgi"
user_name = input("enter your name: ")
age = int(input("enter your age: "))

if age < 18:
    print("you are kid")
else:
    print("you are over age")

if user_name == my_name:
    print("we have same name")
else:
    print("we dont have the same name")