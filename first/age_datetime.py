from datetime import date

class Human:
    age = 0
    name = ''
    birthday = 0

    def __init__(self,name,birthday):
        self.name = name
        self.birthday = birthday
        self.age = date.today()-birthday
    def set_birthday(self,day):
        self.birthday = day
        self.age = self.age - day

    def get_birthday(self):
        return self.birthday

    def get_age(self):
        return self.age


if __name__ == '__main__':
    student = Human('Don',date(int(input()),int(input()),int(input())))
    print(student.get_age())
    string = list(map(Human.set_birthday(23), student))  # можно истользовать методы объктов
    print(string)