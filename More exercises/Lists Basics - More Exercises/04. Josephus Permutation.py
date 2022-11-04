people = list(map(int, input().split(" ")))
index = 0
position = 1
executed_list = []
k = int(input())
while people:
    if index > len(people) - 1:
        index = 0
    if position % k == 0:
        executed_list.append(people.pop(index))
        position += 1
        continue
    position += 1
    index += 1

print(f"[{','.join(list(map(str, executed_list)))}]")

# https://judge.softuni.org/Contests/Practice/Index/1726#3

# 4.	Josephus Permutation
# This problem takes its name from arguably the most important event in the life of the ancient historian Josephus. According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. Refusing to surrender to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man of every three until one last man was left (and that it was supposed to kill himself to end the act). Well, Josephus and another man were the last, and, as we now know every detail of the story, you may have correctly guessed that they did not precisely follow through with the original idea.
# You are now to create a program that prints a Josephus permutation, receiving two lines of code:
# •	the list itself - numbers separated by a single space representing the people in the circle
# •	a number k
# People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and proceeds from left to right. After a specified number of people are skipped, the k person is executed. The procedure is repeated with the remaining people, starting with the next person, going in the same direction, and skipping the same number of people until no one remains.
# Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"
# Example
# Input	Output	Comment
# 1 2 3 4 5 6 7
# 3	[3,6,2,7,5,1,4]	[1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out and goes into the result [3]
# [1,2,4,5,7] => 6 is counted out and goes into the result [3,6]
# [1,4,5,7] => 2 is counted out and goes into the result [3,6,2]
# [1,4,5] => 7 is counted out and goes into the result [3,6,2,7]
# [1,4] => 5 is counted out and goes into the result [3,6,2,7,5]
# [4] => 1 is counted out and goes into the result [3,6,2,7,5,1]
# [] => 4 is counted out and goes into the result [3,6,2,7,5,1,4]
# 10 5 65 104 1 0 2
# 8	[10,65,0,1,5,2,104]