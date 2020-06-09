def selection_sort(list1):
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			if list1[j]<list1[i]:
				list1[i],list1[j]=list1[j],list1[i]
				
def main():
	list1=[8,7,9,5,4,3]
	selection_sort(list1)
	print(list1)

if __name__ == '__main__':
	main()

# def select_sort(origin_items, comp=lambda x, y: x < y):
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items



# 选择排序法
nums = [4, 1, 5, 10, -1, 9, 3, 2, 13, 7]
 
count = len(nums)   # count等于nums的长
for i in range(count-1):
    min = i
    for j in range(i+1, count):  # 将剩下的进行遍历，遍历到count
        if nums[min] > nums[j]:
            min = j
    if min != i:    # 若最小值不等于i，进行交换
        t = nums[i]
        nums[i] = nums[min]
        nums[min] = t
 
print(nums
————————————————
版权声明：本文为CSDN博主「牢房看管」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43778797/java/article/details/90242480
