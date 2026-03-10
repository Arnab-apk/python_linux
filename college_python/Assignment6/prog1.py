import math

def area_circle(radius):
    return math.pi * radius ** 2

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def main():
    print("=== Area Calculator ===")
    print("1. Circle")
    print("2. Square")
    print("3. Rectangle")
    print("4. Triangle")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == '1':
        r = float(input("Enter radius: "))
        print(f"Area of Circle: {area_circle(r):.2f}")
    elif choice == '2':
        s = float(input("Enter side: "))
        print(f"Area of Square: {area_square(s):.2f}")
    elif choice == '3':
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print(f"Area of Rectangle: {area_rectangle(l, w):.2f}")
    elif choice == '4':
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print(f"Area of Triangle: {area_triangle(b, h):.2f}")
    else:
        print("Invalid choice!")

main()
