
actual_input = "9191896883-9191940271,457499-518693,4952-6512,960-1219,882220-1039699,2694-3465,3818-4790,166124487-166225167,759713819-759869448,4821434-4881387,7271-9983,1182154-1266413,810784-881078,802-958,1288-1491,45169-59445,25035-29864,379542-433637,287-398,75872077-75913335,653953-689335,168872-217692,91-113,475-590,592-770,310876-346156,2214325-2229214,85977-112721,51466993-51620441,8838997-8982991,534003-610353,32397-42770,17-27,68666227-68701396,1826294188-1826476065,1649-2195,141065204-141208529,7437352-7611438,10216-13989,33-44,1-16,49-74,60646-73921,701379-808878"
test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def create_pairs(input_string:str)->list:
    inputs = input_string.split(",")
    i = []
    for item in inputs:
        i.append(item.split("-")[0])
        i.append(item.split("-")[1])
    result = []
    for n in range(0, len(i) - 1, 2):
        result.append((int(i[n]), int(i[n + 1])))
    return result

#TODO: first star
def find_duplicates(pair_list):
    result = 0
    for a, b in pair_list:
        for number in range(a, b+1):
            num_str = str(number)
            first_half = num_str[0:len(num_str)//2] # [a:b], b not inclusive
            sec_half = num_str[len(num_str) // 2::]
            if first_half == sec_half:
                result += number
    return result

#TODO: second star
def find_repeats(pair_list):
    result = 0
    for a, b in pair_list:
        # print(a, b)
        for number in range(a, b + 1):
            num_str = str(number)
            combi_found = []
            for length in range(1, (len(num_str) // 2)+1):
                teil = num_str[0:length]
                sol = teil*(len(num_str) // length)
                if sol == num_str and sol not in combi_found:
                    # print("found: " + num_str)
                    result += number
                    combi_found.append(num_str)
        # print()
    return result

# test_pairs = [(11,22)]

print(f"solution: {find_repeats(create_pairs(actual_input))}")