print("Welcome to the Data Analyzer And Transformer Program")

def print_menu():
    print("\nSelect option:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factortial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")

def display_summary(dataset):
    if not dataset:
        print("Dataset is empty Please input data first (Option 1).")
        return
    total_elements = len(dataset)
    max_value = max(dataset)
    min_value = min(dataset)
    sum_values = sum(dataset)
    
    avg_value = sum_values / total_elements
    print("\nData Summary:")
    print(f"- Total elements: {total_elements}")
    print(f"- Minimum value: {min_value}")
    print(f"- Maximum value: {max_value}")
    print(f"- Sum of all values: {sum_values}")
    print(f"- Average value: {avg_value:.2f}")

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def filter_data(dataset, threshold):
    return list(filter(lambda x: x > threshold, dataset))

def sort_data(dataset):
    order = input("Enter sorting order ('asc' for Ascending, 'desc' for Descending): ").lower()
    if order == 'desc':
        return sorted(dataset, key=lambda x: x, reverse=True)
    else:
        return sorted(dataset, key=lambda x: x)

def display_statistics(dataset):     #Use AI
    if not dataset:
        print("Dataset is empty! Please input data first (Option 1).")
        return
    n = len(dataset)
    mean_val = sum(dataset) / n
    sorted_data = sorted(dataset)
    if n % 2 == 1:
        median_val = sorted_data[n // 2]
    else:
        median_val = (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2
    variance_val = sum((x - mean_val) ** 2 for x in dataset) / n
    std_dev_val = variance_val ** 0.5
    print("\nDataset Statistics:")
    print(f"- Mean: {mean_val:.2f}")
    print(f"- Median: {median_val}")
    print(f"- Standard Deviation: {std_dev_val:.2f}")

dataset = []

while True:
    print_menu()
    choice = int(input("Please enter your choice number: "))
    
    if choice == 1:
        data_input = input("Enter data for a 1D array (separated by spaces):\n")
        dataset = [int(x) for x in data_input.split()]
        print("Data stored successfully")
        
    elif choice == 2:
        display_summary(dataset)
        
    elif choice == 3:
        num = int(input("Enter a number to calculate its factorial: "))
        print(f"Factorial of {num} is: {calculate_factorial(num)}")
        
    elif choice == 4:
        if not dataset:
            print("Dataset is empty")
        else:
            threshold = int(input("Enter the threshold value: "))
            result = filter_data(dataset, threshold)
            print(f"Elements greater than {threshold}: {result}")
            
    elif choice == 5:
        if not dataset:
            print("Dataset is empty")
        else:
            result = sort_data(dataset)
            print(f"Sorted Data: {result}")
            
    elif choice == 6:
        display_statistics(dataset)
        
    elif choice == 7:
        print("Exit the program")
        break
        
    else:
        print("Invalid choice Please enter a number between 1 to 7")
