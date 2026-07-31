colors = ("red", "green", "blue", "yellow", "purple")

# Indexing (same as lists)
print(f"First color: {colors[0]}")      # red คือตัวเเรกที่โค้คต้องการ
print(f"Last color: {colors[-1]}")      # purple คือตัวสุดท้ายที่โค้คต้องการ

# Slicing (same as lists)
print(f"First 3: {colors[0:3]}")        # ('red', 'green', 'blue') คือสีที่เราต้องการ
print(f"Last 2: {colors[-2:]}")         # ('yellow', 'purple') ถ้า-2คือนับท้อยหลังเเละคำตอบก็อยู่ในวงเเล็บ
print(f"Every 2nd: {colors[::2]}")      # ('red', 'blue', 'purple')

# Tuple unpacking
point = (10, 20)
x, y = point
print(f"x: {x}, y: {y}")                # x: 10, y: 20

# Multiple assignment using tuples
person = ("Alice", 25, "Engineer")
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Swapping variables using tuples
a = 5
b = 10
a, b = b, a
print(f"After swap: a = {a}, b = {b}")  # a = 10, b = 5