import numpy as np

import functions


n=int(input("Which dimension do you want to study?"))
k=int(input("To which eigenvalue do you want to check?"))

#interval that we want to study
X = np.linspace(0, 7, max(400, k**2))
Y=[]
for m in range(1, k+1):
    Y_m=[]
    # for each value of L, find the sharp upper bound depending on n, m, L
    for l in X:
        Y_m.append(functions.sharp_upper_bound(n,m,l))


    #find the critical length
    ym_max_index = Y_m.index(max(Y_m))
    if max(Y_m) > Y_m[-1]:
        critical_length_m = X[ym_max_index]
    else:
        critical_length_m = -1

    Y.append(critical_length_m)
#print(Y)

#find the largest index which is equal to -1
i = 0
if Y[len(Y) - i - 1] == -1:
    print(f"In dimension {n}, the {k}th eigenvalue has a critical length at infinity.")
while Y[len(Y)-i-1] != -1:
    i=i+1
    if Y[len(Y)-i-1] ==-1:
        print(f"In dimension {n}, from the eigenvalue number {len(Y)-i+1} and to the {k}th, I only found finite critical lengths.")



