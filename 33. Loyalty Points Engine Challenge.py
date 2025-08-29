# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Purchase history (e.g., 3.75, 7.20, etc.)
purchases = [20.50, 7.20, 11.75]
totalPoints = []


def earnPoints(price):
    # calling int(price) to round to the nearest whole dollar for the loyalty point
    return int(price) * 3


def tierLabel(points):
    if points < 100:
        return "Bronze"
    elif points >= 101 and points < 500:
        return "Silver"
    elif points > 500:
        return "Gold"
    else:
        print("Error calculating Loyalty Tier")


# earning points for each purchase & adding those points to the totalPoints list
for purchase in purchases:
    totalPoints.append(earnPoints(purchase))

print(
    f"=== LOYALTY SUMMARY ===\nTotal Dollars Spent: ${sum(purchases)}\nTotal Points Earned: {sum(totalPoints)} points\nFinal Loyalty Tier: {tierLabel(sum(totalPoints))}"
)
