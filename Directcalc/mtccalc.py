import math
while (True):
    def find_angles(v, R, g=17.81):
        val = (g * R) / (v**2)
        if val > 1:
            return None  # target out of range
        angle1 = 0.5 * math.asin(val)  # in radians
        angle2 = (math.pi / 2) - angle1  # complementary angle
        return math.degrees(angle1), math.degrees(angle2)

    # Example:
    v = int(input("Enter the initial velocity (m/s): "))
    R = int(input("Enter the range (m): "))
    angles = find_angles(v, R)
    if angles:
        print(f"Possible angles: {angles[0]:.2f}°, {angles[1]:.2f}°")
    else:
        print("Target out of range")