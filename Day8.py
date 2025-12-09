import math

# finds the first n closest connections, connect them and in the end multiply their number of boxes in the largest 3 circuits
# two boxes or more connected -> circuit
test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

# as for the puzzle input we have 1000 positions, which means 1000*999/2 distances
# need to be calculated to find the closest box to each box

class Coordinate:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def distance(self, coor):
        if type(coor) != Coordinate:
            print("Class issue, parameter given not an Coordinate!!")
        return round(math.sqrt((self.x-coor.x)**2+(self.y-coor.y)**2+(self.z-coor.z)**2), 4)

    def print(self):
        print(f"({self.x}, {self.y}, {self.z})")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

############Testing################
# a1 = Coordinate(12, 3,4)
# a2 = Coordinate(12, 3,4)
# a3 = Coordinate(5, 2,3)
# print(a1.distance(a3))
# print(a1 == a3)
#
# coordinate_pair = (a1, a2)
#
# print(coordinate_pair)

####################################

def part_one(input_str):
    coordinates = []
    for line in input_str.split():
        temp = line.split(",")
        coordinates.append(Coordinate(temp[0], temp[1], temp[2]))

    # distance: {(cor1, cor2): distance, (cor1, cor3): distance}
    # len(distance) should be #coord*(#coord - 1) / 2
    # different implementation used, ignore this

    distances = {}
    # we have to store dictionary keys as hashable type (any object that is list or iterable not included)
    i = 0
    for c in coordinates:
        distance_from_c = {}
        for p in range(0, len(coordinates)):
            if c.distance(coordinates[p]) != 0: # if zero, then it's itself
                distance_from_c[c.distance(coordinates[p])] = coordinates[p]
        distances[i] = distance_from_c
        i +=1


    circuits = [] #[{cir1},{[}cir2}]
    used_boxes = []
    # denkfehler, after you put two boxes in the circuits, they should no longer be finding a circuit
    for k, dis in distances.items():
        if coordinates[k] not in used_boxes:
            closest_box_to_k_coor = dis[min(dis.keys())]
            coordinates[k].print()
            dis[min(dis.keys())].print()

            # find the circuit or add these two as new ones
            added = False
            for circuit in circuits:
                if coordinates[k] in circuit:
                    circuit.append(closest_box_to_k_coor)
                    added = True
                    used_boxes.append(closest_box_to_k_coor)
                    # ideally stops searching
            if not added:
                circuits.append([coordinates[k], closest_box_to_k_coor])
                used_boxes.append(coordinates[k])
                used_boxes.append(closest_box_to_k_coor)

# TODO: not done yet, NOT EVEN THE FIRST STAR!!

    for circuit in circuits:
        print(circuit)


    return 0

print(part_one(test_input))

# TODO: learn how to make the program more efficient, don't repeat the same distance