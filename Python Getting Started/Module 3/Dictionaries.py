## DICTIONARIES ##
'''
One can use Dictionaries to store key-value pairs.
"Keys" are akin to variable names
"Values" are their respective values
'''
first_pick = {                                # Defines one item in dict
    "Name": "Zion Williamson",
    "School": "Duke",
    "Draft Team": "New Orleans Pelicans",
    "Draft Slot": 1
}
print(first_pick)

''' To define multiple items: '''
draft_info = [                              # Creates a list of dict's
    {"Name": "Zion Williamson",
     "School": "Duke",
     "Draft Team": "New Orleans Pelicans",
     "Draft Slot": 1},
    {"Name": "Ja Morant",
     "School": "Murray St",
     "Draft Team": "Memphis Grizzlies",
     "Draft Slot": 2},
    {"Name": "RJ Barrett",
     "School": "Duke",
     "Draft Team": "New York Knicks",
     "Draft Slot": 3}
]
print(draft_info)

''' To get data out of a dictionary '''
print(first_pick["Name"])
print(first_pick.get("Position", "Unknown"))
print(first_pick.keys())        # Returns all keys in dict
print(first_pick.values())      # Returns all values in dict
del first_pick["School"]        # Deletes the key-value pair for "School"
print(first_pick.keys())
print(first_pick.values())
