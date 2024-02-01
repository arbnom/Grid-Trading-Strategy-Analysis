def generate_and_evaluate_sequences(max_grid, num_hitted_grids, quantity_per_grid, diff_between_grids):
    def recurse(seq):
        if 0 < len(seq) <= num_hitted_grids:
            evaluate_sequence(seq)
        if len(seq) == num_hitted_grids:
            return

        # Extend the sequence with 1 and -1 and recurse
        if sum(seq) + 1 <= max_grid:
            recurse(seq + [1])
        if sum(seq) - 1 >= -max_grid:
            recurse(seq + [-1])

    def evaluate_sequence(seq):
        L = len(seq)
        S = sum(seq)
        impermanent_loss = quantity_per_grid * diff_between_grids * abs(((S - 1) * S) / 2)
        realized_profit = quantity_per_grid * diff_between_grids * (L - S) / 2
        profit_loss = realized_profit - impermanent_loss
        results.append(profit_loss)
        print(f"Sequence: {seq}, L: {L}, S: {S}, Impermanent Loss: {impermanent_loss}, Realized Profit: {realized_profit}, Profit/Loss: {profit_loss}")

    results = []
    recurse([])  # Start with an empty sequence

    # Calculate and return the average profit/loss
    return sum(results) / len(results) if results else 0

# Inputs
max_grid = 3
num_hitted_grids = 6
quantity_per_grid = 1
diff_between_grids = 1

# Generate sequences and calculate the average profit/loss
average_profit_loss = generate_and_evaluate_sequences(max_grid, num_hitted_grids, quantity_per_grid, diff_between_grids)
print(f"Average Profit/Loss: {average_profit_loss}")
