N = int(input())

book_dict = {}

for i in range(N):
    book_nm = input()
    if book_nm not in book_dict:
        book_dict[book_nm] = 1
    else:
        book_dict[book_nm] += 1

sorted_list = sorted(book_dict.items(), key=lambda item: (-item[1], item[0]))

print(sorted_list[0][0])

