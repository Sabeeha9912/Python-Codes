# tuple intersection
def tuple_intersect(t1,t2):
    print("1st tuple is:",t1)
    print("2nd tuple is:",t2)
    intersections=tuple(set(t1).intersection (set(t2)))
    return intersections
t1=(1,2,3,4,5)
t2=(3,4,5,6)
result=tuple_intersect(t1,t2)
print(result)
