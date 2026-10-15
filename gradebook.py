grade_book = {
    "Huck" : "C+",
    "Franco" : "D-",
    "Max" : "A"
}

user_input = input("Who's grade you wanna check? ")

check_dic = grade_book.get(user_input)

if check_dic == None:
    print("Student not found")
else:
    print(check_dic)
