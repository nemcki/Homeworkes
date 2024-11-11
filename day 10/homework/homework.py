
#2)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ, რამდენჯერ შედის შემოტანილი რიცხვი 100-ში. გააკეთეთ ყველაზე მოკლე გზით(ამისათვის გამოიყენეთ გაყოფის სწორი ტიპი)
num=int(input("pleas enter number: "))

print(100 // num)








#3)while ციკლის გამოყენებით გამოიტანეთ 1-დან 20-მდე ყველა კენტი რიცხვის ჯამი
sum = 0

counter_variable = 1

while counter_variable < 20:
    if counter_variable % 2 != 0:
        sum += counter_variable
    counter_variable += 1


print(sum)


#4)მომხარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ ის, რომელიც არის მეტი. თუ ორივე რიცხვი ტოლია დაბეჭდეთ "Both numbers are equal"

num1 = int(input("Enter first number> "))

num2 = int(input("Enter second number> "))

if num1 > num2:
    print("first number is more")
elif num2 > num1:
    print("second number is more")
else:
    print("Both numbers are equal")



#5)მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ შემოტანილი რიცხვის ფაქტორიალი(დასერჩეთ რა არის ფაქტორიალი)
result = 1

num = int(input("Enter any number> "))

for i in range(1, num):
    result *= i

print(result)


result = 1

counter_variable = 1

num = int(input("Enter any number> "))

while counter_variable < num:
    result *= counter_variable
    counter_variable += 1

print(result)



#6)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ის ცვლადში. შემდეგ დაბეჭდეთ შემოტანილი რიცხვის ჩათვლით ყველა რიცხვის კვადრატის ჯამი
num = int(input("Enter any number> "))

sum = 1

for i in range(1, num):
    num = i ** 2
    num += sum

print(sum)





#7)თამაში "რიცხვის გამოცნობა". შექმენით ცვლადი და შეინახეთ რომელიმე რიცხვი 1-დან 20-ის ჩათვლით(ეს იქნება ჩაფიქრებული რიცხვი). 
#გამოიყენეთ while loop-ი და მომხარებელს შემოატანინეთ რიცხვი იქამდე სანამ არ გამოიცნობს მას. 
#თუ მომხარებლის მიერ შემოტანილი რიცხვი მეტია ჩაფიქრებულზე, დაპრინტეთ To high, თუ ნაკლებია Too low,
#ხოლო იმ შემთხვევაში თუ მომხარებელი გამოიცნობს რიცხვს დაპრინტეთ "You win"

win_number = 13

num1 = 0

while num1 != win_number:
    num1 = int(input("Enter number 1-20> "))
    if num1 < win_number:
        print("Too low")
    elif num1 > win_number:
        print("Too high")
    else:
        print("You win")