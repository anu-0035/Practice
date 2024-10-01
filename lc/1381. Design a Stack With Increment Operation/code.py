class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []  # Initialize the stack as an empty list
        self.maxSize = maxSize  # Store the maximum size of the stack
        self.increment_list = [0] * maxSize  # Auxiliary list to handle increments efficiently

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)  # Add x to the top of the stack
        # If the stack is full, do nothing

    def pop(self) -> int:
        if not self.stack:
            return -1  # Return -1 if the stack is empty

        index = len(self.stack) - 1  # Get the top index of the stack
        pop_value = self.stack.pop() + self.increment_list[index]  # Adjust the popped value with the increment

        if index > 0:
            self.increment_list[index - 1] += self.increment_list[index]  # Pass the increment down to the previous element

        self.increment_list[index] = 0  # Reset the increment at this level since the value has been popped

        return pop_value

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack))  # Determine the limit of elements to increment
        if limit > 0:
            self.increment_list[limit - 1] += val  
