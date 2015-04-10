from random import choice

val = choice(range(1, 4))
# so this is the basic idea:
# create a dictionary mapping values to functions
d = {
    1: lambda: print("Some option."),
    2: lambda: print("Some other option."),
    # (use list comprehension to put multiple commands)
    3: lambda: [print("Interestingly, "), print("these are executed when you put them in a list")]
}
# call the function that is mapped to a specific value
d[val]()

# that's basically what happens here as well
{
    1: lambda: print("Some option."),
    2: lambda: print("Some other option."),
    3: lambda: [print("Interestingly, "), print("these are executed when you put them in a list")]
}.get(val)()