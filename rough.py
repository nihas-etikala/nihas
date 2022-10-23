# n = int(input('number:'))
# N = 0
# marks_list = []
# m = set()
# names = []
# while 2 * n > N:
#     name = input('name:')
#     marks = float(input('marks'))
#     m.add(marks)
#     marks_list.append([name, marks])
#     N += 2
# t = list(m)
# t.sort()
# for a in marks_list:
#     if a[1] == t[1]:
#         names.append(a[0])
# names.sort()
# for b in names:
#     print(names)
# ------------------------------------------------------------
# n = int(input())
# N = 0
# marks_list = {}
# while N < n:
#     person_marks = input()
#     N += 1
#     marks = person_marks.split(' ')
#     marks_list[marks[0]] = [marks[1], marks[2], marks[3]]
# name = input()
# mark = marks_list.get(name)
# average =(int(mark[0]) + int(mark[1]) + int(mark[2])) / 3
# print('%.2f' % average)
# ---------------------------------------------------------------------
# def is_leap(year):
#     year_is_leap = False
#     if year % 4 == 0:
#         year_is_leap = True
#         if year % 100 == 0:
#             year_is_leap = False
#             if year % 400 == 0:
#                 year_is_leap = True
#             else:
#                 year_is_leap = False
#         else:
#             year_is_leap = True
#     return year_is_leap
#
#
# input_year = int(input())
# print(is_leap(input_year))
# -------------------------------------------------------------------------------------
#
# def is_prime(number):
#     for divisors in range(2, int((number ** (1 / 2) + 1))):
#         if number % divisors == 0 and number / divisors != 1:
#             return False
#     return True
#
#
# print(is_prime(13))
# ---------------------------------------------------------------------
# def addf(number):
#     xq = input()
#     print(xq)
#     return 3+number
# a = print('3')
# print(type(32222222222222222222222222222222222222222222222222222222222222))
# b = print(a)
# print(b)
#
#
# print(print(print('3')))


# x = addf(addf(addf(5)))
# print(x)
# -----------------------------------------------------------------------------------
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# sample_list = []
# listx = []
# listy = []
# listz = []
# a = range(0, (x + 1))
# b = range(0, (y + 1))
# c = range(0, (z + 1))
# for e in a:
#     listx.append(e)
# for f in b:
#     listy.append(f)
# for g in c:
#     listz.append(g)
# for p in listx:
#     for q in listy:
#         for r in listz:
#             sample_list.append([p, q, r])
# sample_list2 = sample_list.copy()
# for each_list in sample_list:
#     # print(each_list)
#     h = 0
#     for numbers in range(0, 3):
#         h += each_list[numbers]
#         # print(h)
#     if h == n:
#         sample_list2.remove(each_list)
#
# print(sample_list2)
# -------------------------------------------------------
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# sample_list = [[i, j, k ] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
# final_list = [nihas for nihas in sample_list if sum(nihas) == n]
# print(sample_list)
# print(final_list)
# -------------------------------------------------------
# english_nos = int(input())
# e_subscriptions = input()
# e_subscriptions.split()
# english_set = set(map(int, e_subscriptions.split()))
# french_nos = int(input())
# f_subscriptions = input()
# french_set = set(map(int, f_subscriptions.split()))
# print(len(english_set | french_set))
#
# ---------------------------------------------------------------------------
# def change_case(text):
#     sample_text = ''
#     for letters in text:
#         if letters.isupper():
#             sample_text = sample_text + letters.lower()
#         else:
#             sample_text = sample_text + letters.upper()
#     return sample_text
#
#
# print(change_case(text=input()))
#
# ------------------------------------------------------------------
# text = input()
# print('-'.join(text.split()))
# ---------------------------------------------------------------
# def full_name_greeting(first_name, last_name):
#     print(f'Hello {first_name} {last_name}! You just delved into python')
#
#
# first = input()
# last = input()
# full_name_greeting(first, last)
# ---------------------------------------------------------------------
# def string_mutate(string, index, text):
#     a = list(string)
#     a[index] = text
#     sample_string = ''
#     for letters in a:
#         sample_string += letters
#     return sample_string
#
#
# string = input()
# [index, text] = input().split(' ')
# print(string_mutate(string, int(index), text))
# ---------------------------------------------------------------------
# def count_substring(string, sub_string):
#     string_copy = string
#     a = len(sub_string)
#     b = 0
#     count = 0
#     while b <= (len(string) - a):
#         if string_copy[0: a] == sub_string:
#             count += 1
#         b += 1
#         string_copy = string_copy[1:]
#     return count
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)
# -------------------------------------------------------------------------
from itertools import combinations
string = 'banana'
lista = ['b', 'a', 'n', 'a', 'n', 'a']
perms = combinations(lista)
for lists in perms:
    print(''.join(lists))
# order_of_permutation = 1
# permutation_list = []
# while order_of_permutation <= len(string):
#     permutations(lista)
------------------------------------------------------------
print('new change')
#
print( 'new change 2')
print('dffvav')