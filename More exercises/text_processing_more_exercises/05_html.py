title = ['<h1>', f'    {input()}', '</h1>']
content = ['<article>', f'    {input()}', '</article>']
comment_input = input()
comment = []
while comment_input != 'end of comments':
    comment.append('<div>')
    comment.append(f'    {comment_input}')
    comment.append('</div>')
    comment_input = input()

for item in title:
    print(item)
for item in content:
    print(item)
for item in comment:
    print(item)