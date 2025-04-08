
#Angepasster Code
from datetime import date #Importiere das Modul für Datumsoperationen
    #Superklasse Person mit den Attributen Vorname und Nachname 
class Person:
     def __init__(self, first_name, last_name,Geburtsdatum):
        self.first_name = first_name
        self.last_name = last_name
        self.__birthdate = Geburtsdatum #private Variable, die nicht von außen zugänglich ist

     
     def get_age(self):
        # Berechnung des Alters in Jahren
        days_difference = (date.today() - self.__birthdate).days
        return days_difference // 365  # In ganze Jahre umwandeln 
        

    # Subklasse Subject mit den Attributen Geschlecht, Alter und Maximalpuls
class Subject(Person):
    def __init__(self, first_name, last_name,Geburtsdatum, sex,):
        super().__init__(first_name, last_name,Geburtsdatum) #ruft direkt die Initialisierung der Superklasse auf
        self.sex = sex
        self.age = self.get_age() 
        self.max_hr_bpm = self.estimate_max_hr()

    def estimate_max_hr(self):
        if self.sex == "male":
            return 223 - 0.9 * self.age
        elif self.sex == "female":
            return 226 - 1.0 * self.age
        else:
            return float(input("Enter maximum heart rate: "))
        
    # Subklasse Supervisor mit den Attributen Vorname und Nachname  
class Examiner(Person):
    def __init__(self, first_name, last_name, Geburtsdatum): 
        super().__init__(first_name, last_name,Geburtsdatum) #ruft direkt die Initialisierung der Superklasse auf

class Experiment:
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def add_subject(self, subject):
        self.subject = subject

    def add_examiner(self, examiner):
        self.examiner = examiner

    def __str__(self):
        return (
            f"Experiment: {self.name} am {self.date}\n"
            f"Subject: {self.subject.first_name} {self.subject.last_name}, "
            f"Alter: {self.subject.age}, Geschlecht: {self.subject.sex}, "
            f"Max HR: {self.subject.max_hr_bpm}\n"
            f"Examiner: {self.examiner.first_name} {self.examiner.last_name}"
        )