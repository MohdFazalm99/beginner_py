
# First Example is of 2d-list

number_grid = [
    [1,2,3],
    [2,4,3],
    [7,6,9],
    [0]
]

# In the above grid we are assigning numbers in rows and cols  and with that we can fetch any of these number using the index of that number of index of rows and cols.

print(number_grid[0][2])


# Second Example is of Nested loop

for row in number_grid:
    print(row)
    # here we are printing the entire grid using the loop

for row in number_grid:
    for col in row:
        print(col)
        # here we are printing the entire grid in col pattern


