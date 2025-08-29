# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

revokedBadgeNumbers = {225, 410, 710, 556, 557}
approved = []
denied = []

while True:
    visitorName = input("What is your name? ")

    if visitorName.lower() == "done":
        approved.sort()
        denied.sort()
        print(
            f"=== END OF DAY REPORT ===\nThere were {len(approved)} approved visitors today.\nThere were {len(denied)} denied visitors today"
        )
        print("APPROVED VISITORS")
        for visitor in enumerate(approved, 1):
            print(f"{visitor[0]}. {visitor[1].title()}")
        print("DENIED VISITORS")
        for visitor in enumerate(denied, 1):
            print(f"{visitor[0]}. {visitor[1].title()}")
        break
    else:
        badgeNumber = int(input("What is your badge number? ").strip())
        for i in revokedBadgeNumbers:
            if badgeNumber == i:
                print("ACCESS DENIED")
                denied.append(visitorName)
        if badgeNumber not in revokedBadgeNumbers:
            print("ACCESS GRANTED")
            approved.append(visitorName)
