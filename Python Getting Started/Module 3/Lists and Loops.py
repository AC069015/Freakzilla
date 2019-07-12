## LISTS and LOOPS ##

''' Holds multiple objects under one variable'''

''' To define a list: '''
roy_candidates = []     # empty list

roy_candidates = ["Zion Williamson", "Ja Morant", "RJ Barrett"]

''' To access an element in a list, reference its "index" '''
print(f"The Favorite for ROY is {roy_candidates[0]}.")  # Index starts at 0
print(f"{roy_candidates[1]} is a highlight waiting to happen!")
print(f"The Knicks' consolation prize is {roy_candidates[2]}.")
    # to reference the last item in a list, type "roy_candidates[-1]"

''' To change or add a list element '''
roy_candidates.append("Cameron Johnson")    # can't do "roy[3] = "Cam J."
print(roy_candidates)
roy_candidates[3] = "Deandre Hunter"
print(roy_candidates)

''' To check to see if item is in a list '''
for_real = "Cameron Johnson" in roy_candidates
print(for_real)

''' See how many items are in a list '''
short_list = len(roy_candidates)
print(short_list)

''' To delete an element in a list '''
del roy_candidates[3]
print(roy_candidates)

# List Slicing: obtain partial elements in a list #
roy_favorite = roy_candidates[:-2]  # Use ":"; does not modify list
print(roy_favorite)

## LOOPS ##
'''
Print all elements in a list --> Use a loop
There are two kinds of loops: "for" loops and "while" loops
'''

''' A "for" loop example '''
for rookie in roy_candidates:   # "for" item "in" list:
    print(f"{rookie} is a leading candidate for Rookie of the Year.")

''' Breaking a loop:
"Breaking" tells the loop to stop running, even if it hasn't reached
the end of it's index
'''
for rookie in roy_candidates:
    if rookie == "Ja Morant":
        print("That's the dude with the best flow, right there!")
        break
    print("Not the dude I'm looking for.")

''' Continuing a loop:
"Continue" tells the loop to skip any action during an iteration
of the loop if it meets a certain condition, while continuing to
progress through the rest of the loop.
'''
for rookie in roy_candidates:
    if rookie == "Ja Morant":
        continue
    print(f"{rookie} is one of the Duke guys.")

''' A "while" loop example ''' ## "while" loops are prone to infinite loops
rookie = 0          # Need to initalize
while rookie <= 2:
    print(f"{roy_candidates[rookie]} is a Rookie of the Year contender.")
    rookie += 1     # "+=" means "rookie = rookie + 1"
