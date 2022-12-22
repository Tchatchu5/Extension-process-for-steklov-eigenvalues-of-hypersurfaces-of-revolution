from numpy import *

import fonctions


n=int(input("Which dimension do you want to study?"))
i = int(input("To which diagnosis eigenvalue do you want to study?"))

k = 2
K=[]
Diag_critic_length=[]
for j in range(1, i):
    k = k+ 2*fonctions.mu(n, j)
    K.append(k)
    print(K)
    # first interval that we want to study
    X_j = linspace(0, 7, max(400, k))
    # for each value of L, find the sharp upper bound depending on n, k, L
    Y_j = []
    for l in X_j:
        Y_j.append(fonctions.sharp_upper_bound(n, k, l))
    if max(Y_j) > Y_j[-1]:
        diagnosis_eigenvalue_j = 1
    else:
        diagnosis_eigenvalue_j = -1
    Diag_critic_length.append(diagnosis_eigenvalue_j)
print(Diag_critic_length)
c = 0
if Diag_critic_length[len(Diag_critic_length) - c - 1] == -1:
    print(f"In dimension {n}, the {K[len(Diag_critic_length) - c - 1]}th eigenvalue has a critical length at infinity.")
while Diag_critic_length[len(Diag_critic_length)-c-1] != -1:
    c=c+1
    if Diag_critic_length[len(Diag_critic_length)-c-1] ==-1:
        print(f"In dimension {n}, from the eigenvalue number {K[len(Diag_critic_length)-c]} and to the {K[-1]}th, I only found finite critical lengths.")


