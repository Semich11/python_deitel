def product(*arr):
    product = 1
    for i in arr:
        product *= i
    return product

# print(product(1,2,3,4))