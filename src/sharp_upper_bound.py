import functions


n=int(input("Which dimension do you want to study?"))
k=int(input("Which eigenvalue do you want to study?"))
L=float(input("Which meridian length o you want to study?"))

print(f"The sharp upper bound for the {k}th Steklov eigenavlue of a hypersurface of revolution in the Euclidean space, with meridian length {L} and dimension {n} is {functions.sharp_upper_bound(n, k, L)}")