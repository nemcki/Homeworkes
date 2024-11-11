# 1)თქვენი დავალებაა შექმნათ მარტივი ჩატ-ბოტი, რომელიც კოდის გაშვებისთანავე მიესალმება მომხარებელს და ჰკითხავს "How are your?",
#თუ მომხარებელი შეიყვანს, "Normal" დაბეჭდეთ "Bot:I hope you will get better", სხვა შემთხვევაში თუ შემოიყვანს "Great", 
#დაუბეჭდეთ "Bot:Good! Have a nice day", ხოლო თუ შემოიყვანა "Sad" ან "Super Sad" დაუბეჭდეთ "Bot:It's sad". 
#საბოლოოდ დაბეჭდეთ "Good bye!" და გათიშეთ while ციკლი. ამისათვის მას გადაეცით სწორი პირობა(მინიშნება: 
# შექმენით ცვლადი რომლის მნიშვნელობა თავიდან იქნება False, while ციკლს პირობად გაუწერეთ ეს ცვლადი, 
#თუ მომხარებელმა სწორი ინფორმაცია შემოიყვანა მისი ნიშვნელობა გახდება True და როცა ყველა პირობა შესრულდება while ციკლი გაითიშება).
#თუ მომხარებელი შემოიყვანს ისეთ ინფორმაციას რაზეც თქვენი ბოტი არ არის დაპროგრამირებული, 
#დაბეჭდეთ "Bot: Sorry, I didn't understand, repeat."
#(ამ შემთხვევაში while ციკლისთვის შექმნილი ცვლადის მნიშვნელობა არ იცვლება და ციკლი არ წყვეტს მუშაობას)
#დაგჭირდებათ: while loop; input; if/else; and or.
#თქვენი სურვილით დაამატეთ სხვა ფუნქციები და გააუმჯობესეთ ჩატ-ბოტი

while True:
    print("go on")
    user_input = input("enter your question or exit to quit: ").lower()
    if user_input == "how are you?":
        print("i am doing well, thank you!")
    elif user_input == "whats the weather like?":
        print("its sunnny and warm today.")
    elif user_input == "give me bitcoin":
        print("i am sorry, but i can not give you bitcoin.")
    elif user_input == "hack nasa":
        print("i am not hacking nasa, i am a python programmer.")
    elif user_input == "exit":
        print("goodbye!")
        break
    else:
        print("i am not sure how to answer that.")




#2) შექმენით პრეზენტაცია, სადაც ისაუბრებთ თუ როგორ მუშაობს CPU, RAM, GPU. კარგი იქნება თუ დახატავთ

