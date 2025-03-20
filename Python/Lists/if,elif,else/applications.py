a = 10
b = 5
c = 10
text ="hello"
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
listy = list1
if a > b and c>=a:
    print("a is greater than b and c is greater than or equal to a")
elif a <= b or c!=b:
    print("either a is less than or equal to b or c is not equal to b")
else:
    print("none of the conditions were met")

if list1 == list2 and list1 is not list2:
    print("list1 and list2 have the same values but are different objects")
elif not (a==b):
    print("a is not equal to b")
else:
    print("none of the conditions were met")
if "e" in text and 6 not in list1:
    print('the letter "e" is in the text and 6 is not in list1')
elif "x" not in text or  3 in list1:
    print("the letter 'x' is not in the text or 3 is in list1")
else:
    print("none of the conditions were met")
if a >b and (3) in list1 or text is not None:
    print("complex condition met:a is greater than b and 3 is in list1 or text is not None")
elif list1 is listy and len(text) > 0:
    print("list1 and listy are the same object and the length of text is greater than 0")
else:
    print("none of the conditions were met")