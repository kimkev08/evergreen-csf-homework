n = 100
f = 0
j = 1
k = 0
l = 0

series = "fibonacci"

if (series == "fibonacci"):
    for i in range (0, n):
         f = j + k
         j = k
         k = f
         print i, f
         
 
elif (series == "sum"):
    for i in range (0, n+1):
        l = l + 3
        print l

else:
    print "invalid string"
    
## colaberators: Cliff