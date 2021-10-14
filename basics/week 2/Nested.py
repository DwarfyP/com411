print("does the book have a hard/soft cover?")
book = input()
if book == "soft":
    print("is book perfectly bound? yes/no")
    bound = input()
    if bound == "yes":
        print("Soft cover, perfectly bound books are very popular")
    else:
        print("shame soft and bound is a perfect combo")
else:
    print("hard cover nice choice")