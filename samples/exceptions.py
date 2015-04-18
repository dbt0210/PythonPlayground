try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except FileNotFoundError as err:
    print("File not found: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error.")
finally:
    # DO something!
    pass

try:
    with open("my2ndfile.txt") as f:
        for line in f:
            print(line)
except:
    print("Some error occured.")
