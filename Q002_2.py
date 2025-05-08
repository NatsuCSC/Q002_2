S = str(input())
piano = ['d','r','m','f','s','l','c' ]
playsec = abs(piano.index(S[0]) - piano.index('m'))

for i in range(len(S)):
    playsec += 1
    if S[i] != S[i-1] and i > 0:
        playsec += abs(piano.index(S[i]) - piano.index(S[i-1]))
else:
    print(playsec)
