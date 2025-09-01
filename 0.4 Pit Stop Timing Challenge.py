# 🏁 Pit Stop Timing Optimizer 🔧


print("Hello, welcome to the Pit Stop Timing Optimizer!")

# 1. Ask the user for the total race time in seconds.
totalRaceTime = float(input("What was the total race time (in seconds?) "))

# 2. Ask how many pit stops were made.
numPitStops = int(input("What was the number of pit stops made? "))

# 3. Ask for the average pit stop duration (in seconds).
avgPitStopTime = float(
    input("Lastly, what was the average pit stop duration (in seconds)? ")
)

# Then:
# - Calculate the total pit stop time.
totalPitStopTime = numPitStops * avgPitStopTime

# - Calculate the percentage of the race spent in the pits.
pitPercentTime = (totalPitStopTime / totalRaceTime) * 100

# - Round the percentage to 2 decimal places.
roundedPPT = round(pitPercentTime, 2)

# Show the user our values stored thus far
print("--- PIT STOP SUMMARY ---")
print(f"[TOTAL RACE TIME]: {totalRaceTime} seconds")
print(f"[NUMBER OF PIT STOPS]: {numPitStops} pit stops")
print(f"[AVG. PIT STOP TIME]: {avgPitStopTime} seconds")

# Finally, print all of the following:
# - Total pit stop time in seconds
print("[PIT STOP TIME]: " + str(totalPitStopTime) + " seconds")

if pitPercentTime >= 0.05:
    # - Percentage of race time spent in pits
    print(f"[% OF RACE SPENT IN PITS]: {roundedPPT}%")
    # - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"
    print("You need a new pit crew. 🛠️")
else:
    print(f"[% OF RACE SPENT IN PITS]: {roundedPPT}%")
