class Subject():
    def __init__(self, first_name, last, sex, age):
        self.first_name = first_name 
        self.last = last 
        self.sex = sex 
        self.age = age
        self.max_hr = self.estimate_max_hr()
        
    def estimate_max_hr(self):
        if self.sex == "male":
            self.max_hr_bpm = 223 - 0.9 * self.age
        elif self.sex == "female":
            self.max_hr_bpm = 226 - 1.0 * self.age
        else:
            self.max_hr_bpm = input("Enter maximum heart rate:")
        return self.max_hr_bpm

class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Experiment():
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
      self.subject = subject
    def add_supervisor(self, supervisor):
        self.supervisor = supervisor

# Damit die Ausgabe im Test.py als Text ausgegeben wird und nicht nur die technische Information
    def __str__(self):
        return (
            f"Experiment: {self.name} am {self.date}\n"
            f"Subject: {self.subject.first_name} {self.subject.last}, "
            f"Alter: {self.subject.age}, Geschlecht: {self.subject.sex}, "
            f"Max HR: {self.subject.max_hr_bpm}\n"
            f"Supervisor: {self.supervisor.first_name} {self.supervisor.last_name}"
        )
