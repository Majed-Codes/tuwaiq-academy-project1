# Create the Diseases class
class Diseases:

    # Initialize the patient information
    def __init__(self, patient_id, name, age, gender, answers):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.answers = answers

    # Ask the patient about different symptoms
    def display_questions(self):
        print("Disease Assessment")

        # Store the patient's answer as True or False
        self.answers["fever"] = input("Do you have a fever? (yes/no): ").lower() == "yes"
        self.answers["cough"] = input("Do you have a cough? (yes/no): ").lower() == "yes"
        self.answers["headache"] = input("Do you have a headache? (yes/no): ").lower() == "yes"
        self.answers["fatigue"] = input("Do you feel tired or weak? (yes/no): ").lower() == "yes"
        self.answers["pain"] = input("Do you have body pain? (yes/no): ").lower() == "yes"

    # Display patient information and assessment result
    def display_info(self):
        print("\nAssessment completed")

        # Display basic patient information
        print("\nPatient Information")
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

        print("\nSymptoms")

        # Get the symptoms where the answer is True
        symptoms = [
            symptom for symptom, answer in self.answers.items() if answer
        ]

        # Display the reported symptoms
        if symptoms:
            for symptom in symptoms:
                print(f"- {symptom}")
        else:
            print("No symptoms selected.")

        print("\nAssessment Result")

        # Determine the result based on the number of symptoms
        if len(symptoms) >= 3:
            print("Several symptoms were reported. Please consult a healthcare professional.")
        elif len(symptoms) > 0:
            print("Some symptoms were reported.")
        else:
            print("No symptoms were reported.")


# Create a patient object
patient = Diseases(
    patient_id=1,
    name="Mohammed",
    age=27,
    gender="Male",
    answers={}
)

# Ask the patient about symptoms
patient.display_questions()

# Display the assessment result
patient.display_info()