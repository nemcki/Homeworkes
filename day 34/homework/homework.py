#1) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი.
# ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.
#არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება


def manual_replace(s):

    new_str = ''
    
    for char in s:
        if char == ' ':
            new_str += '-'
        else:
            new_str += char
    
    return new_str


#2) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, 
# მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. 
# ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.
#გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step


def manual_range(*args):
 
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1

    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1

    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        return "Error: Invalid number of arguments."
    
    result = []
    
    if step > 0:
        i = start
        while i < end:
            result.append(i)
            i += step
    elif step < 0:
        i = start
        while i > end:
            result.append(i)
            i += step
    
    return result



#4) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს string-ს. 
# ამ ფუნქციამ უნდა გაიგოს გადმოცემულ string-ში თითოეული სიმბოლოს რაოდენობა და ჩაამატოს ახალ სიაში
# (ერთი სიმბოლის რაოდენობა მხოლოდ ერთხელ უნდა ჩაამატოთ. მგალითად თუ string-ში 5 "a" გვხვდება, 
# რიცხვი 5 მასივში მხოლოდ ერთხელ უნდა ჩავამატოთ, მაგრამ სხვა სიმბოლოც თუ გვხვდება იგივე რაოდენობით, 
# მას ვამატებთ ჩვეულებრივ). საბოლოდ დაასორტირეთ მიღებული სია ზრდადობით და დააბრუნეთ



#ვერ მივხვდიიიიი ????????????????????????




#5)შექმენთ ფუნქცია, რომელიც არგუმენტად იღებს სიმბოლოების სიას.
#  დაასორტირეთ ეს სია ანბანის მიხედვით, გადააქციეთ string-ად და დააბრუნეთ

def sort_and_join(char_list):
    char_list.sort()
    
    result = ''.join(char_list)
    
    return result


#6) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვების სიას და აბრუნებს მას კლებადობის მიხედვით დასორტირებულს

def sort_descending(num_list):

    num_list.sort(reverse=True)
    
    return num_list

