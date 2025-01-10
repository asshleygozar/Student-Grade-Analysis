from functools import reduce
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
                print("Press 1 to exit")
                student_name = input("Enter student name: ")
                student_grade = int(input("Enter student grade: "))

                if student_grade == "q":
                    instance.results()
                    break
                else:
                    student_info = {"name": student_name, "grade":student_grade}
                    load_file.append(student_info)
                    try:
                        with open(self.file_path,"w") as file:
                            json.dump(load_file, file, indent=2)
                    except FileNotFoundError:
                        print("File not found!")
        except ValueError:
            print("Student grade must be integer!")

    def student_grades(grades):

        data = instance.load_students_grades()
        total_grades = list(map(lambda x:"Name: " + str(x["name"]) + " Grade: "+str(x["grade"]) + "%", data))
        print("Students grades")

        for grade in total_grades:
            print(grade)
    
    def passed_students(grades):

        data = instance.load_students_grades()
        passed_grades = list(filter(lambda y: y["grade"] >= 75, data))

        for passed in passed_grades:
            print(f"Name: {passed["name"]} Grade: {passed["grade"]} Status: Passed!")

    def failed_students(grades):

        data = instance.load_students_grades()
        failed_grades = list(filter(lambda z: z["grade"] <75, data))

        for failed in failed_grades:
            print(f"Name: {failed["name"]} Grade: {failed["grade"]} Status: Failed!")

    def average_of_whole_class(grades):

        data = instance.load_students_grades()

        total_score = reduce(lambda x, y: x + y["grade"], data,0)
        average = total_score / len(data)
        print(f"Average grade of the class: {average}")

    def results():

        load = instance.load_students_grades()
        StudentGradeAnalysis.student_grades(load)
        StudentGradeAnalysis.passed_students(load)
        StudentGradeAnalysis.failed_students(load)
        StudentGradeAnalysis.average_of_whole_class(load)  

instance = StudentGradeAnalysis("students_grades.json")
StudentGradeAnalysis.results()



