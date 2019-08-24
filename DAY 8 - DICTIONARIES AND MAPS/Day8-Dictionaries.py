import sys

# one way to get input:
# n = int(input().strip())
# or, using system library, readline:
print('How many entries?:')
n = int(sys.stdin.readline().strip()) # number of entries

# declaring dictionary
phone_book = dict()
print('Enter the entries. Name <space> Phone number and press enter')
for i in range(n):
    entry = sys.stdin.readline().strip().split(' ')
    phone_book[entry[0]] = entry[1]

print('Query: which name you want to look?:')
query = sys.stdin.readline().strip()
while query:
    if query in phone_book.keys():
        print(query + ' = ' + phone_book.get(query))
    else:
        print('Not found')
    query = sys.stdin.readline().strip()

