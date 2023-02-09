import numpy as np
import sys
import timeit
import functions


# python -m cProfile -s time valeurs_propres_diagnostiques.py

def main():
	args = sys.argv[1:]

	n = int(args[0] if len(args) > 0 else input("Which dimension do you want to study? "))
	i = int(args[1] if len(args) > 1 else input("To which diagnosis eigenvalue do you want to study? "))

	k = 2
	K = [k]
	Diag_critic_length = []

	t_0 = timeit.default_timer()
	for j in range(1, i):
		k = k + 2 * functions.mu(n, j)
		K.append(k)
		t_1 = timeit.default_timer()
		elapsed_time = round((t_1 - t_0) * 10 ** 3, 3)
		print(f"{j:02d}:", K, f"-- Elapsed time: {elapsed_time} ms")
		t_0 = timeit.default_timer()
		# first interval that we want to study
		X_j = np.linspace(0, 7, max(400, k))
		# for each value of L, find the sharp upper bound depending on n, k, L
		Y_j = []
		for l in X_j:
			Y_j.append(functions.sharp_upper_bound(n, k, l))
		if max(Y_j) > Y_j[-1]:
			diagnosis_eigenvalue_j = 1
		else:
			diagnosis_eigenvalue_j = -1
		Diag_critic_length.append(diagnosis_eigenvalue_j)

	print(Diag_critic_length)

	c = 0
	if Diag_critic_length[len(Diag_critic_length) - c - 1] == -1:
		print(
			f"In dimension {n}, the {K[len(Diag_critic_length) - c - 1]}th eigenvalue has a critical length at infinity.")

	while Diag_critic_length[len(Diag_critic_length) - c - 1] != -1:
		c = c + 1
		if Diag_critic_length[len(Diag_critic_length) - c - 1] == -1:
			print(
				f"In dimension {n}, from the eigenvalue number {K[len(Diag_critic_length)-c+1]} and to the {K[-1]+2*functions.mu(n, i)-1}th, I only found finite critical lengths.")


if __name__ == "__main__":
	main()
