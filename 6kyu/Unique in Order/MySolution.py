def unique_in_order(iterable):
    li = []
    li[:0] = iterable
    if len(li) > 0:
        li2 = [li[0]]
        for x in range(1,len(li)):
            if li[x] != li[x-1]:
                li2.append(li[x])
        return li2
    else:
        return []
