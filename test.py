from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    supervisor = Supervisor("Sophia", "Nowotny")
    subject = Subject("Sophia", "Nowotny", "female", 30)
    subject.estimate_max_hr()
    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)

    print(experiment)
    