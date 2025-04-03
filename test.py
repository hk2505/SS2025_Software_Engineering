from my_classes import Subject, Examiner, Experiment

if __name__ == "__main__":

    # Erstellen eines Prüfers und einer Testperson
    examiner = Examiner("Hannah", "Kleutgens", "26.04.2005")  # keine Geburtsdaten notwendig
    subject = Subject("Max", "Müller", "male", 25, "24.03.2000")  # Alter wird direkt übergeben

    # Experiment erstellen
    experiment = Experiment("Leistungstest", "2025-04-03")
    experiment.add_subject(subject)
    experiment.add_examiner(examiner)

    # Ergebnis ausgeben
    print(experiment)
