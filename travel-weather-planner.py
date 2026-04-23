# Travel Weather Planner (User Input Version)

# Get user input
distance_mi = float(input("Enter distance in miles: "))
is_raining = input("Is it raining? (yes/no): ").strip().lower() == "yes"
has_bike = input("Do you have a bike? (yes/no): ").strip().lower() == "yes"
has_car = input("Do you have a car? (yes/no): ").strip().lower() == "yes"
has_ride_share_app = input("Do you have a ride-share app? (yes/no): ").strip().lower() == "yes"

# Decision logic
if not distance_mi:
    print(False)

elif distance_mi <= 1:
    print(not is_raining)

elif distance_mi <= 6:
    print(has_bike and not is_raining)

else:
    print(has_car or has_ride_share_app)