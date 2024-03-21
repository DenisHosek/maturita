def vyp_dnu(a, b,c,d,e,f):
    if c == f:
        days = (e-b) * 30 + (d-a)
    else:
        years = f - c
        days = (12 -b) * 30 + (31-a) + (e-1) * 30 + (d-1)
        if years > 1:
            for i in range(years):
                days += 360
    return days