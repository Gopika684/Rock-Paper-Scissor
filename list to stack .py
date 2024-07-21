def push_keys_with_marks_greater_than_75(dictionary):
    stack = []
    for key, value in dictionary.items():
        if value > 75:
            stack.append(key)
    return stack

# Function to pop and display the contents of the stack
def pop_and_display_stack(stack):
    while stack:
        print(stack.pop())

# Create the dictionary
marks_dict = {
    "Alice": 80,
    "Bob": 65,
    "Charlie": 90,
    "Dave": 70,
    "Eve": 85,
    "Frank": 60
}

# Call the push function to create a stack of keys with marks > 75
stack_of_keys = push_keys_with_marks_greater_than_75(marks_dict)

# Call the pop and display function to print the contents of the stack
print("Contents of the stack:")
pop_and_display_stack(stack_of_keys)
