from pathlib import Path


WORKDIR = Path('/home/Vasheti/code/adventofcode/day1/')

def read_file():
    file = Path(WORKDIR / 'input.txt')
    list1 = []
    list2 = []
    try:
        with open(file, 'r') as r:
            lines = r.readlines()
            for line in lines:
                if line.strip():
                    values = line.split()
                    list1.append(values[0])
                    list2.append(values[1])

            list1.sort()
            list2.sort()
            return list1, list2
    except Exception as err:
        print(f'youre stupid {err}')

def compare_lists(list1, list2):
    total_diff = 0
    multiplier = 1
    for num1, num2 in zip(list1, list2):
        multiplier = list2.count(num1)
        total_diff += abs(int(num1) * int(multiplier))

    return total_diff
        

def main():
    list1, list2 = read_file()
    result = compare_lists(list1, list2)
    print(result)


main()