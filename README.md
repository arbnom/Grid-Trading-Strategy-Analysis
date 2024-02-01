# Grid Trading Strategy Analysis

This repository contains Python scripts designed to analyze various aspects of grid trading strategies using sequences of -1 and 1 to represent trading grid hits. Each script focuses on a different aspect of grid trading analysis, calculating the average results of sequences, and evaluating the performance of specific subsequences within a given sequence.

## Scripts Overview

### `average_sequence_upto_length.py`

- **Purpose**: Generates all valid sequences of -1 and 1 with lengths up to a specified number (`num_hitted_grids`), ensuring the partial sums of these sequences stay within the predefined range (`-max_grid` to `+max_grid`). It calculates the average result for these sequences.
- **Key Formulas**:
  - **Realized Profit**: `quantity_per_grid * diff_between_grids * (L - S) / 2`
  - **Impermanent Loss**: `quantity_per_grid * diff_between_grids * abs(((S - 1) * S) / 2)`

### `average_sequence_fixed_length.py`

- **Purpose**: Similar to the first script but generates sequences of a fixed length (`num_hitted_grids`). It calculates the average result for these sequences using the same formulas for realized profit and impermanent loss.

### `longest_valid_subsequence_result.py`

- **Purpose**: Identifies the longest subsequence within a given sequence of -1 and 1 that does not exceed the `max_grid` value in partial sums. It calculates the result for this subsequence using the realized profit and impermanent loss formulas.

## Understanding the Formulas

- **Realized Profit**: Represents the profit realized from the grid hits. It is calculated as the product of the quantity per grid, the difference between grids, and half the difference between the length of the sequence and its sum.
- **Impermanent Loss**: Reflects the loss incurred due to price deviation within the grid. It is calculated as the product of the quantity per grid, the difference between grids, and half the absolute value of the product of the sum of the sequence minus one and the sum itself.

## Future Resources

I am currently preparing a detailed blog post that will explain the concepts of realized profit and impermanent loss within the context of grid trading strategies. This post will explore the mathematics and practical implications of these formulas in depth. Once published, the link to this post will be added here for further reading.
