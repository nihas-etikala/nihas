import string
word = input().rstrip()
length = len(word)

vowels = {i : False for i in string.ascii_uppercase}

for i in "AEIOU":
    vowels[i] = True

stuart_points = 0
bob_points = 0

for start in range(length):
    if vowels[word[start]]:
       bob_points += length - start
    else:
       stuart_points += length - start

if stuart_points > bob_points:
    print("Stuart", stuart_points)
elif stuart_points < bob_points:
    print("Kevin", bob_points)
else:
    print("Draw")


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
# def minnion_game(main_string):
#     from itertools import combinations
#     # kevin - vowels | stuart - consonants
#     kevin_score = 0
#     stuart_score = 0
#     kevin_list = []
#     stuart_list = []
#     vowels = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
#     range_for_word = range(0, len(main_string) + 1)
#     sample_list1 = []
#     for numbers in range_for_word:
#         sample_list1.append(numbers)
#     sample_list2 = []
#     perms = combinations(sample_list1, 2)
#     for tupls in perms:
#         u, v = tupls
#         sample_list2.append(main_string[u: v])
#     all_sub_strings = list(set(sample_list2))
#     # print(all_sub_strings)
#     for sub_strings in all_sub_strings:
#         if sub_strings[0] in vowels:
#             kevin_list.append(sub_strings)
#         else:
#             stuart_list.append(sub_strings)
#     # print(kevin_list)
#     # print(stuart_list)
#     for vowel_words in kevin_list:
#         kevin_score += count_substring(main_string, vowel_words)
#     for consonant_words in stuart_list:
#         stuart_score += count_substring(main_string, consonant_words)
#     if stuart_score > kevin_score:
#         print('Stuart ' + str(stuart_score))
#     elif stuart_score < kevin_score:
#         print('Kevin ' + str(kevin_score))
#     else:
#         print('Draw')
# minnion_game(input())