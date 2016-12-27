def answer(h, q):
    p = [None] * len(q)
    
    def findIt(h, missingZ, stateFactor, count):
        max = (2**h) - 1
        maxhalf = max/2

        print 'h: ', h, "missingZ:", missingZ, "maxhalf: ", maxhalf ," stateFactor:",  stateFactor 
        #base
        if missingZ == maxhalf + stateFactor:
            return max + stateFactor
        elif missingZ == maxhalf*2 + stateFactor:
            return max + stateFactor

        
        if missingZ < maxhalf+stateFactor:
            stateFactor += 0
        else:
            stateFactor += maxhalf

        return findIt(h-1, missingZ, stateFactor, count+1)


    for missingZ in q:
        cornerCase = (2**h) - 1
        if cornerCase == missingZ:
            p[q.index(cornerCase)] = -1
        else:
            p[q.index(missingZ)] = findIt(h, missingZ, 0, 0)


    return p




h = 5
q = [27]
print answer( h, q )
