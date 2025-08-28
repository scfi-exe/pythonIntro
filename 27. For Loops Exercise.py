names = ["john ClEEse", "Eric IDLE", "michael"]
names1 = ["graHam chapman", "TERRY", "terry jones"]
guestList = names + names1

print("You are planning your birthday party! You have two invites left to give out.")

for i in range(2):
    guestList.append(input("Who would you like to give an extra invite to? "))

for guest in guestList:
    print(f"{guest.title()}! You are invited to the party on Saturday.")
