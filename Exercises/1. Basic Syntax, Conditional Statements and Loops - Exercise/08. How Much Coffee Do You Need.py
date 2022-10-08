event = str(input())
event_case_fold = event.casefold()
coffees = 0

while event != "END":
    if event_case_fold == "cat" \
            or event_case_fold == "dog" \
            or event_case_fold == "movie" \
            or event_case_fold == "coding":
        if event.isupper():
            coffees += 2
        elif event.islower():
            coffees += 1
    event = str(input())
    event_case_fold = event.casefold()

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)