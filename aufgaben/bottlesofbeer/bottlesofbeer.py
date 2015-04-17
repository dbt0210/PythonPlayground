for i in range(99, -1, -1):
    print("{0} bottle{1} of beer on the wall! {0} bottle{1} of beer!".format("No more" if i == 0 else i, "s" if i != 1 else ""))
    if i != 0:
        print("Take one down, pass it around!", end=" ")
    else:
        print("Go to the store and buy some more!", end=" ")
    print("No more" if i == 1 else ("99" if i == 0 else i - 1), "bottles" if i - 1 != 1 else "bottle", "of beer on the wall!\n")