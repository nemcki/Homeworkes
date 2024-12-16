#2)  შექმენით string-ების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ სიაში არსებული ყველა სიტყვის სიმბოლოთა რაოდენობა
words = ["გამარჯობა", "მსოფლიო", "პროგრამირება", "Python", "შექმნა"]

for i in words:
    print(len(i))

#3) შექმენით რიცხვების სია, while loop-ის გამოყენებით გაიგეთ ამ სიაში ყველა ლუწი რიცხვის ჯამი და დაპრინტეთ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0

counter = 0

while counter < len(numbers):
    if numbers[counter] % 2 == 0:
        sum += numbers[counter]
    counter += 1

print(sum)

#4) შექმენით სახელების სია, გადაუარეთ მას for loop-ით და დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები, რომლებიც იწყებიან "A"-ზე
names = ["Ana", "Boris", "Alex", "Maria", "Artem", "Nina", "Andrew"]

for i in names:
    if i[0] == 'A':
        print(i)

#5) შექმენით რიცხვების სია, სადაც გექნებათ დუბლიკატები. გადაუარეთ მას for loop-ით და დაბეჭდეთ მხოლოდ ისეთი რცხვების ჯამი,
#რომლებიც არ მეორდება სიაში
numbers = [1, 2, 3, 2, 4, 5, 1, 6, 7, 5]

not_dublicates = []

for i in numbers:
    if i not in not_dublicates:
        not_dublicates.append(i)

print(sum(not_dublicates))

#6) შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს რიცხვს და დაბეჭდავს 1-დან შემოტანილ რიცხვამდე ყველა მარტივ რიცხვს



#7) შექმენით სია შემდგარი 5 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ მე-3 და მე-4 ელემენტები


my_list = [10, 20, 30, 40, 50]


print(my_list[2:3]) 




#8) შექმენით რიცხვების სია, შემდგარი 10 ელემენტისგან. slicing-ის გამოყენებით დაბეჭდეთ სიის ყოველი მეორე ელემენტი


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


every_second_element = numbers[::2]


print(every_second_element)


#9) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ სთრინგის ბოლო სამი სიმბოლო(გამოიყენეთ slicing და მინუსიანი ინდექსები)


text = "Hello, World!"


last_three_chars = text[-3:]


print(last_three_chars)



#10) შექმენით რიცხვების სია, დაბეჭდეთ სია თავიდან ბოლომდე slicing-ის გამოყენებით 



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


full_list = numbers[:]


print(full_list)
