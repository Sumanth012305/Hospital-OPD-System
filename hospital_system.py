# Hospital OPD System

class Patient:
    def __init__(self, name, age, gender, symptoms):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms

    def display_info(self):
        return f'Patient: {self.name}, Age: {self.age}, Gender: {self.gender}, Symptoms: {self.symptoms}'

class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization

    def display_info(self):
        return f'Doctor: {self.name}, Specialization: {self.specialization}'

class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def display_appointment(self):
        return f'Appointment for {self.patient.name} with Dr. {self.doctor.name} on {self.date_time}'

# Example usage
if __name__ == '__main__':
    patient1 = Patient('John Doe', 30, 'Male', 'Headache')
    doctor1 = Doctor('Dr. Smith', 'Neurologist')
    appointment1 = Appointment(patient1, doctor1, '2023-02-12 10:00:00')
    print(patient1.display_info())
    print(doctor1.display_info())
    print(appointment1.display_appointment())