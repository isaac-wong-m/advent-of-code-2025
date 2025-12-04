

test_inputs = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open("day3.txt", "r") as f:
    actual_input = f.read()

def find_batteries(battery_bank:str)->int:
    # find the largets number first and split the string
    # find the second largest with the string after the first num
    first = 0
    index = 0
    for i in range(len(battery_bank) - 1 ):
        if int(battery_bank[i]) > int(first):
            first = battery_bank[i]
            index = i
    if index == len(battery_bank) - 2: # if it's the last two digits
        return int(first+battery_bank[-1])

    return int(first + find_battery(battery_bank[index + 1::]))

def find_battery(battery_bank:str)->int:
    first = 0
    for i in range(len(battery_bank)):
        if int(battery_bank[i]) > int(first):
            first = battery_bank[i]
    return first

# print(find_largest_batteries(single_input))

#TODO: first star
def find_banks_batteries(banks:str)->int:
    result = 0
    for bank in banks.split():
        result += int(find_batteries(bank))
    return result

# print(find_banks_batteries(actual_input))


#TODO: second star
# make damn thing recursive

# def find_12_batteries(battery_bank)->int:
#     first = 0
#     index = 0
#     for i in range(len(battery_bank) - 11):
#         if int(battery_bank[i]) > int(first):
#             first = battery_bank[i]
#             index = i
#     if index == len(battery_bank) - 12:  # if it's the last 12 digits
#         return int(first + battery_bank[-11::])
#
#     result = str(first)
#
#     for n in range(11):
#         pair = find_battery_and_index(battery_bank, index, 11-n)
#         index = pair[1]
#         result += str(pair[0])
#     return result
#
# def find_battery_and_index(battery_bank:str, start_index:int, end_spaces:int)->int:
#     first = 0
#     index = 0
#     for i in range(start_index, len(battery_bank) - end_spaces):
#         if int(battery_bank[i]) > int(first):
#             first = battery_bank[i]
#             index = i
#     return first, index
#
#
# def find_banks_12_batteries(banks:str)->int:
#     result = 0
#     for bank in banks.split():
#         result += int(find_12_batteries(bank))
#     return result

def foo():
    return "dog", 3


a = "12345678912421122299"
b = "12345"
# print(b[-2::])

# print(find_12_batteries(a))
print(find_banks_batteries(test_inputs))

# print(a[-12::])