print("hello you are going to help beep find his battery")
print("where should he look bedroom/bathroom/lab")
look = input()
if look == "bedroom":
    print("where in the bedroom should i look?")
    search1 = input()
    if search1 == "cupboard":
        print("found some hobnobs but no battery")
    else:
        print("nothing there")
elif look == "bathroom":
    print("where in the bathroom should i look?")
    search2 = input()
    if search2 == "bathtub":
        print("found pirate ducky but no battery")
    else:
        print("nothing there")
elif look == "lab":
    print("where in the lab should i look")
    search3 = input()
    if search3 == "table":
        print("yes i found the battery at last")
    else:
        print("not here but i sense it close")
else:
    print("i dont know where that is but ill keep looking")