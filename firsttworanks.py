mylist = []
high = 0
sec_high = 0
for _ in range( int( input( ) ) ):
    name = input( )
    score = float( input( ) )
    mylist.append( [name, score] )
    print( _ )
    if _ > 0:
        if mylist[_][_ + 1] >= mylist[_ + 1][_ + 1]:
            high = mylist[_][_ + 1]
            sec_high = mylist[_ + 1][_ + 1]
        else:
            high = mylist[_ + 1][_ + 1]
            sec_high = mylist[_][_ + 1]
print( mylist )
print( high )
print( sec_high )