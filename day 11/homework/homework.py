#1) გააიაზრეთ ეს კოდი, დაკომენტარეთ თითოეული კოდი
secret_pass = "luka1234" #
user_pass = ''

tries = 3

while tries > 0 and user_pass != secret_pass:
    user_pass = input("Enter your password (you have " + str(tries) + " tries left): ")
    tries = tries - 1

    if user_pass == secret_pass:
        print("Access granted!")
    elif tries == 0:
        print("You've reached the maximum number of tries. Access denied!")
    else:
        print("Access denied! Try again.")




#2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)
counter = 0

for i in range(1, 51):
    if i % 2 == 0:
        counter += 1

print(counter)



#3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ while loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა,
# ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)

sum = 0

quantity = 0

counter = 0

while counter < 100:
    if counter % 2 == 0:
        sum += counter
        quantity += 1
    counter += 1

print(sum // quantity)





#4) დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ while loop-ი)


number = 0

while number < 30:
    if number % 3 == 0:
        print(number)
    number += 1




#5) მომხარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)

num = int(input("Enter number> "))

for i in range(1, num):
    if num % i == 0:
        print(i)






#6) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია
num = int(input("Enter number> "))

if num > 0:
    print("num is positive")
elif num < 0:
    print("num is negative")
else:
    print(0)




#7) დაწერეთ პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს). 
#ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)



year = int(input("Enter year> "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("this is leap year")
else:
    print("this is not leap year")



#8) მომხმარებელს შემოატანინეთ რიცხვი 1-დან 100-ის ჩათვლით(ეს იქნება მისი ქულა). 
#თუ მაგალითად 90-დან 100-ის ჩათვლით ექნება ქულა გამოუტანეთ "Your grade is A",
#თუ 80-დან 90-მდე, გამოუტანეთ "Your grade is B", თუ 70-დან 80-მდე გამოუტანეთ "Your grade is C", 
#სხვა შემთხვევაში გამოუტანეთ "Your grade is D"


score = int(input("Enter you score> "))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score < 90:
    print("Your grade is B")
elif score >= 70 and score < 80:
    print("Your grade is C")
else:
    print("Your grade is D")