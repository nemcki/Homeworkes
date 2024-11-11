#while ციკლის საშვალებით გამოიტანეთ რიცხვები 1-იდან 10-მდე
num = 0
while num < 10:
    print(num)
    num = num + 1

#2)while ციკლის საშვალებით გამოიტანეთ რიცხვები 20-იდან 0-მდე

num=20
while num > 0:
    print(num)
    num=num-1

#3)while ციკლის საშვალებით გამოიტანეთ 1-დან 20-მდე მხოლოდ ლუწი რიცხვები
num=0
while num < 20:
    print(num)
    num=num+2

#4)while ციკლის საშვალებით გამოიტანეთ 1-იდან 100-მდე ყველა 5-ის ჯერადი რიცხვი

num1=0
while num1 < 100:
    num1=num1+5
    print(num1)
    
#5)while ციკლისა და input-ის საშვალებით მომხარებელს შემოატანინეთ პაროლი სანამ არ იქნება ის "goa123"-ის ტოლი

pasword=""
while pasword != "goa123":
    pasword=input("enter your pasword: ")

    