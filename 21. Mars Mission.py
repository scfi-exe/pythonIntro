# 🪐 Mars Mission Planner — Challenge Steps
#
# 1. Write a function to calculate how long it takes
#    to reach Mars at a given speed.[timeToMars]
#    - Mars' average distance is 225,000,000 km.
#    - Use the formula: time = distance ÷ speed
#    - Round the result to the nearest hour.
#
# 2. Write another function to figure out the total fuel cost
#    for a mission.
#    - Formula: total cost = distance × fuel usage × price per liter
#
# 3. Test your functions with the provided mission data:
#    - Pathfinder: 40,000 km/h
#    - Perseverance: 75,000 km/h
#    - Starship: 120,000 km/h
#    - Each mission travels 225 million km,
#      burns 0.3 liters/km, and fuel costs $1.80/L.
#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost

# Mission data
mission_1_speed = 40000  # Pathfinder
mission_2_speed = 75000  # Perseverance
mission_3_speed = 120000  # Starship

mars_distance = 225_000_000  # in kilometers
fuel_rate = 0.3  # liters per kilometer
fuel_price = 1.8  # dollars per liter


# formula to determine avg time to maras
def timeToMars(speed):
    exactSpeed = mars_distance // speed
    return exactSpeed


# fuel burn rater (liters per km)
fuelBurnRate = 0.3
fuelDollarCostPerLiter = 1.80


# formula to determine total fuel cost
def totalFuelCost(tripDistance):
    # total cost = distance * fuel usage * price per liter
    totalCost = (tripDistance * fuelBurnRate) * fuelDollarCostPerLiter
    # formats the total to 2 decimal places, instead of the default 1
    roundedTotal = "{:.2f}".format(totalCost)
    return roundedTotal


print("===== Mars Mission Planner =====\n")
print("Mission Name: Pathfinder")
print(f"Travel Time: {timeToMars(mission_1_speed)} hours")
print(f"Fuel Cost: ${totalFuelCost(mars_distance)}\n")

print("Mission Name: Perserverance")
print(f"Travel Time: {timeToMars(mission_2_speed)} hours")
print(f"Fuel Cost: ${totalFuelCost(mars_distance)}\n")

print("Mission Name: Starship")
print(f"Travel Time: {timeToMars(mission_3_speed)} hours")
print(f"Fuel Cost: ${totalFuelCost(mars_distance)}\n")
