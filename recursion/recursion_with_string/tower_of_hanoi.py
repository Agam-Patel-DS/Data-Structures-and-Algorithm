def tower_of_hanoi(n,source,destination,auxillary):
    if n==0:
        return
    if n==1:
        print(source,"==>", destination)
        return
    
    tower_of_hanoi(n-1,source,auxillary,destination)
    print(source,"==>",destination)
    tower_of_hanoi(n-1,auxillary,destination,source)


n=7
tower_of_hanoi(n, "Source", "Destination", "Auxilliary")