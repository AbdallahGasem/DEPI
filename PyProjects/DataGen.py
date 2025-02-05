import random
from datetime import datetime, timedelta

# Helper function to generate random dates
def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return (start + timedelta(seconds=random_seconds)).strftime('%Y-%m-%d %H:%M:%S')

# Generate 20 patients
patients = []
names = ["John Doe", "Jane Smith", "Alice Johnson", "Robert Brown", "Emily Davis", "Michael Wilson", "Sarah Miller", "David Taylor", "Jessica Anderson", "Daniel Thomas", "Laura Moore", "Kevin White", "Samantha Harris", "Chris Martin", "Rachel Thompson", "Andrew Garcia", "Sophia Martinez", "Brian Robinson", "Olivia Clark", "James Lewis"]

for i in range(20):
    patient_id = i + 1
    name = names[i % len(names)]
    gender = random.choice(['M', 'F'])
    age = random.randint(18, 80)
    contact_info = f"+20100{random.randint(1000000, 9999999)}"
    admission_date = random_date(datetime(2023, 1, 1), datetime(2024, 12, 31))
    patients.append((patient_id, name, gender, age, contact_info, admission_date))

# Generate 50 doctors
doctors = []
doctor_names = ["Dr. Smith", "Dr. Johnson", "Dr. Williams", "Dr. Jones", "Dr. Brown", "Dr. Davis", "Dr. Miller", "Dr. Wilson", "Dr. Moore", "Dr. Taylor", "Dr. Anderson", "Dr. Thomas", "Dr. Jackson", "Dr. White", "Dr. Harris", "Dr. Martin", "Dr. Thompson", "Dr. Garcia", "Dr. Martinez", "Dr. Robinson", "Dr. Clark", "Dr. Rodriguez", "Dr. Lewis", "Dr. Lee", "Dr. Walker", "Dr. Hall", "Dr. Allen", "Dr. Young", "Dr. Hernandez", "Dr. King", "Dr. Wright", "Dr. Lopez", "Dr. Hill", "Dr. Scott", "Dr. Green", "Dr. Adams", "Dr. Baker", "Dr. Gonzalez", "Dr. Nelson", "Dr. Carter", "Dr. Mitchell", "Dr. Perez", "Dr. Roberts", "Dr. Turner", "Dr. Phillips", "Dr. Campbell", "Dr. Parker", "Dr. Evans", "Dr. Edwards", "Dr. Collins"]

specializations = ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Dermatology", "Radiology", "Oncology", "Psychiatry", "Urology", "Gastroenterology"]
departments = ["General", "Emergency", "Surgery", "ICU", "Outpatient"]

for i in range(50):
    name = doctor_names[i % len(doctor_names)]
    contact_info = f"+20100{random.randint(1000000, 9999999)}"
    specialization = random.choice(specializations)
    department = random.choice(departments)
    doctors.append((name, contact_info, specialization, department))

# Generate 20 appointments
appointments = []

for i in range(30):
    appointment_id = i + 1
    patient_id = random.randint(1, 20)
    doctor_id = random.randint(1, 50)
    appointment_date = random_date(datetime(2024, 1, 1), datetime(2025, 1, 1))
    status = random.choice(["Scheduled", "Completed", "Cancelled"])
    appointments.append((appointment_id, patient_id, doctor_id, appointment_date, status))

# Output generated data
print("Patients:", patients)
print("Doctors:", doctors)
print("Appointments:", appointments)
