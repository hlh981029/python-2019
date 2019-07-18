# score     grade
# 0-59      E
# 60-69     D
# 70-79     C
# 80-89     B
# 90-100    A


# scores = [0,10,20,30,40,50,60,70,80,90,100]
# grades = [0,0,0,0,0]


# test = 'A'
# print(test)


# count = 0
# while count <= 10:
#     score = scores[count]
#     print('current score: ')
#     print(score)
#     print('current grade: ')
#     grade = ''
#     if score < 0 or score > 100:
#         print('error')
#     else:
#         if score <= 59:
#             grade = 'E'
#         elif score <= 69:
#             grade = 'D'
#         elif score <= 79:
#             grade = 'C'
#         elif score <= 89:
#             grade = 'B'
#         else:
#             grade = 'A'
#         print(grade)
#     count = count + 1


# for score in scores:
#     print('current score: ')
#     print(score)
#     print('current grade: ')
#     grade = ''
#     if score < 0 or score > 100:
#         print('error')
#     else:
#         if score <= 59:
#             grade = 'E'
#             grades[4] += 1
#         elif score <= 69:
#             grade = 'D'
#             grades[3] += 1
#         elif score <= 79:
#             grade = 'C'
#             grades[2] += 1
#         elif score <= 89:
#             grade = 'B'
#             grades[1] += 1
#         else:
#             grade = 'A'
#             grades[0] += 1
#
#         print(grade)
# for grade in grades:
#     print(grade)