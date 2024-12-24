from prettytable import PrettyTable

class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = 0
        total_subjects = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_subjects += len(grades)
        return total_grades / total_subjects if total_subjects > 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_grades(self):
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")
        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        print(f"Average Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")

def display_grades_table(tracker):
    table = PrettyTable()
    table.field_names = ["Subject", "Grades", "Average Grade", "Letter Grade"]
    
    for subject, grades in tracker.grades.items():
        average = sum(grades) / len(grades) if grades else 0
        letter_grade = tracker.get_letter_grade(average)
        table.add_row([subject, grades, f"{average:.2f}", letter_grade])
    
    overall_average = tracker.calculate_average()
    overall_letter_grade = tracker.get_letter_grade(overall_average)
    
    print(table)
    print(f"\nOverall Average Grade: {overall_average:.2f}")
    print(f"Overall Letter Grade: {overall_letter_grade}")

def main():
    tracker = StudentGradeTracker()
    while True:
        print("\n1. Add Grade")
        print("2. Display Grades")
        print("3. Display Grades in Table")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            tracker.add_grade(subject, grade)
        elif choice == '2':
            tracker.display_grades()
        elif choice == '3':
            display_grades_table(tracker)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
