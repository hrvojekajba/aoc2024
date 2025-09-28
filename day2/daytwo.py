problem_input = open("/home/hrvojekajba/repos/aoc2024/day2/daytwoinput.txt")
lines = []
lines_checked = []

def split_input(pr_inp):
    for line in pr_inp:
        numbers_in_line = line.split()
        line_to_int = list(map(int, numbers_in_line))
        lines.append(line_to_int)

def check_lines(lines):
    for line in lines:
        if line == sorted(line, reverse=False) or line == sorted(line, reverse=True):
            lines_checked.append(line)

def check_difference(line):
        for i in range(len(line)):
            if i == 0:
                continue
            score = abs(line[i] - line[i - 1])
            if score > 3 or score < 1:
                return False
        return True

def main():
    safe_lines = 0
    split_input(problem_input)
    check_lines(lines)
    for line in lines_checked:
        if check_difference(line) == True:
            safe_lines += 1
        # PART 2 - todo
        else:
            for i, number in enumerate(line):
                line_copy = line.copy()
                line_copy.pop(i)
                if check_difference(line_copy) == True:
                    safe_lines += 1
                    break
    print(f"Number of safe lines: {safe_lines}")

if __name__ == "__main__":
    main()