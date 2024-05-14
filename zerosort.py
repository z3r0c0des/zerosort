def fun(arr):
    temp=[]
    main=[]
    temp.append(arr[0])
    for i in range (1,len(arr)):
        if arr[i]>arr[i-1]:
            temp.append(arr[i])
        else:
            main.append(temp)
            temp=[]
            temp.append(arr[i])
    main.append(temp)
    cook=[]
    peep=funt(main,cook)
    return peep
def funt(main,cook):
    a=0
    mini=0
    while(main!=[]):
        mini= main[0][0]
        a=0
        for i in range(len(main)):
            if main[i][0]<mini:
                mini=main[i][0]
                a=i
        cook.append(mini)
        main[a].remove(mini)
        if [] in main:
            main.remove([])

    return cook
ar=[0,2,5,6,7,13,4]
t=fun(ar)
print(t)