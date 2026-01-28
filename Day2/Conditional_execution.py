try:
    score = float(input("Enter Score: "))
    if score < 0 or score > 1:  raise ValueError
except ValueError:
    print("Bad score")
    exit()

A_score,B_score,C_score,D_score,F_score = 0.9,0.8,0.7,0.6,0.6

if score >= A_score: print("A")
elif score >= B_score: print("B")
elif score >= C_score: print("C")
elif score >= D_score: print("D")
elif score < F_score: print("F")