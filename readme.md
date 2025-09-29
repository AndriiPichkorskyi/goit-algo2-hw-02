# Homework Tasks

## Task 1: Find Min and Max (Divide and Conquer)

Implement a recursive function that finds the **minimum** and **maximum** elements in an array using the _divide and conquer_ method.

- Input: array of numbers of any length
- Output: tuple `(min, max)`
- Approach: recursion
- Time complexity: **O(n)**

Example:

```python
sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultMin, resultMax = findMinMax(sample)
print(resultMin, resultMax)  # 1 10
```

## Task 2: 3D Printer Queue Optimization

Develop a program to optimize the **queue of 3D printing jobs** considering task priorities and printer constraints.
A greedy algorithm is used to select print groups.

- Jobs have: `id`, `volume`, `priority`, `print_time`
- Printer constraints: `max_volume`, `max_items`
- Higher priority tasks are printed first
- Total print time = sum of the **maximum print time per group**

**Example Output:**

```json
{
  "print_order": ["M2", "M1", "M3"],
  "total_time": 270
}
```
