def compute_total(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]
    result = compute_total(data)
    print(f"Total: {result}")