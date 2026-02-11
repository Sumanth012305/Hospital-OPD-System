class Patient:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority

class Bed:
    def __init__(self, bed_number):
        self.bed_number = bed_number
        self.is_occupied = False

class HospitalSystem:
    def __init__(self):
        self.priority_queue = []
        self.beds = {1: Bed(1), 2: Bed(2), 3: Bed(3)}  # Example bed numbers
        
    def admit_patient(self, patient):
        heapq.heappush(self.priority_queue, patient)

    def discharge_patient(self):
        if self.priority_queue:
            patient = heapq.heappop(self.priority_queue)
            print(f'Discharging patient: {patient.name}')
        else:
            print('No patients to discharge')

    def assign_bed(self, patient_name):
        for bed in self.beds.values():
            if not bed.is_occupied:
                bed.is_occupied = True
                print(f'Assigned {patient_name} to bed {bed.bed_number}')
                return
        print('No beds available')

    def show_patients(self):
        print('Current patients in the system:')
        for patient in self.priority_queue:
            print(f'Patient: {patient.name}, Priority: {patient.priority}')

import heapq

if __name__ == '__main__':
    hospital_system = HospitalSystem()
    while True:
        print('\nHospital OPD Management System')
        print('1. Admit Patient')
        print('2. Discharge Patient')
        print('3. Show Patients')
        print('4. Assign Bed')
        print('5. Exit')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            name = input('Enter patient name: ')
            priority = int(input('Enter patient priority (1-5): '))
            patient = Patient(name, priority)
            hospital_system.admit_patient(patient)
        elif choice == '2':
            hospital_system.discharge_patient()
        elif choice == '3':
            hospital_system.show_patients()
        elif choice == '4':
            name = input('Enter patient name for bed assignment: ')
            hospital_system.assign_bed(name)
        elif choice == '5':
            break
        else:
            print('Invalid choice! Please try again.')