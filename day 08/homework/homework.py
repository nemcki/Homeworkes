#2)გამოიტანეთ თქვენი სახელი და გვარი იმდენჯერ, რამდენი წლისაც ხართ

full_name=("giorgi iadze")
for i in range(26):
     print(full_name)

#3)გამოიტანეთ ტერმინალში რიცხვები 1-დან 20-ის ჩათვლით


for i in range(1, 21):
     print(i)

#4)გამოიტანეთ ტერმინალში რიცხვები 20-დან 0-მდე

for i in range(20, -1, -1):
    print(i)

#5)გამოითვალეთ 1-დან 50-ის ჩათვლით ყველა რიცხვის ჯამი და დაპრინტეთ საბოლოო შედეგი
num = 0
for i in range(50):
    num = num + i
print(num)

#6)დაბეჭდეთ 1-დან 5-ის ჩათვლით რიცხვთა კვადრატი(n * n)

for i in range(6):
     print(i * i)

#7)დაბეჭდეთ ყველა ლუწი რიცხვის ჯამი 1-დან 10-ის ჩათვლით

total_sum = sum(i for i in range(1, 11) if i %2 == 0)
print(total_sum)

#8)მომხარებელს შემოატანინეთ რიცხვი და შეინახეთ ცვლადში, შემდეგ კი 0-დან შემოტანილი რიცხვის ჩათვლით შეამოწმეთ, თუ ლუწია დაბეჭდეთ რიცხვი is Even, სხვა შემთხვევაში რიცხვი is Odd;(მაგალითად 4, ლუწია ამიტომაც დაბეჭდავთ "4 is Even")

num1=int(input("enter your number :"))
for i in range(num1):
    if num1 %2 == 0:
        print("number is even")
        break
    else :
     print("number is odd ")
     break


