#1) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.
#მგალითად: "Hello" >>> "H - 1", "e - 2"...

text = "Hello"

for index, char in enumerate(text, start=1):
    print(f"{char} - {index}")




#2) შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. 
#ამ ფუნქციამ უნდა შეართოს ეს სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი
#არ გამოიყენოთ .join() ფუნქცია

def manual_join(strings, delimiter):
    if not strings:
        return ""
    
    result = strings[0]
    
    for string in strings[1:]:
        result += delimiter + string
    
    return result




#3) შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ან სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ.
#დააბრუნეთ მიღებული შედეგი.

def manual_count(input_data, element):
    count = 0
    
    if isinstance(input_data, list):
        for item in input_data:
            if item == element:
                count += 1
    
    elif isinstance(input_data, str):
        for char in input_data:
            if char == element:
                count += 1
    
    return count



#4) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. 
#ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.
#არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება

def manual_replace(input_string):
    result = ""  # შედეგი, რომელშიც შევაგროვებთ ცვლადს
    
    # გადავუაროთ სთრინგის თითოეულ სიმბოლოზე
    for char in input_string:
        if char == " ":  # თუ სიმბოლო არის space
            result += "-"  # შევცვალოთ ტირეთი
        else:
            result += char  # სხვა შემთხვევაში სიმბოლო დარჩება უცვლელი
    
    return result  # საბოლოო შედეგი დავაბრუნოთ



#5) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, 
#ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი,
#მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. 
#ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.
#გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step


def manual_range(*args):
    # პირველ რიგში, გადამოწმდება რამდენი არგუმენტი გვაქვს
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
        # თუ გადაეცემა მეტი არგუმენტი, ფუნქცია ვერ იმუშავებს
        raise TypeError("manual_range expected at most 3 arguments, got more.")
    
    result = []

    if step > 0:
        current = start
        while current < end:
            result.append(current)
            current += step
    elif step < 0:
        current = start
        while current > end:
            result.append(current)
            current += step
            
    return result
