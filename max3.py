#demonstrates largest number among 3 numbers
if __name__ == "__main__":
    a,b,c=None,None,None
    a=int(raw_input("Enter a value"))
    b=int(raw_input("Enter b value"))
    c=int(raw_input("Enter c value"))
if a>b and a>c:
    print "%d is big" %a
elif b>c:
    print "%d is big" %b
else:
    print "%d is big" %c
