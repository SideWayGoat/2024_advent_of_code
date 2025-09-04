from pathlib import Path

WORKDIR = Path('/home/Vasheti/code/adventofcode/day4/')

def read_file():
    file = Path(WORKDIR, 'input.txt')
    try:
        with open(file, 'r') as f:
            data = f.readlines()
            return data
    except Exception as err:
        print(f'To even fail at reading a file... cringe {err}')

def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def findWordInDirection(grid, n, m, word, index,x, y, dirX, dirY):
    if index == len(word):
        return True

    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(grid, n, m, word, index + 1, x + dirX, y + dirY, dirX, dirY)

    return False

def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
          
            # Check if the first character matches
            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, 0, 
                                           i, j, dirX, dirY):
                        ans.append([i, j])

    return ans

def main():
    data = read_file()
    word = 'XMAS'
    ans = searchWord(data, word)

    print(len(ans))


main()