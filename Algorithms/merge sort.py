test = [3453, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554, 34534, 23, 2222, 345363, 34664, 56757, 45345, 567567, 35, 2, 2, 22, 35345, 46456456456546456, 456456, 5, 394, 45, 34346, 5, 5756554]
test2 = [2, 4, 8, 6, 5, 7, 1, 3]
test3 = [4, 8, 2, 6, 5]


def m_sort(x):
    if len(x) < 2:
        return x
    x1 = m_sort(x[:len(x)/2])
    x2 = m_sort(x[len(x)/2:])
    sorted_x = []
    lx1, lx2 = len(x1), len(x2)
    i = 0
    j = 0
    while True:
        if x1[i] < x2[j]:
            sorted_x.append(x1[i])
            if i >= lx1-1:
                sorted_x += x2[j:]
                break
            i +=1
        else:
            sorted_x.append(x2[j])
            if j >= lx2-1:
                sorted_x += x1[i:]
                break
            j += 1
    return sorted_x

