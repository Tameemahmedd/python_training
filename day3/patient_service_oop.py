from patient import Patient

class Patient_service:
    def __init__(self):
        self.patients = list()

    def patient_add(self, id, name):
        patient = Patient(id, name)
        self.patients.append(patient)
        print('Patient is created')

    def patient_remove(self, id):
        for p in self.patients:
            if p.id == id:
                patient=p
        # patient = (p for p in self.patients if p.id == id)
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        print(patient)
        if input('Are you sure to delete (Yes/No): ').lower() == 'yes':
            self.patients.remove(patient)
            print(f'Patient with id = {id} deleted')

    def list_patients(self):
        # for id in self.patients:
        for p in self.patients:
            print(p.id, p.name)

    def list_patient_by_id(self, id):
        for p in self.patients:
            if p.id == id:
                patient=p
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        print(patient.id, patient.name)

    def patient_update(self, id):
        for p in self.patients:
            if p.id == id:
                patient=p
        if patient == None:
            print(f'Patient with id = {id} not found')
            return
        new_name = input(f'Enter new name of the patient {patient.name}: ')
        patient.name = new_name
        print('Patient update completed')