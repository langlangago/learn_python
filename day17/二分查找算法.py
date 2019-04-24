
def find(l, num, start=0, end=None):
    end = len(l)-1 if end is None else end
    middle = (start+end)//2
    if num == l[middle]:
        return middle
    elif num < l[middle]:
        end = middle-1
    else:
        start = middle+1
    if start > end:
        return 'No this value.'
    return find(l, num, start, end)


l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(find(l, 19))
