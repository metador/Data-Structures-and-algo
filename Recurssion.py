def recu(n):

    if n==1:
        print
        print "-"
        return
    recu(n-1)

    print
    print "-"*n
    recu(n-1)
    return

recu(4)