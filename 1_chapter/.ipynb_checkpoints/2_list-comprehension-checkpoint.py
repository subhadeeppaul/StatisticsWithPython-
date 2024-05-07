# Define array1 using list comprehension
array1 = [(2*n + 1)**2 for n in range(1, 6)]

# Define array2 using list comprehension
array2 = [i**0.5 for i in array1]

# Print the types of the objects
print("UnitRange{Int64}    Array{Int64,1}    Array{Float64,1}")

# Print the values of the objects
print((list(range(1, 6)), array1, array2))