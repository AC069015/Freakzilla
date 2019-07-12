'''
Data Types:

1. Integers (int)
2. Floats (float)
3. Strings (str)
4. Boolean
5. None

'''
# 1. Integers
rockets_games = 93
type(rockets_games)

# 2. Floats
harden_ppg = 35.4
type(harden_ppg)

def total_points(games, ppg):  # Python will allow both Integer and Float values
    return games*ppg

total_points(rockets_games, harden_ppg)

# 3. Strings
goat = 'lebron'         
goat == "lebron"
goat == """lebron"""    # Can use ', " or """ to signal something as a string

## Useful String Functions ##
goat.capitalize()
goat.replace("n", " ")
goat.isalpha()  # Are all characters letters?

goat_number = "6"
goat_number.isdigit()   # Are all characters integers? Useful when converting to int

goat_info = "lebron_james, 6, Los Angeles Lakers"
goat_info.split(sep = ",")  # Splits a string into a list

### String Format Function
star = "Kawhi Leonard"
co_star = "Paul George"
"Hey {1}, this is {0}. Want to meet up in LA?".format(star, co_star)
# a quicker way, called "String Interpolation" #
f"Hey {co_star}, this is {star}. Want to meet up in LA?"

# 4. Boolean - refers to a TRUE/FALSE value
giannis_mvp = True  # Note that you need a capital T/F to designate as True/False
bucks_champs = False
## Booleans are useful for setting conditions in loops ##
## Convert to integer or string:
int(giannis_mvp)
int(bucks_champs)
str(giannis_mvp)


# 5. None - similar to "NULL" in other languages

seattle_team = None # Not associated with any value; a placeholder variable
                    # Evaluates to FALSE in an IF statement
type(seattle_team)

