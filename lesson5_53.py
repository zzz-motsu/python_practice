# def menu(entree='beef', drink='wine'):
#     print(entree, drink)
#
# menu(entree='beef', drink='coffee')

def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

# menu(entree='beef', drink='wine')

menu(**d)

def menu2(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for k, v in kwargs.items():
        print(k, v)

menu2('banana', 'apple', 'orange', entree='beef', drink='coffee')