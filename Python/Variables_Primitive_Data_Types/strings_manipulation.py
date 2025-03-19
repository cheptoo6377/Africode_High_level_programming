# my_string = "Hello world"
# print(my_string[1:4])
# greeting = "hello"
# name = "john dee"
# x = greeting + " " + name[0:4]
# print(x)
#..concantenation.combine strings in one statement.
# greeting = "Hello "
# name = "Jane Dee"
# x = "Hello " + name 
# print(x)
#...string methods...
# name = "john doe"
# new_name = "DOE"
# print(help(str))
#1capitalize
# cap_name = name.capitalize()
# print(cap_name)
# upper_name = name.upper()

# print(upper_name)
#..lower case
# lower_name = new_name.lower()
# print(lower_name)
# print(name.count('o'))
phone = "'0726','123','456'"
#...split...
# new_list = name.split()
# print(new_list)
# new_phone = phone.split('-')
# print(new_phone)
# my_name = "Abnednego kipngeno bett"
# new_li = my_name.split()
# middle_name = new_li[1]
# print(middle_name)

#join****
# joined_phone = '#'.join(phone)
# print(joined_phone)

# print(type(phone))
# print(type(joined_phone))

#***isalnum
python3 = "python3"
python = "m"
# print(python3.isalnum())
# print(python3.isalpha())
# text = "python123"
# print(text.isdigit())
# text2 = "01234"
# print(text2.isdigit())
#isspace
# text = " "
# print(text.isspace())
#startswith
python = "python3"
# print(python.startswith("P"))
#endswith
# print(python.endswith("3"))
#replace
# my_string = "i love python"
# new_string = my_string.replace("python","Java")
# print(new_string)
#****strip**
# text = "  python  "
# print(text)
# new_text = text.strip()
# print(new_text)

    #old way of formatting strings
# string = "John"
# age = 23
# height = 1.6
# print("Hello {} you are {} years old and {} tall" .format(string,age,height))
# print(f"HELLO,{string.upper()} i am {age +1} and {height}tall")