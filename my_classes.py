class Subject():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.max_hr = self.estimate_max_hr()
        
    def estimate_max_hr(self):
        """A function that estimates the maximum heart rate of a subject"""
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
            max_hr_bpm = input("Enter maximum heart rate:")

        return(max_hr_bpm)

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