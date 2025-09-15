import math

import math

def sigmoid(num: float) -> float:
    return 1 / (1 + math.exp(-num))

example_vector_sums = [200, 1, -200, 2, 20, -100]

def main(): 
    for i in example_vector_sums:
        print(f"sigmoid({i}) = {sigmoid(i)}")

if __name__ == "__main__":
    main()
