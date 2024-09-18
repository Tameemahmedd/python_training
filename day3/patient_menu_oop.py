from patient_service_oop import Patient_service

def menu(services):
    choice = int(input('1:Add 2:Delete 3:Update 4:ListAll 5:Search 6:Exit \nYour choice: '))
    if choice == 1:
        id = int(input('Enter patient id: '))
        name = input('Enter patient name: ')
        services.patient_add(id, name)
    elif choice == 2:
        id = int(input('Enter patient id: '))
        services.patient_remove(id)
    elif choice == 3:
        id = int(input('Enter patient id: '))
        services.patient_update(id)
    elif choice == 4:
        services.list_patients()
    elif choice == 5:
        id = int(input('Enter patient id: '))
        services.list_patient_by_id(id)
    elif choice == 6:
        pass
    else:
        print('Invalid choice enetered')
    return choice

def patient_app():
    service_obj = Patient_service()
    choice = menu(service_obj)
    while choice != 6:
        choice = menu(service_obj)
    print('Thank you being patient')