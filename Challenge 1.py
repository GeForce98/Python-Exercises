#Quincy Asemota
#Weekly Assignment 2 
#Write a program that calculates a student's final grade in this course.

#Tells user about the purpose of the program
print("This program will calculate a students final grade in the course based on the percentage in the syllabus.")
#Prompts user to enter student's grades for assignments
print("Please enter a student's average grade for the weekly assignments, grade for mid-course project and grade for final project.")
#Prompts user to input the student's grades for the assignment
def main():
    weekly_assignments = int(input("Please enter the average grade for the weekly assignments: "))
    project = int(input("Please enter the grade for the mid-course project: "))
    final_project = int(input("Please enter the grade for the final project: "))

    #Calculations for students grades - according to syllabus grading scale
    assignments_total = (weekly_assignments * 0.6) + (project * 0.2) + (final_project * 0.2)

    #Letter grading scale
    if 94 <= assignments_total <=100:
        return "The final grade for this student is a A."
    elif 89 <= assignments_total <= 93:
        return "The final grade for this student is a A-."
    elif 85 <= assignments_total  <= 89:
        return "The final grade for this student is a B+."
    elif 82 <= assignments_total <= 84:
        return "The final grade for this student is a B."
    elif 79 <= assignments_total <= 81:
        return "The final grade for this student is a B-."
    elif 76 <= assignments_total <= 78:
        return "The final grade for this student is a C+."
    elif 73 <= assignments_total <= 75:
        return "The final grade for this student is a C."
    elif 70 <= assignments_total <= 72:
        return "This final grade for this student is a C-."
    elif 67 <= assignments_total <= 69:
        return "The final grade for this student is a D+."
    elif 63 <= assignments_total <= 66:
        return "The final grade for this student is a D."
    elif 60 <= assignments_total <= 63:
        return "The final grade for this student is a D-."
    elif assignments_total < 60:
        return "The final grade for this student is a E."

usergrade = main()
print (usergrade)
            






