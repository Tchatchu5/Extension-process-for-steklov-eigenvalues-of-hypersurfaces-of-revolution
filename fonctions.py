from numpy import *

#factoriel function
def factorial(N):
    if N == 0:
        return 1
    else:
       return N*factorial(N-1)

#function multiplicity of the Laplace eigenvalues on a sphere
def mu(n, k):
    return int((n+2*k-2)*factorial(n+k-3)/(factorial(k)*factorial(n-2)))

print(mu(8,0))


#Steklov - Dirichlet eigenvalue on an annulus
def sigma_dirichlet(n, D, L):
    return ((n+D-2)*(1+L/2)**(2*D+n-2)+D)/((1+L/2)**(2*D+n-2)-1)

#Steklov - Neumann eigenvalue on an annulus
def sigma_neumann(n, N, L):
    return N*((N+n-2)*((1+L/2)**(2*N+n-2)-1))/(N*(1+L/2)**(2*N+n-2)+N+n-2)



#function which return the integer l_0 in the extension process
def l_0(n, k):
    list = []
    for i in range(0, k + 1):
        list.append((mu(n, i)))
    sum = 0
    j = 0
    for i in range(0, k + 1):
        if sum + list[i] > k:
            return j
        sum = sum + list[i]
        j = j + 1
    return None


#function which return the integer l_1 in the extension process
def l_1(m2_list: list, k: int) -> int:
    """Compute the L_1 number representing the number of incremental addition to perform from M2's list values in order to
    go above or equal to K

    Args
    ----
        * m2_list: list of M sorted according to its respective value in E
        * K: Knt eigenvalue

    Returns
    ----
        The number of additions performed
    """
    i, accumulator = 0, 0
    while accumulator < k:
        accumulator += m2_list[i]
        i+=1
    #Reverse latest addition that brought us above K
    return i-1


#function which gives the sharp upper bound in the extension process
def sharp_upper_bound(n, k, L):
    E=[]
    for i in range(0, l_0(n,k)+1):
        E.append(sigma_dirichlet(n, i, L))
    for i in range(1, l_0(n,k)+2):
        E.append(sigma_neumann(n, i, L))


    M=[]
    for i in range(0, l_0(n,k)+1):
        M.append(mu(n,i))
    for i in range(1, l_0(n,k)+2):
        M.append(mu(n,i))

    #print(f"Before, e:{E}\nm:{M}")

    link_dict = {}
    for i in range(len(E)):
        key = E[i]
        value = M[i]
        try:
            link_dict[key].append(value)
        except KeyError as e:
            link_dict[key] = [value]

    #print(f"Link dict: {link_dict}")

    E.sort()
    M2 = [link_dict[e_value].pop(0) for e_value in E]

    l1 = l_1(M2, k)

    #print(f"sorted E: {E}\nSorted M2:{M2}")

    #print(f"Computing addition number to obtain a value >= K")

    return E[l1]
    #print(f"From list: {M2}, There need to be {l1} addition to obtain accumulator >= K = {k}")
    #print(f"From list {E}, at index {l1} = {E[l1]}")


