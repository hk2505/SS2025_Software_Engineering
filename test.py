from datetime import datetime
from my_classes import Subject, Examiner, Experiment

if __name__ == "__main__":
    examiner_birthdate = datetime.strptime("26.04.2005", "%d.%m.%Y").date() # Umwandlung des Geburtsdatums in ein Datumsobjekt
    subject_birthdate = datetime.strptime("24.03.2000", "%d.%m.%Y").date()

    examiner = Examiner("Hannah", "Kleutgens", examiner_birthdate)
    subject = Subject("Max", "Müller", subject_birthdate, "male")

    # Experiment erstellen
    experiment = Experiment("Leistungstest", "2025-04-03")
    experiment.add_subject(subject)
    experiment.add_examiner(examiner)

    print(experiment)