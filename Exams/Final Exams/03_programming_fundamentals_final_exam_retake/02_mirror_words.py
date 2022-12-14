import re

text_input = input()
pattern = re.compile(r'(\@|\#)(?P<word_1>[A-Za-z]{3,})\1{2}(?P<word_2>[A-Za-z]{3,})\1')
mirror_words = []
valid = 0

if re.search(pattern, text_input):
    for valid, item in enumerate(re.finditer(pattern, text_input)):
        if item.group('word_1') == item.group('word_2')[::-1]:
            mirror_words.append(f'{item.group("word_1")} <=> {item.group("word_2")}')
    print(f'{valid + 1} word pairs found!')
else:
    print('No word pairs found!')

if mirror_words:
    print('The mirror words are:')
    print(', '.join(mirror_words))
else:
    print('No mirror words!')

# https://judge.softuni.org/Contests/Practice/Index/2307#1

# Problem 2 - Mirror words
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2307#1.
#
# The SoftUni Spelling Bee competition is here. But it`s not like any other Spelling Bee competition out there. It`s different and a lot more fun! You, of course, are a participant, and you are eager to show the competition that you are the best, so go ahead, learn the rules and win!
# On the first line of the input, you will be given a text string. To win the competition, you have to find all hidden word pairs, read them, and mark the ones that are mirror images of each other.
# First of all, you have to extract the hidden word pairs. Hidden word pairs are:
# •	Surrounded by "@" or "#" (only one of the two) in the following pattern #wordOne##wordTwo# or @wordOne@@wordTwo@
# •	At least 3 characters long each (without the surrounding symbols)
# •	Made up of letters only
# If the second word, spelled backward, is the same as the first word and vice versa (casing matters!), they are a match, and you have to store them somewhere. Examples of mirror words:
# #Part##traP# @leveL@@Level@ #sAw##wAs#
# •	If you don`t find any valid pairs, print: "No word pairs found!"
# •	If you find valid pairs print their count: "{valid pairs count} word pairs found!"
# •	If there are no mirror words, print: "No mirror words!"
# •	If there are mirror words print:
# "The mirror words are:
# {wordOne} <=> {wordtwo}, {wordOne} <=> {wordtwo}, … {wordOne} <=> {wordtwo}"
# Input / Constraints
# •	You will recive a string.
# Output
# •	Print the proper output messages in the proper cases as described in the problem description.
# •	If there are pairs of mirror words, print them in the end, each pair separated by ", ".
# •	Each pair of mirror word must be printed with " <=> " between the words.
# Examples
# Input
# @mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r
# Output	Comments
# 5 word pairs found!
# The mirror words are:
# Part <=> traP, leveL <=> Level, sAw <=> wAs	There are 5 green and yellow pairs that meet all requirements and thus are valid.
# #poOl##loOp# is valid and looks very much like a mirror words pair, but it isn`t because the casings don`t match.
# #car#rac# "rac" spelled backward is "car", but this is not a valid pair because there is only one "#" between the words.
# @pack@@ckap@ is also valid, but "ckap" backward is "pakc" which is not the same as "pack", so they are not mirror words.
# Input
# #po0l##l0op# @bAc##cAB@ @LM@ML@ #xxxXxx##xxxXxx# @aba@@ababa@
# Output	Comments
# 2 word pairs found!
# No mirror words!	"xxxXxx" backward is not the same as "xxxXxx"
# @aba@@ababa@ is a valid pair, but the word lengths are different - these are definitely not mirror words
# Input
# #lol#lol# @#God@@doG@# #abC@@Cba# @Xyu@#uyX#
# Output	Comments
# No word pairs found!
# No mirror words!