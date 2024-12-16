#2) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სახელი და დაბეჭდავს მისთვის მიესალმებას (მაგალითად: "Hello Nika"). 
# გამოძახეთ ეს ფუნქცია 2-ჯერ და გადაეცით სხვადასხვა სახელი


def greeting(name):
    print("Hello " + (name))


greeting("Nika")
greeting("Ana")



#3)შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა 2 რიცხვი. ფუნქციამ უნდა დაბეჭდოს ამ რიცხვების ნამრავლი. საბოლოოდ გამოიძახეთ ის


def multiply(num1, num2):
    print(num1 * num2) 


multiply(4, 5)


#4) შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა სია. ფუნქციამ უნდა დაბეჭდოს ეს სია შებრუნებულად(არ გამოიყენოთ slicing-ი)


def reverse_list(my_list):
    
    for i in range(len(my_list)-1, -1, -1):
        print(my_list[i])


reverse_list([1, 2, 3, 4, 5])


#5) შექმენით ფუნქცია, რომელსაც გადასცემთ რიცხვების სიას. გადაუარეთ გადმოცემულ სიას for ციკლით და დააბრუნეთ ახალი სია, 
#სადაც ჩამატებული იქნება გადმოცემული სიიდან მხოლოდ ის რიცხვები, რომლებიც მეტია 10-ზე. საბოლოოდ დააბრუნეთ ეს სია


def filter_greater_than_ten(numbers):
    result = []  
    for num in numbers:
        if num > 10:
            result.append(num)  
    return result


numbers = [5, 12, 7, 18, 3, 15, 8]
filtered_numbers = filter_greater_than_ten(numbers)


print(filtered_numbers)


#6) შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, 
# გამოიყენეთ slicing-ი


def remove_first_and_last(char_list):
    return char_list[1:-1]  


characters = ['a', 'b', 'c', 'd', 'e']
modified_list = remove_first_and_last(characters)


print(modified_list)


#7) შექმენით ფუნქცია, რომელსაც გადაეცემა ორი რიცხვების სია, 
# გადაურეთ ორივეს for ციკლით და გაიგეთ თითოეულ სიაში რიცხვების ჯამი(შეინახეთ ცალკე ცვლადებში), 
# გაამრავლეთ ორივე ერთმანეთზე და დააბრუნეთ
# ფუნქცია multiply_sums, რომელიც ორ რიცხვთა სიას იღებს


def multiply_sums(list1, list2):
    sum_list1 = 0  
    sum_list2 = 0  
    
    
    for num in list1:
        sum_list1 += num  
    
    
    for num in list2:
        sum_list2 += num 
    
    
    result = sum_list1 * sum_list2
    
    return result  


list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = multiply_sums(list1, list2)

print(result)





#8) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას while ციკლით და ჩაამატეთ გაორმაგებული რიცხვები ახალ სიაში.
#  საბოლოოდ დააბრუნეთ ეს სია


def double_numbers(numbers):
    doubled_list = []  
    index = 0  
    

    while index < len(numbers):
        doubled_list.append(numbers[index] * 2)  
        index += 1  
    
    return doubled_list 


numbers = [1, 2, 3, 4, 5]
doubled_numbers_list = double_numbers(numbers)


print(doubled_numbers_list)




#9) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ ლუწი რიცხვები ახალ სიაში.
#  საბოლოოდ დააბრუნეთ ეს სია


def filter_even_numbers(numbers):
    even_numbers = []  
    
    
    for num in numbers:
        if num % 2 == 0:  
            even_numbers.append(num)  
    
    return even_numbers  


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_list = filter_even_numbers(numbers)


print(even_numbers_list)





#10) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული სიიდან მხოლოდ იმ სახელებს, 
# რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია


def filter_names_starting_with_n(names):
    filtered_names = []  
    
    
    for name in names:
        if name.startswith('N'): 
            filtered_names.append(name)  
    
    return filtered_names  

# ფუნქციის გამოძახება
names = ['Nika', 'Ana', 'Nino', 'Makina', 'Nodo']
filtered_names_list = filter_names_starting_with_n(names)


print(filtered_names_list)
