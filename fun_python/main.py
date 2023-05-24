from Hanoi import Hanoi


if __name__ == '__main__':
    # Driver code
    disks = int(input("Number of disks to be displaced: "))
    Hanoi.hanoi(disks, 'A', 'B', 'C')
