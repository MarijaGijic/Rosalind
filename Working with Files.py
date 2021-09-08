i = 1
f = open('rosalind_ini5 (1).txt')
for line in f.readlines():
    if i % 2 == 0 :
        print (line)
    i += 1 
    # prikazuju se pasusi na parnim mesti,a
