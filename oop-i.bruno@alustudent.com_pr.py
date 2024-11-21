class Patient:
    # Constructor to initialize a patient object
    def __init__(self, patient_id, name, age, gender, admission_date, condition):
        self.patient_id = patient_id  # Unique ID for the patient
        self.name = name  # Name of the patient
        self.age = age  # Age of the patient
        self.gender = gender  # Gender of the patient
        self.admission_date = admission_date  # Admission date of the patient
        self.condition = condition  # Current medical condition of the patient

    # Method to return a string representation of patient details
    def get_details(self):
        return (f"Patient ID: {self.patient_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Admission Date: {self.admission_date}\n"
                f"Condition: {self.condition}")

# Function to count the number of patients
def count_patients(patient_list):
    return len(patient_list)

# Function to list all patient names
def list_patient_names(patient_list):
    return [patient.name for patient in patient_list]

# Function to print patient details by ID
def print_patient_by_id(patient_list):
    # Ask the user for a patient ID
    patient_id = int(input("Enter the patient ID: "))
    found = False
    for patient in patient_list:
        if patient.patient_id == patient_id:
            print("\nPatient found!\n")
            print(patient.get_details())  # Print the details of the patient
            found = True
            break
    if not found:
        print("Patient not found.")  # If no matching patient ID is found

# Create multiple instances of the Patient class
patient1 = Patient(1, "Alice Smith", 30, "Female", "2024-11-10", "Flu")
patient2 = Patient(2, "Bob Johnson", 45, "Male", "2024-11-15", "Broken Leg")
patient3 = Patient(3, "Carol White", 60, "Female", "2024-11-17", "Hypertension")

# Store patient instances in a list
patients = [patient1, patient2, patient3]

# Example usage:
print(f"Total number of patients: {count_patients(patients)}")
print("\nList of patient names:")
for name in list_patient_names(patients):
    print(name)

# Print patient details by ID
print_patient_by_id(patients)

