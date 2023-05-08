class Person(object):
    def talk(self):
        print('talk')

    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

# class PersonCarRobot(Person, Car):
class PersonCarRobot(Car, Person):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
person_car_robot.run()
person_car_robot.fly()