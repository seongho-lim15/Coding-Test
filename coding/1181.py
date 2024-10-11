N = int(input())
word_arr_list = [[] for _ in range(51)]

for _ in range(N):
    input_word = input()
    word_len = len(input_word)

    if input_word not in word_arr_list[word_len]:
        word_arr_list[word_len].append(input_word)

for word_arr in word_arr_list:
    word_arr.sort()
    for word in word_arr:
        print(word)

# N = int(input())
# word_arr_list = [set() for _ in range(N + 1)]
#
# for _ in range(N):
#     input_word = input()
#     word_len = len(input_word)
#
#     # if input_word not in word_arr_list[word_len]:
#     word_arr_list[word_len].add(input_word)
#
# for word_arr in word_arr_list:
#     word_arr = sorted(list(word_arr))
#     for word in word_arr:
#         print(word)

