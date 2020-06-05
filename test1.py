import torch
print(torch.cuda.is_available())
class Person(object):
    """Hello nice to meet you"""

    def __init__(self,name,age):
        print("init called")
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        print("new called")
        return super(Person,cls).__new__(cls)

    def __str__(self):
        return "name: %s ,age: %d"%(self.name,self.age)

    def __call__(self, *args, **kwargs):
        print('Nice')
        
    def say(self,*args):
        print("What is your name? ")

class Student(Person):
    def __init__(self,name,age):
        # Person.__init__(self,name,age)
        # super().__init__(name,age)
        super().__init__(name, age)
        self.name = name
        self.age = age
    def say(self):
        print("My name is %s"% self.name)


if __name__ == '__main__':
    # Person("Person",28).say()
    lihua = Student("li hua",32)
    lihua.say()



# print("   Good ".center(20))
# print("*".join("Hello Mini nice to meet you".split(' ')))
# a = [1,2,3,4,5]
# a.insert(3,'go')
# a.remove(1)
# print(a)



