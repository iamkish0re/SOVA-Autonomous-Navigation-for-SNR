# Python program to read
# json file

import json
from easytello import tello
def start_drone():
    my_drone = tello.Tello()
    my_drone.takeoff()

    # Opening JSON file
    f = open('waypoint.json',)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    for i in data['wp']:
        print("Distance: ", i['dist_cm'], '\t ' , "Angle : ", i['angle_deg'])
        my_drone.forward(i['dist_cm'])
        my_drone.cw(i['angle_deg'])

        # print(i)

    # Closing file
    f.close()
    my_drone.land()
