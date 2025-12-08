test_input = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def list_fresh_id(string):
    result = []
    list = string.split("\n")
    list.pop(0) # the first entry is just a blank space

    i = 0
    while list[i] != "":
        pair = list[i].split("-")
        # print(pair)
        result.append((int(pair[0]), int(pair[1])))
        result.sort() #sorts it by the first element
        i += 1
    return result

def list_food_id(string):
    list = string.split("\n")
    list.pop(0)
    return [int(id) for id in list[list.index("")+1::]] # we find the center blank line

# print(list_fresh_id(test_input))
print(list_food_id(test_input))

def count_fresh_food(complete_input):
    food_list = list_food_id(complete_input)
    fresh_list = list_fresh_id(complete_input)
    result = 0
    for food in food_list:
        fresh = False
        i = 0
        # print(food, end="")
        while i < len(fresh_list) and not fresh:
            fresh_range = fresh_list[i]
            if fresh_range[0] <= food <= fresh_range[1]:
                result += 1
                fresh = True
            i += 1
        # print(fresh)
    return result

with open("day5.txt", "r") as f:
    actual_input = f.read()

print(count_fresh_food(actual_input))

# TODO: Answer was 674: I got 673, so one too short - figure out the problem


# Part Two:
def count_all_available_fresh_id(fresh_ranges):
    organized_fresh_ranges = []
    # so ranges can be one of two things either they cross path or they don't
    # we add the new range if it's unique and
    # if it crosses a range, we combine them, if the original range contains the new range.. we'll ignore it
    for given_range in fresh_ranges:
        print(given_range)
        if len(organized_fresh_ranges) == 0:
            organized_fresh_ranges.append(given_range)
        else:
            appended = False
            for orga_range in organized_fresh_ranges:
                if not appended:
                    if orga_range[0] <= given_range[0] <= orga_range[1] and orga_range[0] <= given_range[1] <= orga_range[1]:
                        appended = True  # since the range is already contained in the list
                        print("Contained range found")
                    elif orga_range[0] <= given_range[0] <= orga_range[1]:
                        new_range = (orga_range[0], given_range[1])
                        organized_fresh_ranges.remove(orga_range)
                        organized_fresh_ranges.append(new_range)
                        appended = True
                    elif orga_range[0] <= given_range[1] <= orga_range[1]:
                        new_range = (given_range[0], orga_range[1])
                        organized_fresh_ranges.remove(orga_range)
                        organized_fresh_ranges.append(new_range)
                        appended = True
            if not appended:
                organized_fresh_ranges.append(given_range)

    print(organized_fresh_ranges)

    count = 0
    for r in organized_fresh_ranges:
        count += r[1] - r[0] + 1
    return count



test_input_2 = """
100-302
300-400
50-1000
5500-6734
6734-8000
7777-7777
999-999
90000-1000000
10-11
3-15
"""

print(count_all_available_fresh_id(list_fresh_id(test_input_2)))
# TODO: issue -> a range can reach two or more ranges at the same time.


# for ran in list_fresh_id(actual_input):
#     if ran[0] <= ran[1]:
#         print(f"{ran} is flipped")
# none of the ranges are (a, b) where a > b


