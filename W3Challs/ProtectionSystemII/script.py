from z3 import *

s = Solver()
a1 = [Int(f"a1{i}") for i in range(10)]

s.add(a1[0] > 97, a1[0] < 112)
s.add(a1[1] > 97, a1[1] < 112)
s.add(a1[2] > 97, a1[2] < 112)
s.add(a1[3] > 97, a1[3] < 112)
s.add(a1[4] > 97, a1[4] < 112)
s.add(a1[5] > 97, a1[5] < 112)
s.add(a1[6] > 97, a1[6] < 112)
s.add(a1[7] > 97, a1[7] < 112)
s.add(a1[8] > 97, a1[8] < 112)
s.add(a1[9] > 97, a1[9] < 112)

s.add((a1[0] + a1[1] - a1[2] + a1[3] - a1[4]) == (a1[5] - a1[6] + a1[7] - a1[8] + a1[9]))
s.add((a1[0] + a1[1] + a1[2] + a1[3] + a1[4]) == (a1[5] + a1[6] + a1[7] + a1[8] + a1[9]))
s.add(a1[6] > a1[8], a1[9] > a1[7],a1[5] > a1[9])

# các giá trị khác nhau
s.add(Distinct(a1))

if s.check() :
    model = s.model()
    solution = [model.evaluate(a1[i]).as_long() for i in range(10)]
    print("Solution:", solution)
    print("your login :","".join(chr(so) for so in solution[:5]))
    print("your password :","".join(chr(so) for so in solution[5:]))

else:
    print("No solution found.")
