import math

record = float(input())
distance = float(input())
time_for_swimming = float(input())
needed_seconds = 0

time_for_meters_swum = distance * time_for_swimming
seconds_for_swim = math.floor((distance / 15)) * 12.5
total_time = time_for_meters_swum + seconds_for_swim

if record <= total_time:
    needed_seconds = total_time - record
    print(f"No, he failed! He was {needed_seconds:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

