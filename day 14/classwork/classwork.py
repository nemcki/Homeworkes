#2) შექმენით სია სადაც, შეიტანთ მინიმუმ 10 რიცხვს, გადაუარეთ for ციკლის დახმარებით და დაბეჭდეთ თითოეული რიცხვი კენტია თუ ლუწი.
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in items:
    if i % 2 == 0:
        print("it's even")
    else:
        print("it's odd")
    


#3) შექმენით სახელების სია სადაც გექნებათ მინიმუმ 10 სახელი, დაბეჭდეთ ამ სიიდან მხოლოდ ის სახელები რომლების ინდექსებიც არის ლუწი

names = ["elemet1", "elemet2", "elemet3", "elemet4", "elemet5", "elemet6", "elemet7", "elemet8", "elemet9", "elemet10"]

even_idex_names = []

for i in range(len(names)):
    if i % 2 == 0:
        even_idex_names.append(names[i])

print(even_idex_names)




#4) შექმენით სია სადაც გექნებათ 10 რიცხვი, თქვენი დავალებაა გაიგოთ ამ სიაში ყველა ლუწი და კენტი რიცხვიოს ჯამი და დაბეჭდოთ

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even = 0

sum_odd = 0

for i in numbers:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print(sum_even)

print(sum_odd)

#5) შექმენით სია სადაც გექნებათ 10 რიცვი, შემდეგ შექმენით ახალი სია, 
#სადაც ჩაამატებთ პირველი სიიდან ყველა ლუწ რიცხვს და გაიგებთ მათ საშუალო არითმეტიკულს.
#(ახალ სიაზე გამოიყენეთ len() ფუნქცია)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)

print(sum(even_numbers) / len(even_numbers))