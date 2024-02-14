def find_longest_valid_subsequence(sequence, initial_grid_index, num_grids):
    start_index = 0
    max_length = 0
    max_subseq = []

    # Calculate the allowed range for partial sums based on the initial grid's position
    grids_below = initial_grid_index
    grids_above = num_grids - initial_grid_index - 1  # -1 because indices are 0-based

    partial_sum = 0
    for i, value in enumerate(sequence):
        partial_sum += value
        # Ensure the partial sum stays within the range defined by the initial grid's position
        if partial_sum > grids_above or partial_sum < -grids_below:
            current_length = i - start_index
            if current_length > max_length:
                max_length = current_length
                max_subseq = sequence[start_index:i]
            partial_sum -= value
            start_index = i

    # Check if the remaining part of the sequence after the last reset forms the longest valid subsequence
    current_length = len(sequence) - start_index
    if current_length > max_length:
        max_subseq = sequence[start_index:]

    return max_subseq

def calculate_subsequence_result(subsequence, quantity_per_grid, diff_between_grids):
    L = len(subsequence)
    S = sum(subsequence)
    impermanent_loss = quantity_per_grid * diff_between_grids *((abs(S) - 1) * abs(S)) / 2
    realized_profit = quantity_per_grid * diff_between_grids * (L - S) / 2
    result = realized_profit - impermanent_loss

    print(f"Subsequence: {subsequence}, L: {L}, S: {S}, Impermanent Loss: {impermanent_loss}, Realized Profit: {realized_profit}, Result: {result}")
    
    return result

# Example
sequence = [1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1]
initial_grid_index = 8  # Update based on the initial grid's position in your grid list
num_grids = 10  # Total number of grids in your position
quantity_per_grid = 0.1  # Example quantity per grid
diff_between_grids = 10  # Example difference between grids

# Find the longest valid subsequence considering the initial grid's position
longest_subseq = find_longest_valid_subsequence(sequence, initial_grid_index, num_grids)

# Calculate the result for the longest valid subsequence
subsequence_result = calculate_subsequence_result(longest_subseq, quantity_per_grid, diff_between_grids)
