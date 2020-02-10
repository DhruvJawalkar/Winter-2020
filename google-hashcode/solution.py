import sys
import heapq as hq

class Car:

    def __init__(self):
        self.state = 0 #0 is looking for ride, 1 is approaching, 2 is carrying rider
        self.rem_d = 0 #remaining distance to destination
        self.tot_d = 0 #total distance traveled on a ride
        self.start_t = 0 #start time of the current ride
        self.end_t = 0 #end time of the current ride
        self.s_coord = (0, 0) #starting coordinate before finding new ride
        self.r_list = [] #history of all rides



    def add_ride(self, r):
        self.state = 1 #change state
        self.rem_d = calc_dist(self.s_coord, r.s_coord)
        self.tot_d = calc_dist(r.s_coord, r.e_coord)
        self.start_t = r.start_t
        self.end_t = r.end_t #keep track of max end
        self.s_coord = r.e_coord
        self.r_list.append(r.id)



class Ride:

    def __init__(self, line, id):
        self.id = id
        self.s_coord = (line[0],line[1])
        self.e_coord = (line[2],line[3])
        self.start_t = line[4]
        self.end_t = line[5]

        #This reward function is terrible, but it works.
        self.reward = calc_dist(self.s_coord, self.e_coord)

    def __lt__(self, other): #used in making comparisons to build heap
        return self.reward > other.reward

def calc_dist(coord_1, coord_2):
    return (abs(coord_1[0] - coord_2[0]) + abs(coord_1[1] - coord_2[1]))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        rows, cols, num_cars, num_rides, bonus, total_t = [int(x) for x in next(f).split()]
        ride_array = []
        for i, line in enumerate(f):
            ride_array.append(Ride([int(x) for x in line.split()], i))

    hq.heapify(ride_array) #make a max-heap based on reward
    cars = [Car() for i in range(num_cars)]

    score = 0
    for i in range(total_t):
        # print("===STEP " + str(i) + "===")
        for j, car in enumerate(cars):
            if car.state == 0: #car is looking for a new ride
                if len(ride_array) > 0:
                    r = hq.heappop(ride_array)
                    car.add_ride(r)
                    if (car.start_t - car.rem_d > i): #check if car will get bonus
                        score += bonus
                    if (car.rem_d + car.tot_d + i > car.end_t): #if car can't make ride, cancel ride
                        car.state = 0
            if car.state == 1: #car is driving towards new ride
                if car.rem_d == 0: #if car has arrived at new ride
                    car.rem_d = car.tot_d
                    car.state = 2
                else:
                    car.rem_d -= 1 #decrease distance left to travel
                    # print("Car " + str(j) + " is approaching ride " + str(car.r_list[-1]))
            if car.state == 2: #car carrying rider to destination
                if car.rem_d == 0: # if car has completed ride
                    score += car.tot_d
                    car.state = 0
                elif car.start_t <= i: #only start driving if current time is >= ride start time
                    # print("Car " + str(j) + " is carrying ride " + str(car.r_list[-1]))
                    car.rem_d -= 1

    for car in cars:
        print(car.r_list)

    print("Score: " + str(score))
