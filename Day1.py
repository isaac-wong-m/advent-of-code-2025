from Day2 import actual_input

# Dial starts from 50.. 0 to 99, left means minus and right means plus


test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

test_input_2 = "R1000"


# with open("day1.txt", "a") as f:
#   f.write(actual_input)

with open("day1.txt", "r") as f:
    actual_input = f.read()



# test_list = test_input.split()
# for ele in test_list:
#     print(ele[0])
#     print(ele[1::])
#
zeroes = 0
def left_dial(current_dial, dial_num):
    if current_dial - dial_num >= 0:
        return current_dial - dial_num
    else:
        global zeroes
        zeroes += 1
        return left_dial(100, dial_num - current_dial)

def right_dial(current_dial, dial_num):
    if current_dial + dial_num <= 99:
        return current_dial + dial_num
    else:
        global zeroes
        zeroes += 1
        return right_dial(-1, dial_num - (99 - current_dial))

def generate_result(puzzle_input:str)->int:
    input_list = puzzle_input.split()
    curr_dial = 50
    result_count = 0
    for element in input_list:
        if element[0] == "L":
            curr_dial = left_dial(curr_dial, int(element[1::]))
        else:
            curr_dial = right_dial(curr_dial, int(element[1::]))
        if curr_dial == 0:
            result_count += 1
    print(f"current dial: {curr_dial}")
    return result_count




print(f"result: {generate_result(actual_input)}")
print(zeroes)




# complexity probably too high,
# but since I'm doing this in the middle of night I ain't got time to optimize it..



# print(left_dial(50,68))
# print(left_dial(82,30))
# print(right_dial(52,48))