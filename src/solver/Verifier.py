def Verifier(MP,WP, matches):
    #Turn all the inputs into dict
    if isinstance(matches,dict):
        MtoW = dict(matches)
    else:
        MtoW = {}
        for m, w in matches:
            if m not in MtoW:
                MtoW[m] = w
            else:
                return "invalid"
    men = set(MP.keys())
    women = set(WP.keys())


    for m,w in MtoW.items():
        if w not in women:
            return "invalid"
        if m not in men:
            return "invalid"

    seenW = set()
    for m, w in MtoW.items():
        if w in seenW:
            return "invalid"
        seenW.add(w)

    WtoM = {w: m for m, w in MtoW.items()}
    Mranks = {
        m: {w: i for i, w in enumerate(pref_list)}
        for m, pref_list in MP.items()
    }
    Wranks = {
        w: {m: i for i, m in enumerate(pref_list)}
        for w, pref_list in WP.items()
    }

    #Checks Stability

    for m in men:
        if m not in MtoW:
            continue
        currentW = MtoW[m]

        for w in MP[m]:
            if w == currentW:
                break
            wcurrentm = WtoM.get(w, None)
            if wcurrentm is None:
                return "unbalnced"
            if Wranks[w][m] < Wranks[w][wcurrentm]:
                return "unbalnced"
    return "Valid"

def InputParser (input):
    output = {}
    for line in input.splitlines() :
         line = line.strip()
         M, W = line.split(" ")
         output[int(M)-1] = int(W)-1
    return output