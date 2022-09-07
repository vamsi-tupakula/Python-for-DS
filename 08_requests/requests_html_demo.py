from requests_html import HTML

with open('sample.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# match = html.find('title')
# print(match[0].html)
# print(match[0].text)

# matches = html.find('div')
# for match in matches:
#     print(match.text)

# find_first = html.find('p', first=True)
# print(find_first.html)

# find elements based on classes and id's
heading__1 = html.find('#h_2__1')
print(heading__1[0].text)

paras = html.find('.paragraph')
print(paras[1].text)