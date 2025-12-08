with open("day6.txt", "r") as f:
    actual_input = f.read()



def operate(operator:str, num1, num2, num3, num4 = "0"):
    num1, num2, num3, num4 = int(num1), int(num2), int(num3), int(num4)
    if operator == "*":
        if num4 == 0: num4 = 1
        return num1 * num2 * num3 * num4
    elif operator == "+":
        return num1 + num2 + num3 + num4
    else:
        print("Error input")
        return -1

def part_one(input_string): # for four rows
    lines = actual_input.split("\n")
    matrix = [[ele for ele in line.split()] for line in lines]

    result = sum(operate(matrix[4][m], matrix[3][m],matrix[2][m],matrix[1][m],matrix[0][m]) for m in range(len(matrix[0])))
    return result

# print(part_one(actual_input))

# TODO: part two

test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
  1 1    1   1
*   +   *   +  """

def part_two(input_string):
    lines = input_string.split("\n")
    matrix = [[ele for ele in line.split()] for line in lines]
    print(matrix)
    columns = []
    for m in range(len(matrix[0])):
        columns.append([matrix[0][m], matrix[1][m], matrix[2][m], matrix[3][m], matrix[4][m]])
        # the last one is the operation

    result = 0
    for column in columns:
        biggest_num = max(int(column[n]) for n in range(4))
        # add the spaces
        numbers = [0,0,0,0]
        for i in range(4):
            numbers[i] = (len(str(biggest_num)) - len(column[i]))*" " + column[i]
        col = []
        for i in range(len(str(biggest_num))):
            c = ""
            for n in range(4):
                c += numbers[n][len(str(biggest_num)) - 1 - i]
            col.append(int(c))

        if column[4] == "*":
            result1 = 1
            for num in col:
                result1 *= num
            result += result1
        else:
            result1 = 0
            for num in col:
                result1 += num
            result += result1

    return result
# results should be from left to right in columns, so for the first pair of 4 would be 356 * 24 * 1

print(part_two(actual_input))

# TODO: shitty Code, wrong answer btw!!!


