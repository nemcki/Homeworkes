#6) შექმენით სია სადაც ჩაამატებთ 1-დან 100-მდე ყველა ლუწ რიცხვს. საბოლოოდ დაპრინტეთ ეს სია(გამოიყენეთ for loop)

list = []

for i in range(1, 100):
    if i % 2 == 0:
        list.append(i)


print(list)



#7) შექმენით სია სადაც ჩაამატებთ ყველა რიცხვს 1-დან 50-ის ჩათვლით. 
#შემდეგ გადაუარეთ for loop-ით და ამ სიიდან წაშალეთ ყველა კენტი რიცხვი. საბოლოოდ დაპრინტეთ მიღებული სია

list = []

for i in range(1, 51):
    list.append(i)

for i in list:
    if i % 2 != 0:
        list.remove(i)


print(list)




#8) შექმენით ხილების სია სადაც გექნებათ მინიმუმ 10 ელემენტი,
#while loop-ის გამოყენებით წაშალეთ სიის ბოლო ელემენტი იქამდე სანამ სიაში არ დარჩება ორი ელემენტი. 
#ყოველი ელემენტის წაშლისას დაბეჭდეთ ხილების სია

fruits = ["apple", "pineapple", "banana", "apple", "pineapple", "banana", "apple", "pineapple", "banana", "orange"]

while len(fruits) > 2:
    fruits.pop()
    print(fruits)



#9) შექმენით პროგრამა, რომელიც დაითვლის თუ რამდენჯერ შედის სიაში რიცხვი 1 numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1] 
#(ამისათვის გადაუარეთ სიას for loop-ით)

numbers = [1,2,0,1,32,1,30,1,1,21,1,1,1]

counter = 0

for i in numbers:
    if i == 1:
        counter += 1

print(counter)

#10) შექმენით ორი ცარიელი სია, for loop-ის გამოყენებით მომხარებელს 5-ჯერ შემოატანინეთ ნებისმიერი სიტყვა. 
#თუ შემოტანილი სიტყვის სიგრძე არ აღემატება 5-ს ჩაამატეთ პირველ სიაში,
#სხვა შემთხვევაში მეორეში. საბოლოოდ დაბეჭდეთ ორივე სია

list1 = []

list2 = []

for i in range(5):
    i = input("Enter any word> ")
    if len(i) <= 5:
        list1.append(i)
    else:
        list2.append(i)

print(list1)

print(list2)