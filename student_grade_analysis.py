import json
import functools

class StudentGradeAnalysis:
    
    def __init__(self, file_path):
        self.file_path = file_path
    
    def load_students_grades(self):
        try:
            with open(self.file_path, "r") as file:
               students =  json.load(file)
        except FileNotFoundError:
            students = []
        except json.JSONDecodeError:
            students = []
            print("Error loading json file. Starting with empty lists")
        return students
    
    def input_grades(self,load_file):
        try:
            while True:
                student_name = input("Enter student name: ")
                student_grade = int(input("Enter student grade: "))
                
                student_info = {"name:": student_name, "grade":student_grade}
                load_file.append(student_info)
                try:
                    with open(self.file_path,"w") as file:
                        json.dump(load_file, file, indent=2)
                except FileNotFoundError:
                    print("File not found!")

        except ValueError:
            print("Student grade must be integer!")

instance = StudentGradeAnalysis("students_grades.json")
instance.input_grades(instance.load_students_grades())

