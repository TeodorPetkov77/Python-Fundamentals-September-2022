import re

text_input = re.sub(r'\\n', '', input())

pattern_title = re.compile('(?<=<title>)(\w+\s*)+(?=</title>)')
remove_tags_pattern = re.compile('<[^<>]+>')

print(f'Title: {re.search(pattern_title, text_input).group()}')

text_input = re.sub(r'<title>(\w+\s*)+</title>', '', text_input)

for tag in [x.group() for x in re.finditer(remove_tags_pattern, text_input)]:
    text_input = re.sub(tag, ' ', text_input)

print(f'Content: {text_input.strip().replace("  ", " ")}')

# https://judge.softuni.org/Contests/Practice/Index/1744#4

# 5.	HTML Parser
# Write a program that extracts a title and all the content of a HTML file:
# •	The title should be between the HTML tags <title> and <\title>.
# •	The content should be between the HTML tags <body> and <\body>.
# There might be different HTML tags, which you should ignore:
# •	Each HTML tag is surrounded by the symbols "<" and ">". For example: <body>, <p>, <\html>
# •	You also should ignore the HTML tag "\n"
# Example:
# "<html>\n<head><title>News</title></head>\n<body><p><a href="https://softuni.bg">SoftUni</a>aims to provide free real-world practical\n training for young people who want to turn into\n skillful Python software engineers.</p></body>\n</html>"
# In this example the title is "News" and the content is "SoftUni aims to provide free real-world practical training for young people who want to turn into skillful Python software engineers."
# Input
# •	The input will be read from the console.
# •	The input consists of a single line.
# Output
# •	The content should be a single string.
# •	You should extract only the text without the tags.
# •	When you extract the title and the content, you should print the result in the following format:
# o	"Title: {extracted title}"
# o	"Content: {extracted content}"
#
# Input	Output	Comment
# <html>\n<head><title>Some title</title></head>\n<body>Here<p> is some </p>content <a href="www.somesite.com">\nclick</body>\n</html>	Title: Some title
# Content: Here is some content click	We take the title and ignore all the tags to get the content