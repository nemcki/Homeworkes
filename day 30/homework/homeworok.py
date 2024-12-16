#2) შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია

def modify_list():
    
    my_list = [10, 20, 30, 40, 50]
    
    del my_list[2]
    
    my_list.insert(0, 100)
    
    
    return my_list



#3) შექმენით ფუნქცია manual_len, რომელსაც გადაეცემა სთრინგი ან სია, 
# ხოლო ფუნქციამ უნდა დააბრუნოს გადმოცემული სთრინგის/სიის სიგრძე(არ გამოიყენოთ len-ი)

def manual_len(item):

    length = 0
    
    for element in item:
        length += 1
    
    return length


#4) შექმენით ფუნქცია manual_pop, რომელსაც გადაეცემა ორი არგუმენტი, სია და ინდექსი. 
# წაშალეთ სიიდან, გადმოცემულ ინდექსზე მყოფი ელემენტი. საბოლოოდ კი დააბრუნეთ ეს სია(არ გამოიყენოთ .pop ფუნქცია

def manual_pop(my_list, index):

    new_list = []

    for i in range(len(my_list)):

        if i != index:
            new_list.append(my_list[i])
    
    return new_list
