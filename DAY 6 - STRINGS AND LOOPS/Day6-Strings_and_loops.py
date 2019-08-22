print('How Many Words?:\n')
test_cases = int(input())

# iterating loop
for i in range(0, test_cases):
    print('Enter a Word:\n')
    test_string = input()
    even_index_char = ''
    odd_index_char = ''

    for j in range(0, len(test_string)):
        if j % 2 == 0:
            even_index_char += test_string[j]
        else:
            odd_index_char += test_string[j]
    print('{} {}'.format(even_index_char, odd_index_char))

