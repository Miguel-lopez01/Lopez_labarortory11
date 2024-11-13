grades = []
total = 0 
passing_count = 0
passing_percent = 0

print("enter 5 student grade between 40-100:")
for i in range(5):
    attempts = 0
    while True:
        try:
            grade = float(input(f"student{i+1}: "))
            if 40 <= grade <= 100:
               grades.append(grade)
               total += grade
               if grade >= 75:
                  passing_count += 1
               break
            else:
                print("please enter a grade between 40 - 100")
        except ValueError:
            print("invalid input. enter a number and try again")
            attempts += 1 
            if attempts >=3:
                print ("too many attempts")
                break

average_grade = total /5
passing_percent = (passing_count / 5) *  100

print(f"grades entered: {grades}")
print("average grades:", average_grade)
print("number of students that has a passing grade:", passing_count)
print("passing percent:", passing_percent, "%")