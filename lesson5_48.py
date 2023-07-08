def say_something():
    # print('hi')
    s = 'hi'
    return  s

print(type(say_something))
# f = say_something
# f()

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)

result = what_is_this('green')
print(result)

result = what_is_this('blue')
print(result)