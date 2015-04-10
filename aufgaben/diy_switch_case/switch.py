from random import choice

val = choice(range(1, 4))
d = {
    1: lambda: print("Some option."),
    2: lambda: print("Some other option."),
    3: lambda: [print("Interestingly, "), print("these are executed when you put them in a list")]
}
d[val]()

