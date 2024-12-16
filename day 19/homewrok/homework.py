#1) შექმენით სია შემდგარი მინიმუმ 5 ელემენტისგან. წაუშალეთ ამ სიას ბოლო ორი ელემენტი და დაბეჭდეთ ის


numbers = [1, 2, 3, 4, 5, 6]


modified_list = numbers[:-2]


print(modified_list)




#2) შექმენით ცვლადი, სადაც შეინახავთ სთრინგს. slicing-ის მეშვეობით დაბეჭდეთ ის უკუღმა


text = "Hello, World!"


reversed_text = text[::-1]


print(reversed_text)





#3) შექმენით რიცხვების სია შემგარი 10 მინიმუმ ელემენტისგან. გაიგეთ ამ სიაში ყველაზე პატარა და დიდი რიცხვი, 
# შემდეგ კი დაბეჭდეთ მათი ჯამი


numbers = [3, 7, 1, 9, 4, 6, 2, 8, 10, 5]


min_num = min(numbers)
max_num = max(numbers)


sum_of_min_max = min_num + max_num
print(sum_of_min_max)




#4) შექმენით ცვლადი სადაც შეინახავთ სთრინგს და გაიგეთ, 
# არის თუ არა ის პალინდრომი(პალინდრომი არის ისეთი სიტყვა, რომელიც ორივე მხრიდან ერთნაირად იკითხება, მაგალითად, "ana"...)


text = "ana"


is_palindrome = text == text[::-1]


print(is_palindrome)



#5) შექმენით რიცხვების სია, გადაუარეთ მას for loop-ით, 
# გაიგეთ რამდენი ლუწი და რამდენი კენტი რიცხვი გვაქვს სიაში და დაბეჭდეთ მათი რაოდენობა
# შექმენით რიცხვების სია



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_count = 0
odd_count = 0


for number in numbers:
    if number % 2 == 0:  
        even_count += 1
    else:  
        odd_count += 1


print("even_num:", even_count)
print("odd_num:", odd_count)


#6) შექმენით სია, სადაც გექნებათ 1-ანები და 0-ანები, 
# შექმენით ახალი სია, რომელიც თავიდან იქნება ცარიელი. 
# for loop-ით გადაუარეთ პირველ სიას და თუ საიტერაციო ცვლადის მნიშვნელობა იქნება 1, 
# ახალ სიაში ჩაამატეთ True, სხვა შემთხვევაში False. საბოლოოდ დაბეჭდეთ ახალი სია


binary_list = [1, 0, 1, 1, 0, 0, 1]


boolean_list = []


for item in binary_list:
    if item == 1:
        boolean_list.append(True)
    else:
        boolean_list.append(False)


print(boolean_list)
