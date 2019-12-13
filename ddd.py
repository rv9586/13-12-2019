def histo( items ):
    for n in items:
        p = ''
        t = n
        while( t > 0 ):
          p += '%'
          t = t - 1
        print(p)

histo([10, 10, 10, 10])
