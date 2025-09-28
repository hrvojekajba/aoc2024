problem_input = open("/home/hrvojekajba/repos/adventofcode/day1/dayoneinput.txt")
numbers_left = []
numbers_right = []

def get_and_sort(file_obj):
    for line in file_obj:
        numbers = line.split()
        numbers_left.append(numbers[0])
        numbers_right.append(numbers[1])
    numbers_left.sort()
    numbers_right.sort()

def calculate_distance(num_left, num_right):
    distance = 0
    for i in range(len(num_left)):
        distance += abs(int(num_left[i]) - int(num_right[i]))
    return distance


def main():
    get_and_sort(problem_input)
    print(calculate_distance(numbers_left, numbers_right))

if __name__ == "__main__":
    main()
