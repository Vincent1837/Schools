import math

def log(x):
    if x == 0:
        return 0
    else :
        return math.log(x, 2)

# 4 samples
x1 = [1, 6, 12, 1]
x2 = [5, 2, 6, 2]
x3 = [7, 8, 9, 1]
x4 = [3, 4, 3, 2]
samples = [x1, x2, x3, x4]

scores = []

def dft(B=4):
    # iterate through feature dimentions
    for i in range(3):

        # Training Sample Partitioning 
        maximum = max(x[i] for x in samples)
        minimum = min(x[i] for x in samples)
        bins = [minimum + b/B * (maximum - minimum) for b in range(1, B)]

        # DFT Loss Measured by Entropy 
        entropys = []
        for b in bins:
            left_subset = [x[0] for x in enumerate(samples) if x[1][i] <= b]
            right_subset = [x[0] for x in enumerate(samples) if x[1][i] > b]

            left_entropy = right_entropy = 0
            # left entrpy
            class1 = class2 = 0
            for x in left_subset:
                if samples[x][3] == 1:
                    class1 += 1
                else: 
                    class2 += 1
            p1 = class1 / len(left_subset)
            p2 = class2 / len(left_subset)
            left_entropy = -p1*log(p1)-p2*log(p2)

            # right entropy
            class1 = class2 = 0
            for x in right_subset:
                if samples[x][3] == 1:
                    class1 += 1
                else: 
                    class2 += 1
            p1 = class1 / len(right_subset)
            p2 = class2 / len(right_subset)
            right_entropy = -p1*log(p1)-p2*log(p2)

            # weighted average of left and right entropys
            entropy = (len(left_subset)*left_entropy + len(right_subset)*right_entropy)/4
            entropys.append(round(entropy, 2))


        scores.append(min(entropys))
dft()
print(scores)

