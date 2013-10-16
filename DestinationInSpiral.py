def checkio(data):
    def find(n):
        k=1
        if n==1:
            return (0,0)
        #Find edge of matrix
        while not (2*k-1)**2 < n <= (2*k+1)**2:
            k+=1
        edge=2*k
        #Reminder and divident
        rem = ((edge+1)**2 - n)%edge
        div = ((edge+1)**2 - n)/edge
        ans=(0,0)
        #Traverse the matrix points
        if div==0:
            ans=(-k,k-rem)
        elif div==1:
            ans=(-k+rem,-k)
        elif div==2:
            ans=(k,-k+rem)
        else:
            ans=(k-rem,k)
        return ans
    a=find(data[0])
    b=find(data[1])
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"