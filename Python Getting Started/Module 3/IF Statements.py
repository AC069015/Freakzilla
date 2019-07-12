# IF Statements #

kawhi_team = "Los Angeles Clippers"
kd_team = "Brooklyn Nets"
if kawhi_team == "Toronto Raptors": # Need ":" to close the expression
    print("Kawhi came back!")       # "==" checks equality
else:
    print("Still worth it!")        # Indentation used to denote placement
                                    # inside of a code block, instead of {}
## Not If Statements ##
if kawhi_team != "Toronto Raptors":     # "!=" reverses the IF conditional
    print("An unprecedented move my the reigning Finals MVP!")

## Multiple If Conditions ##
        # using "and"
if kawhi_team == "Los Angeles Clippers" and kd_team == "Brooklyn Nets":
    exclamation = f"The {kawhi_team} and the {kd_team}! Wow!"
    print(exclamation)  # Using String Interpolation

        # using "or"
if kawhi_team == "Toronto Raptors" or kd_team == "Brooklyn Nets":
    print("The Eastern Conference gonna have some competition next season!")
    
## Truthy and Falsy Values ##
if kawhi_team:      # can check if a value is defined or not zero
    print("No longer a free agent")

    # A truthy value is any defined value other than zero or an empty string
    # (whether string or integer).
    # As long as variable has some sort of value, it evaluates to true
    # in the setup shown above (in the IF conditional)

## Using Boolean and None values ##
giannis_mvp = True
bucks_champs = False
seattle_team = None

if giannis_mvp:     # Not giannis_mvp == True
    print("The Greek God of Basketball has been coronated!")

if bucks_champs:
    print("We are the champions!")
else:
    print("Maybe next year...")

                        # Another way to write 
if not bucks_champs:    # "if not" reverses Truthy or Falsy conditional
    print("Maybe next year...(rewritten)")

if seattle_team:
    print("Oh how we've missed you so much!")
else:
    print("Fine! We have soccer instead!")

if giannis_mvp and bucks_champs:    # multiple if statement using "and"
    print("Greatest season in Bucks history!")
else:
    print("Still not there...")

heaven = "Greatest season in Bucks history! (rewritten)"
purgatory = "Still not there... (rewritten)"

        # A Ternary If Statement (i.e. a one-liner)
print(heaven) if giannis_mvp and bucks_champs else print(purgatory)

if giannis_mvp or bucks_champs:     # multiple if statement using "or"
    print("Pretty damn successful nonetheless")

## Ternary If Statements (i.e. one-liners) ##

TOR_ECF_games_won = 4
MIL_ECF_games_won = 2

print("TOR") if TOR_ECF_games_won > MIL_ECF_games_won else print("MIL")
