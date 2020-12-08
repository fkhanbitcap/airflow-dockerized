
#
# def minesweeper(matrix):
#     temp_matrix = [""] * len(matrix)
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 'X':
#                 temp_matrix[i] += 'X'
#             if matrix[i][j] == 'O':
#                 temp_var = 0
#                 for m in [i-1,i,i+1]:
#                     for n in [j-1,j,j+1]:
#                         if m >= 0 and m < len(matrix) and n >= 0 and n < len(matrix[0]):
#                             if matrix[m][n] == 'X':
#                                 temp_var += 1
#                 temp_matrix[i] += str(temp_var)
#     for i in temp_matrix:
#         for j in i:
#             print(j+' ', end='')
#         print()
#
# test1 = ["XOOXXXOO", "OOOOXOXX", "XXOXXOOO", "OXOOOXXX", "OOXXXXOX", "XOXXXOXO", "OOOXOXOX", "XOXXOXOX"]
# test2 = ["OOOXXXOXX", "XXXXXXOXX", "XOOXXXXXX", "OOXXOXOXX", "XXXXXXXXX"]
#
# print("test1")
# minesweeper(test1)
# print("\ntest2")
# minesweeper(test2)

# def get_friends(person, rel_list):
#     number_of_friends = 0
#     list_of_friends = []
#     remaining_relations = []
#     for r in rel_list:
#         if person in r:
#             number_of_friends += 1
#             temp = r.split(":")
#             temp.remove(person)
#             list_of_friends.append(temp[0])
#         else:
#             remaining_relations.append(r)
#     for p in list_of_friends:
#         number_of_friends += get_friends(p, remaining_relations)
#     return number_of_friends
#
# def numberOfFriends(rel_list, persons_to_check):
#     for person_in_question in persons_to_check:
#         print(person_in_question, ":", get_friends(person_in_question, rel_list))
#
#
# numberOfFriends(["Anne:Barbara","Barbara:Ivan", "Vinny:Vlad"], ["Anne", "Vinny"])
# print("\n\n")
# numberOfFriends(["Octavia:Zoltan", "Zoltan:Marko", "Marko:Diego", "Diego:Andres"], ["Octavia", "Diego"])

n,m=list(map(int, input().split()))
ns=list(map(int, input().split()))
h=set(map(int, input().split()))
s=set(map(int, input().split()))
