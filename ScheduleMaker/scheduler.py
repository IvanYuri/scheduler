
import json
import random
import sys


'''
second proposal for the general ideia, using json file to
manage and store information, the code works if every shift can be
covered by all avaiable staff for the right amount of days

in this example we have 3 shift available for 6 days of the week,
for three staff members. giving each staff 12 credits, or 12 shifts
to cover, fulling out two shift per staff per day.

'''

# first import the settings where the info is stored
def importSettings(settingsPath):
    with open(settingsPath) as f:
        data = json.load(f)
    return data

# this function counts the numer of shifts available and multiplies by the number of shifts during the week
def countShift(settings):
    shiftsToFill = len(settings["spaces"]) * 3 * 6 #3 shifts, 6 days a week
    numberOfStaff = len(settings["members"])
    shiftCoverable = numberOfStaff * 2 * 6

    # if short staffed the system will require to fill the positions before it can run properly
    if shiftsToFill > shiftCoverable:
        print(f"We are short staffed with {shiftsToFill} shits to fill for {numberOfStaff} employees")
        sys.exit(1)
    print(f"We have {shiftsToFill} shits to fill for {numberOfStaff} employees, able to cover {shiftCoverable} shifts")


settingsPath = sys.argv[1] #protect this
settings = importSettings(settingsPath)

# this prints the staff board and the amount of credits, or shifts they have to work during the week
print(settings["members"])

# this was done manually in this code for speed purposes
days = ["Monday", "Tuesday", "Wed", "Thu", "Fri", "Sat"]
periods = ["Morning", "Afternoon", "Evening"]
shifts = []

'''
goal is to have 1 member per shift per space (3 shifts per day)
'''

# so here we are using two credits a day of each member, so one can work two shifts a day
for member in settings["members"]:
    member["credit"] = 2
    
# in this case we copy the members in setting so we can use two times
referenceMembers = settings["members"].copy()
# print("REF = ", referenceMembers)

# now we append the members to each of the week
for i in range(2):
    shifts.append({"Day" : days[i]})
    settings["members"] = referenceMembers.copy()
    print("members = ", settings["members"])

    # here we randomly assing a shift for each member    
    for period in periods:
        success = len(settings["spaces"])
        # keep looping while there are shifts available
        while success > 0:
            memberAssigneds = random.sample(settings["members"], len(settings["spaces"]))
            for space, member in zip(settings["spaces"], memberAssigneds):
                if member["name"] not in shifts[i]:
                    shifts[i][member["name"]] = [] 
                if member["credit"] > 0:
                    shifts[i][member["name"]].append([period, space["name"]])
                    member["credit"] -= 1
                    success -= 1
            
       
print(shifts)


# for space in settings["spaces"]:
#     for members in settings["members"]:
#         if members["avail"] == True:
