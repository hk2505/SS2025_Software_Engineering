from datetime import date

class Person():
    def __init__(self, first_name, last_name,  birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.__birth_date = birth_date

    def Age(self):
        y, m, d = map(int, self.__birth_date.split("-"))
        t = date.today()

        return t.year -y - ((t.month, t.day) < (m,d))

class Subject(Person):

    def __init__(self, first_name, last_name, birth_date, sex):
        super().__init__(first_name, last_name, birth_date)
        self.sex = sex
        self.max_hr = self.estimate_max_hr()


    def estimate_max_hr(self):
        age = self.get_age()
        if self.sex == "male":
            return 223 - 0.9 * age
        elif self.sex == "female":
            return 226 - 1.0 * age

class Examiner(Person):
    def __init__(self, first_name, last_name, birth_date):
        super().__init__(first_name ,last_name , birth_date)
    

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date


    def add_subject(self, subject):
        self.subject.append = subject

    def add_examiner(self, examiner):
        self.supervisor.append = examiner