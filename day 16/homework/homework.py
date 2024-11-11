#1) დაასრულეთ წინა გაკვეთილით პრეზენტაცია და ასევე გააკეთეთ პრეზენტაცია ინტერნეტზე
#(როგორ მუშაობს ის და როგორ უკავშირდება ერთი კომპიუტერი მეორეს)







#2) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი

list = [1,2,31,4,5]

max_number = list[0]

for i in list:
    if i > max_number:
        max_number = i

print(max_number)






#3) შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(factorial)


#4) შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი

list = [1,2,31,4,5]

max_number = list[0]

for i in list:
    if i < max_number:
        max_number = i

print(max_number)


#5) შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, 
# შემდეგ შექმენით ახალი სია სადაც გექნებათ მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).

list = [4, -2, 7, -5, -10, 3, -1, 8]

negative = []

index = 0

while index < len(list):
    if list[index] < 0:
        negative.append(list[index])
    index += 1


#6) შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)

numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])



#7) შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება

characters = ['a', 'b', 'c', 'a', 'd', 'b', 'e', 'f', 'e']

empty_list = []

for i in characters:
    if i not in empty_list:
        empty_list.append(i)


print(characters)

print(empty_list)




#8) შექმენით ცლვადი სადაც შეინახავთ string-ს, 
# შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის

string = "Hello"

print(string[::-1])




#9) დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი

input1 = int(input("Enter any number> "))

list = []

for i in range(1, input1 + 1):
    if input1 % i == 0:
        list.append(i)

print(list)



#10) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის

year = int(input("Enter any year> "))

#(წელს - 1) // 100 + 1

print((year - 1) // 100 + 1)