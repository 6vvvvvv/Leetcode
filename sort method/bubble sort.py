def bubble_sort(list):
    n = len(list)
    for i in range(0,n-1):
        count = 0
        for j in range(i, n-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                count+=1
        if count == 0:
             break

def main():
    list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("list:%s" % list)
    bubble_sort(list)
    print("new list:%s" % list)

if __name__ == '__main__':
    main()

    # for i in range(1,n):
    #     for j in range(0,n-i):
    #         swap


    # def bubble_sort(origin_items, comp=lambda x, y: x > y):
    # items = origin_items[:]
    # for i in range(len(items) - 1):
    #     swapped = False
    #     for j in range(i, len(items) - 1 - i):
    #         if comp(items[j], items[j + 1]):
    #             items[j], items[j + 1] = items[j + 1], items[j]
    #             swapped = True
    #     if swapped:
    #         swapped = False
    #         for j in range(len(items) - 2 - i, i, -1):
    #             if comp(items[j - 1], items[j]):
    #                 items[j], items[j - 1] = items[j - 1], items[j]
    #                 swapped = True
    #     if not swapped:
    #         break
    # return items
