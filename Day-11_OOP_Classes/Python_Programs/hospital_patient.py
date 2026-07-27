# Program 12: Hospital patient class
class Patient:
    def __init__(self, name, disease):
        self.name = name
        self.disease = disease

    def info(self):
        print(self.name, self.disease)

Patient("Rani", "Flu").info()
