student_record = [
    {"Matric_Number": "001", "Name": "Samuel", "Scores": (100, 90, 80)},
    {"Matric_Number": "002", "Name": "David", "Scores": (80, 30, 40)},
    {"Matric_Number": "003", "Name": "Femi", "Scores": (70, 65, 23)},
    {"Matric_Number": "004", "Name": "Toyin", "Scores": (80, 30, 40)},
    {"Matric_Number": "005", "Name": "Natie", "Scores": (80, 30, 40)}
]

student_record.append({"Matric_Number": "006", "Name": "Ebuka", "Scores": (80, 30, 40)})
student_record.append({"Matric_Number": "007", "Name": "Sharon", "Scores": (80, 30, 40)})

student_record.pop(3)
print(student_record)

