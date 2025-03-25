def sum_numbers(a, b):
    return a + b
# results = sum_numbers(17,5)
# resultss = sum_numbers(10,5)

# print(results)
# print(resultss)
# def cart (item,price,qty=""):
#      print(f"{qty} {item} ksh {price:.2f}")
# cart(2,"mangoes",100)
# cart(100,4,"banana")
#...keyword
# cart(qty=2,price=100,item="mangoes")
# cart(4,price=100,item="banana")
def cost_of_items(qty,item, price, ):
    print(f"{qty} {item} ksh {price:.2f} total cost {qty*price:.2f}")
cost_of_items(4,"sugar",100)