"""Calculate area of rectangle and circle."""

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
radius = float(input("Enter circle radius: "))

area_rectangle = length * breadth
area_circle = 3.14159 * radius * radius

print(f"Area of rectangle = {area_rectangle}")
print(f"Area of circle = {area_circle}")
