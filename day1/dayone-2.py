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

def calculate_similarity(num_left, num_right):
    similarity = 0
    repeats = 0
    for left in num_left:
        for right in num_right:
            if left == right:
                repeats += 1
        similarity += (int(left) * repeats)
        repeats = 0
    return similarity

def main():
    get_and_sort(problem_input)
    similarity = calculate_similarity(numbers_left, numbers_right)
    print(similarity)

if __name__ == "__main__":
    main()