import sqlite3
from datetime import date

connection = sqlite3.connect(":memory:")
connection.execute("PRAGMA foreign_keys = ON")
cursor = connection.cursor()

cursor.executescript("""
CREATE TABLE Doctors (
    doctor_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    specialty TEXT NOT NULL
);

CREATE TABLE Patients (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL
        CHECK (date(date_of_birth) IS NOT NULL)
);

CREATE TABLE Appointments (
    appointment_id INTEGER PRIMARY KEY,
    doctor_id INTEGER NOT NULL,
    patient_id INTEGER NOT NULL,
    appointment_date TEXT NOT NULL
        CHECK (date(appointment_date) IS NOT NULL),
    notes TEXT,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
);

INSERT INTO Doctors (name, specialty)
VALUES ('Dr. Meera Rao', 'Cardiology'), ('Dr. John Lee', 'Neurology');

INSERT INTO Patients (name, date_of_birth)
VALUES ('Asha Kumar', '2000-04-12'), ('Ravi Shah', '1998-09-21');

INSERT INTO Appointments (doctor_id, patient_id, appointment_date, notes)
VALUES
    (1, 1, '2026-01-15', 'Routine checkup'),
    (1, 2, '2026-02-10', 'Follow-up'),
    (2, 1, '2026-02-18', 'Consultation');
""")

# List all appointments for a specific doctor
doctor_id = 1
cursor.execute("""
    SELECT a.appointment_date, p.name AS patient, a.notes
    FROM Appointments AS a
    JOIN Patients AS p ON p.patient_id = a.patient_id
    WHERE a.doctor_id = ?
    ORDER BY a.appointment_date
""", (doctor_id,))
print("Doctor appointments:", cursor.fetchall())

# Retrieve appointment history for a patient
patient_id = 1
cursor.execute("""
    SELECT a.appointment_date, d.name AS doctor, d.specialty, a.notes
    FROM Appointments AS a
    JOIN Doctors AS d ON d.doctor_id = a.doctor_id
    WHERE a.patient_id = ?
    ORDER BY a.appointment_date
""", (patient_id,))
print("Patient history:", cursor.fetchall())

# Count patients treated by each doctor
cursor.execute("""
    SELECT d.name, COUNT(DISTINCT a.patient_id) AS patient_count
    FROM Doctors AS d
    LEFT JOIN Appointments AS a ON a.doctor_id = d.doctor_id
    GROUP BY d.doctor_id, d.name
    ORDER BY d.name
""")
print("Patients per doctor:", cursor.fetchall())

connection.close()