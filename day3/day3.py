from pathlib import Path
import re

WORKDIR = '/home/Vasheti/code/adventofcode/day3/'

def read_file() -> str:
    file = Path(WORKDIR, 'input.txt')
    data = []
    try:
        with open(file, 'r') as f:
            data = f.read()
            return data
    except Exception as err:
        print(f'being stupid again {err}')

def extract_mul(data: str) -> int:
    """go through the string and find the sequence mul(x,y)"""
    total = 0
    matches = re.findall(r"(mul\(\d+,\d+\))|(don't\(\))|(do\(\))", data)
    skip = False
    try:
        for match in matches:
            if "don't()" in match:
                skip = True

            if "do()" in match:
                skip = False
                continue

            if skip:
                continue

            number = re.findall(r'\d+', match[0])
            if number[0] and number[1]:
                total += int(number[0]) * int(number[1])
                
    except Exception as err:
        print(f'failed with {match} with error {err}')
    
    return total

def main():
    data = read_file()
    total = extract_mul(data)

    print(total)

main()