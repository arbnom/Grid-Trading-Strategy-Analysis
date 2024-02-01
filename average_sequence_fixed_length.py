def generate_sequences(max_grid, num_hitted_grids):
    def recurse(seq, depth):
        if depth == 0:  # When the desired depth is reached, add the sequence
            if len(seq) == num_hitted_grids:  # Ensure the sequence has the exact length
                sequences.append(seq)
            return

        # Continue recursion only if the partial sum constraints are satisfied
        if sum(seq) + 1 <= max_grid:
            recurse(seq + [1], depth - 1)
        if sum(seq) - 1 >= -max_grid:
            recurse(seq + [-1], depth - 1)

    sequences = []
    recurse([], num_hitted_grids)  # Start recursion with the desired depth
    return sequences

def calculate_profit_loss(sequences, quantity_per_grid, diff_between_grids):
    total_profit_loss = 0

    for seq in sequences:
        L = len(seq)  # Length of the sequence
        S = sum(seq)  # Sum of the sequence
        impermanent_loss = quantity_per_grid * diff_between_grids * abs(((S - 1) * S) / 2)
        realized_profit = quantity_per_grid * diff_between_grids * (L - S) / 2
        profit_loss = realized_profit - impermanent_loss

        # Debug print statement for each sequence's calculations
        print(f"Sequence: {seq}, L: {L}, S: {S}, Impermanent Loss: {impermanent_loss}, Realized Profit: {realized_profit}, Profit/Loss: {profit_loss}")

        total_profit_loss += profit_loss

    return total_profit_loss / len(sequences) if sequences else 0

# Inputs
max_grid = 3
num_hitted_grids = 6  
quantity_per_grid = 1
diff_between_grids = 1

# Generate sequences
valid_sequences = generate_sequences(max_grid, num_hitted_grids)

# Calculate average profit/loss
average_profit_loss = calculate_profit_loss(valid_sequences, quantity_per_grid, diff_between_grids)

print(f"Average Profit/Loss: {average_profit_loss}")
