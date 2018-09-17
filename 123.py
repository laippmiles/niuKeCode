while 1:
    a=[]
    s = input()
    if s != "":
        a.append(int(s))
        for i in range(2):
            s = input()
            if s != "":
                for x in s.split():
                    a.append(int(x))
        year = a[0]
        month = a[1]
        day = a[2]
        print(a)
        monthperday = [31,28,31,30,31,30,31,31,30,31,30]
        if (year%4 == 0 and year % 100 != 0) and year % 400 ==0:
            monthperday[1] = 29
        count = day
        for i in range(month):
            count += monthperday[i]
        print('This day is the first year of the year is: the '+ str(count)+' day')
    else:
        break
