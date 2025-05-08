S = str(input())
piano = ['d','r','m','f','s','l','c' ]
playSec = abs(piano.index(S[0]) - piano.index('m'))

for i in range(len(S)):
    playSec += 1
    if S[i] != S[i-1] and i > 0:
        playSec += abs(piano.index(S[i]) - piano.index(S[i-1]))
else:
    print(playSec)
