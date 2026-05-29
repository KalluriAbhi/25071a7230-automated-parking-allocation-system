# =========================================================
#      Automated Parking Allocation System
# =========================================================

 from datetime import datetime

# Setup parking
floors = 2
slots_per_floor = 3

parking = []
for f in range(floors):
    floor = []
    for s in range(slots_per_floor):
        floor.append({
            "occupied": False,
            "vehicle": None,
            "entry_time": None,
            "name": None,
            "phone": None
        })
    parking.append(floor)

rate_per_hour = 20


# 🚗 Book Slot
def book_slot():
    vehicle = input("Enter vehicle number: ")
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")

    for f in range(len(parking)):
        for s in range(len(parking[f])):
            if not parking[f][s]["occupied"]:
                parking[f][s]["occupied"] = True
                parking[f][s]["vehicle"] = vehicle
                parking[f][s]["entry_time"] = datetime.now()
                parking[f][s]["name"] = name
                parking[f][s]["phone"] = phone

                print("\n✅ Slot booked!")
                print("Name:", name)
                print("Phone:", phone)
                print("Vehicle:", vehicle)
                print(f"Floor: {f+1}, Slot: {s+1}")
                print("Entry Time:", parking[f][s]["entry_time"], "\n")
                return

    print("\n❌ No slots available!\n")


# 🚪 Exit + Bill
def exit_slot():
    vehicle = input("Enter vehicle number: ")
    payment = input("Payment Mode (UPI/Cash/Card): ")

    for f in range(len(parking)):
        for s in range(len(parking[f])):
            slot = parking[f][s]

            if slot["vehicle"] == vehicle:
                exit_time = datetime.now()
                duration = exit_time - slot["entry_time"]

                seconds = int(duration.total_seconds())

                # 🔥 Manual ceil logic
                hours = seconds // 3600
                if seconds % 3600 != 0:
                    hours += 1

                bill = hours * rate_per_hour

                print("\n------ BILL ------")
                print("Name:", slot["name"])
                print("Phone:", slot["phone"])
                print("Vehicle:", vehicle)
                print("Floor:", f+1, "Slot:", s+1)
                print("Entry:", slot["entry_time"])
                print("Exit:", exit_time)
                print("Hours:", hours)
                print("Amount: ₹", bill)
                print("Payment Mode:", payment)
                print("------------------\n")

                # Free slot
                parking[f][s] = {
                    "occupied": False,
                    "vehicle": None,
                    "entry_time": None,
                    "name": None,
                    "phone": None
                }
                return

    print("\n❌ Vehicle not found!\n")


# 📊 Show Parking
def show_parking():
    print("\n--- Parking Status ---")
    for f in range(len(parking)):
        print(f"\nFloor {f+1}:")
        for s in range(len(parking[f])):
            slot = parking[f][s]
            if slot["occupied"]:
                print(f" Slot {s+1}: OCCUPIED ({slot['vehicle']})")
            else:
                print(f" Slot {s+1}: EMPTY")
    print("----------------------\n")


# 🎮 Menu
while True:
    print("==== PARKING SYSTEM ====")
    print("1. Book Slot")
    print("2. Exit & Pay")
    print("3. Show Parking")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_slot()

    elif choice == "2":
        exit_slot()

    elif choice == "3":
        show_parking()

    elif choice == "4":
        print("Exiting... 👋")
        break

    else:
        print("❌ Invalid choice!\n")
