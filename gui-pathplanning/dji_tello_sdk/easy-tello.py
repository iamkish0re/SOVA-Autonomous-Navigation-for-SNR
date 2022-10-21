from easytello import tello

my_drone = tello.Tello()
my_drone.takeoff()

# for i in range(4):
# 	my_drone.forward(100)
# 	my_drone.cw(90)
# my_drone.cw(90)
my_drone.forward(300)
my_drone.cw(90)
my_drone.forward(500)
my_drone.cw(90)
my_drone.forward(300)
my_drone.cw(90)
my_drone.forward(500)

my_drone.land()