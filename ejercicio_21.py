vector_a = [1, 2, 3]
vector_b = [-1, 0, 2]

scalar_product = 0

for z in range(len(vector_a)):
    scalar_product += vector_a[z] * vector_b[z]

print("El producto escalar de los vectores:\n-",vector_a, "\n-",vector_b, "\nEs igual a", scalar_product)
