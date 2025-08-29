# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time

bus = {
    "seat1": {
        "name": "Banjo",
        "breed": "Mini Poodle",
        "Pickup Time": "6:45 PM",
        "Dropoff Time": "9:00 PM",
    },
    "seat2": {
        "name": "Salvador",
        "breed": "Toy Poodle",
        "Pickup Time": "2:00 PM",
        "Dropoff Time": "7:00 PM",
    },
}

#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#

print(f"=== Starting Bus Roster ===")
for seat, dog in bus.items():
    print(
        f"{seat} is occupied by {dog.get("name", "no name found")}. They are a {dog.get("breed")}."
    )
    print(
        f"{dog.get("name")}'s pickup time is {dog.get("Pickup Time")} and their dropoff time is {dog.get("Dropoff Time")}"
    )

# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#

numSeats = len(bus)
maxSeats = 10

while numSeats < (maxSeats + 1):
    bus[f"seat{numSeats}"] = {
        "name": f"dog{numSeats}",
        "breed": f"breed{numSeats}",
        "Pickup Time": "5:00",
        "Dropoff Time": "7:00",
    }

    numSeats = numSeats + 1

print(bus)
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#

seatToRemove = ""

earlyLeaver = input("Which pet leaves early?: ")
for seat, dog in bus.items():
    if dog.get("name").strip().lower() == earlyLeaver.strip().lower():
        seatToRemove = seat
        print(f"{dog.get("name")} has headed home early.")
        break

bus.pop(seatToRemove)

# 5. Print a final roster listing the remaining pets and their dropoff times.

print("=== FINAL BUS ROSTER ===")
for seat, dog in bus.items():
    print(
        f"{seat} contains {dog.get("name")}, whose dropoff time is {dog.get("Dropoff Time")}."
    )
