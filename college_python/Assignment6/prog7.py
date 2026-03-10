def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

n = int(input("Enter number of disks: "))
print(f"\nSteps to solve Tower of Hanoi with {n} disks:\n")
tower_of_hanoi(n, 'A', 'C', 'B')
