# Define a function
def binomial_coeff(n, r):
  # Since nC-1 and 4C5 gives 0 
    if r < 0 or r > n:
        return 0
  # Also nC0 and nCn gives 1
    if r == 0 or r == n:
        return 1
  # Two previous row from Pascal's triangle
    return binomial_coeff(n-1, r-1) + binomial_coeff(n-1, r)

# Make sure this part is outside the function!
result = binomial_coeff(7, 4)
print(result)
