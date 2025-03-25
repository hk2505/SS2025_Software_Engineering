from my_functions import estimate_max_hr, build_person, build_experiment

if __name__ == "__main__":

    first_name = input("Vorname des Probanden: ")
    last_name = input("Nachname des Probanden: ")
    sex= input("Geschlecht des Probanden: ")
    age= input ("Alter des Probanden in Jahren: ")
    age_year = int(age)
    age=age_year #In der Funktion build_person wird age ebenfalls nochmal als int benötigt 
    experiment_name= input("Name des Experiments: ")
    date= input("Datum: ")
    supervisor= input("Name des Versuchsleiters:")
    subject= input("ID des Probands: ")

    Proband= build_person(first_name,last_name, sex, age) # in der Funktion wird die estimate_max_hr schon benutzt 
    Experiment= build_experiment(experiment_name,date,supervisor,subject)

    Alle_Daten = {
        "Daten über Proband": Proband, #Max_Puls wird bei build Person aufgelistet und muss daher nicht 2x aufegführt werden 
        "Experiment": Experiment
}

print(Alle_Daten)




