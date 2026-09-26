# Automatic Plant Watering System
# Python Project

def automatic_watering(soil_moisture):
    print("\n===== AUTOMATIC PLANT WATERING SYSTEM =====")
    print(f"Soil Moisture: {soil_moisture}%")

    if soil_moisture < 30:
        print("Soil is dry.")
        print("Water Pump: ON")
        print("Plant is being watered...")
    else:
        print("Soil moisture is sufficient.")
        print("Water Pump: OFF")
        print("No watering required.")


while True:
    print("\n1. Check Soil Moisture")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            moisture = float(input("Enter soil moisture percentage (0-100): "))

            if 0 <= moisture <= 100:
                automatic_watering(moisture)
            else:
                print("Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter a number.")

    elif choice == "2":
        print("Automatic Plant Watering System Closed.")
        break

    else:
        print("Invalid choice!")
