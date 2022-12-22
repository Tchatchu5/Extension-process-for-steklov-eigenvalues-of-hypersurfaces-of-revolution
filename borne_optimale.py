from numpy import *
import fonctions


n=int(input("Quelle dimension voulez-vous étudier ?"))
k=int(input("Quelle valeur propre voulez-vous étudier ?"))
L=float(input("Quelle longueur voulez-vous étudier ?"))

print(f"La borne optimale pour la {k}-ème valeur propre de Steklov d'une hypersurface de révolution du monde euclidien, dont la longueur du méridien est {L} et de dimension {n} est {fonctions.sharp_upper_bound(n, k, L)}")