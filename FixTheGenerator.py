from itertools import combinations
def checkio(data):
    def istriangle(sides):
        return (sum(sides)-max(sides))<max(sides)
    
    possibilities = combinations(data,3)
    return sum(map(istriangle,possibilities))

    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio((4, 2, 10)) == 1, "First"
    assert checkio((1, 2, 3)) == 0, "Second"
    assert checkio((5, 2, 9, 6)) == 2, "Third"