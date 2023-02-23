# GPA formula = SUM(grade * hours_per_subject)/ total_hours
# Declare variables
grade1 = 0
grade2 = 0
grade3 = 0
hours_per_subject = 0
total_hours = 0
grade_point = 0
GPA = 0

# Get grades and credit hours for three subjects
grade1 = float(input("Enter score for Subject 1: "))
hours_per_subject = float(input("Enter credit hours for Subject 1: "))
grade_point = grade1 * hours_per_subject
total_hours = hours_per_subject

grade2 = float(input("Enter score for Subject 2: "))
hours_per_subject = float(input("Enter credit hours for Subject 2: "))
grade_point += grade2 * hours_per_subject
total_hours += hours_per_subject

grade3 = float(input("Enter score for Subject 3: "))
hours_per_subject = float(input("Enter credit hours for Subject 3: "))
grade_point += grade3 * hours_per_subject
total_hours += hours_per_subject

# Calculate GPA
GPA = grade_point / total_hours

# Output the result
print("The student GPA is: ", GPA)

#
#
#
#
#
# or a bit optimised version:
grade1 = float(input("Enter score for Subject 1: "))
hours_per_subject1 = float(input("Enter credit hours for Subject 1: "))
grade2 = float(input("Enter score for Subject 2: "))
hours_per_subject2 = float(input("Enter credit hours for Subject 2: "))
grade3 = float(input("Enter score for Subject 3: "))
hours_per_subject3 = float(input("Enter credit hours for Subject 3: "))

total_hours = hours_per_subject1 + hours_per_subject2 + hours_per_subject3
grade_point = (grade1 * hours_per_subject1) + (grade2 * hours_per_subject2) + (grade3 * hours_per_subject3)
GPA = grade_point / total_hours

print("The student GPA is:", GPA)
