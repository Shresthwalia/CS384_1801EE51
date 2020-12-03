import tutorial01 as A1

actual_answers = [9, 12, 80, 5, 0.333,[2, 6, 18, 54, 162],[2, 6, 10, 14, 18],[1.0, 0.5, 0.333, 0.25, 0.2]]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.multiply(10, 8)
student_answers.append(test_case_3)

test_case_4 = A1.divide(10, 2)
student_answers.append(test_case_4)

test_case_5 = A1.power(3 , -1)
student_answers.append(test_case_5)

gp = A1.printGP(2, 3, 5) 
gp = list(gp) 
student_answers.append(gp)

ap =A1.printAP(2,4,5)
ap =list(ap)
student_answers.append(ap)

hp =A1.printHP(1,1,5)
hp =list(hp)
student_answers.append(hp)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")
