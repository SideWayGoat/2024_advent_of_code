from pathlib import Path

WORKDIR = Path('/home/Vasheti/code/adventofcode/day2/')

def read_data():
    file = Path(WORKDIR / 'input.txt')
    dataset = []
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            for line in data:
                numbers = [int(x) for x in line.split()]
                dataset.append(numbers)
            return dataset
    except Exception as err:
        print(f'being stupid again {err}')

def safe_unsafe(data):
    """Check if sequences can be made safe by removing at most one element"""
    safe = 0
    
    for line in data:
        if is_safe_sequence(line):
            safe += 1
            continue
        
        for i in range(len(line)):
            modified_line = line[:i] + line[i+1:]
            if is_safe_sequence(modified_line):
                safe += 1
                break
    
    return safe

def is_safe_sequence(seq):
    """Check if sequence is strictly monotonic with differences ≤ 3"""
    if len(seq) <= 1:
        return True
    
    is_increasing = all(seq[i] < seq[i+1] for i in range(len(seq)-1))
    is_decreasing = all(seq[i] > seq[i+1] for i in range(len(seq)-1))
    
    if not (is_increasing or is_decreasing):
        return False
    
    for i in range(len(seq)-1):
        if abs(seq[i+1] - seq[i]) > 3:
            return False
    
    return True


def main():
    data = read_data()
    safe = safe_unsafe(data)
    print(safe)

main()