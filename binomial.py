def binomial_coeff(n, r):
  # Condition 1, when we get something like nC-1 or 3C4
    if r < 0 or r > n:
        return 0
  # Condition 2, when we gte things like nC0 or nCn
    if r == 0 or r == n:
        return 1
  # Adding the two previous terms in the Pascal's triangle.
    return binomial_coeff(n-1, r-1) + binomial_coeff(n-1, r)

# Take input from users
n = int(input("Enter n (total number of items): "))
r = int(input("Enter r (items to choose): "))

# Calculate and print result
result = binomial_coeff(n, r)
print(f"Binomial Coefficient C({n}, {r}) = {result}")



