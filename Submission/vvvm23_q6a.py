def merge_sort_hybrid(l):
    if len(l) <= 4:
        return selection_sort(l)

    mid = len(l) // 2
    left = merge_sort_hybrid(l[:mid])
    right = merge_sort_hybrid(l[mid:])

    return merge(left, right)

def merge(left, right):
    count = 0
    out = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            count += 1
            if left[0] <= right[0]:
                out.append(left[0])
                left = left[1:]
            else:
                out.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            out = out + left
            left = []
        else:
            out = out + right
            right = []
    return out

def selection_sort(l):
    for i in range(0, len(l) - 1):
        elem = l[i]
        pos = i
        for j in range(i+1, len(l)):
            if l[j] < elem:
                elem = l[j]
                pos = j
        
        l[i], l[pos] = l[pos], l[i]

    return l