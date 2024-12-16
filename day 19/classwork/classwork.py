#1) შექმენით რიცხვების სია, შემდგარი მინიმუმ 10 ელემენტისგან. გადაუარეთ ამ საის while loop-ის გამოყენებით. 
# გაიგეთ ცალკე ლუწი და კენტი რიცხვების ჯამი,
#  საბოლოოდ შეადარეთ ისინი ერთმანეთს და დაპრინტეთ უდიდესი


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


even_sum = 0
odd_sum = 0


index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:  
        even_sum += numbers[index]
    else:  
        odd_sum += numbers[index]
    index += 1  


max_sum = max(even_sum, odd_sum)


print("hight_sum:", max_sum)



#2) შექმენით სიმბოლოების სია, გადაუარეთ მას for loop-ით და სიიდან ყველა სიმბოლოს შორის მოახდინეთ კონკადინაცია. 
# ციკლის გარეთ დაგჭირდებათ ცვლადი სადაც შაამატებთ ამ სთრინგებს


characters = ['a', 'b', 'c', 'd', 'e']


concatenated_string = ""


for char in characters:
    concatenated_string += char


print(concatenated_string)
