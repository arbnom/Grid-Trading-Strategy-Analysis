def find_longest_valid_subsequence(sequence, max_grid):
    start_index = 0
    max_length = 0
    max_subseq = []

    partial_sum = 0
    for i, value in enumerate(sequence):
        partial_sum += value
        if partial_sum > max_grid or partial_sum < -max_grid:
            current_length = i - start_index
            if current_length > max_length:
                max_length = current_length
                max_subseq = sequence[start_index:i]
            partial_sum -= value
            start_index = i

    current_length = len(sequence) - start_index
    if current_length > max_length:
        max_subseq = sequence[start_index:]

    return max_subseq

def calculate_subsequence_result(subsequence, quantity_per_grid, diff_between_grids):
    L = len(subsequence)
    S = sum(subsequence)
    impermanent_loss = quantity_per_grid * diff_between_grids * abs(((S - 1) * S) / 2)
    realized_profit = quantity_per_grid * diff_between_grids * (L - S) / 2
    result = realized_profit - impermanent_loss

    print(f"Subsequence: {subsequence}, L: {L}, S: {S}, Impermanent Loss: {impermanent_loss}, Realized Profit: {realized_profit}, Result: {result}")
    
    return result

# Example usage
sequence = [1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, 1]
max_grid = 5  # Example max grid value
quantity_per_grid = 0.1  # Example quantity per grid
diff_between_grids = 10  # Example difference between grids

# Find the longest valid subsequence
longest_subseq = find_longest_valid_subsequence(sequence, max_grid)

# Calculate the result for the longest valid subsequence
subsequence_result = calculate_subsequence_result(longest_subseq, quantity_per_grid, diff_between_grids)
