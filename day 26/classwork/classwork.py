#1) შექმენით ფუნქცია, manual_capitalize რომელიც იქნება capitalize ფუნქციის კლონი


def manual_capitalize(text):
    if len(text) == 0:
        return text

    return text[0].upper() + text[1:].lower()



#2) შექმენით ფუნქცია, manual_title, რომელიც იქნება title ფუნქციის კლონი

def manual_title(text):
    words = text.split() 
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
