
distance_mi = 4
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = False

if bool(distance_mi) == False:
    print(False)
else:

    if distance_mi <= 1:
        if is_raining == False:
            print(True)
        elif is_raining == True:
            print(False)

    if distance_mi > 1 and distance_mi <= 6:
        if has_bike and is_raining == False:
            print(True)
        else:
            print(False)

    if distance_mi > 6:
        if has_car or has_ride_share_app:
            print(True)
        else:
            print(False)