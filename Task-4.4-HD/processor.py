import os

input_file = "/data/input/numbers.txt"
output_file = "/data/output/result.txt"

print("Starting data processing container...")

with open(input_file, "r") as file:
    numbers = [float(line.strip()) for line in file if line.strip()]

total = sum(numbers)
average = total / len(numbers)
minimum = min(numbers)
maximum = max(numbers)

result = (
    f"Count: {len(numbers)}\n"
    f"Total: {total}\n"
    f"Average: {average}\n"
    f"Minimum: {minimum}\n"
    f"Maximum: {maximum}\n"
)

os.makedirs("/data/output", exist_ok=True)

with open(output_file, "w") as file:
    file.write(result)

print("Processing complete.")
print(result)
print(f"Result saved to {output_file}")