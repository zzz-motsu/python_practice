# import lesson_package.utils
# from lesson_package.tools import utils
# from lesson_package.talk import human
# from lesson_package.talk import monster
from lesson_package.talk import monster

# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')

# print(r)

# print(human.sing())
# print(human.cry())

print(monster.sing())
print(monster.cry())

try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')