import re

test_string = '123abc456789abc123ABC'
pattern = re.compile(r'abc')

# matches = pattern.finditer(test_string)

# for match in matches:
#     print(match)

# match = pattern.match(test_string)
# print(match)

# match = pattern.search(test_string)
# print(match)

# matches = re.findall(pattern, test_string)
# for match in matches:
#     print(match)

# ṃatch object methods
matches = pattern.finditer(test_string)
for match in matches:
    print(match.span(), match.group(),"start :", match.start(),"end :", match.end())