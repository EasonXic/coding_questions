# insert
def insert_sort(nums):
    # in place    implement based on vector
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        index_i=0
        for j in range(i):
            if nums[i]>=nums[i-j-1]:
                index_i=i-j
                break
        nums[index_i:i+1]=[nums[i]]+nums[index_i:i]
    return nums

# select
def select_sort(nums):
    # in place    implement based on vector
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)-1):
        MIN = nums[i]
        min_index=i
        for j in range(i+1,len(nums)):
            if nums[j]<MIN:
                MIN=nums[j]
                min_index = j
        nums[min_index] = nums[i]
        nums[i] = MIN
    return nums

# bubble
def bubble_sort(nums):
    # in place    implement based on vector
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)):
        all_sorted=True
        for j in range(len(nums)-1,0,-1):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]
                all_sorted=False
        if all_sorted:
            break
    return nums

# merge
def merge(nums1,nums2):
    i=0
    j=0
    temp=[]
    while(i<len(nums1) or j<len(nums2)):
        if i==len(nums1):
            temp.append(nums2[j])
            j += 1
        elif j==len(nums2):
            temp.append(nums1[i])
            i += 1
        elif nums1[i]<=nums2[j]:
            temp.append(nums1[i])
            i += 1
        else:
            temp.append(nums2[j])
            j += 1
    return temp
def merge_sort(nums):
    if len(nums)<=1:
        return nums
    sub_1=merge_sort(nums[:len(nums)//2])
    sub_2=merge_sort(nums[len(nums)//2:])
    return merge(sub_1,sub_2)

# Shell
# 循环很多，但其实复杂度不高
def Shell_sort(nums):
    if len(nums)<=1:
        return nums
    gap=len(nums)//2
    while(gap>=1):
        for i in range(gap): # i表示第几组，对于一个给定的gap一共有gap组
            index_start=i # 第i组第一个元素开始的编号
            index=index_start+gap # index表示每个组内的指针，从组内第二个迭代到最后一个
            # 插入排序
            while index<len(nums): 
                j=index  # j表示index指向的元素，在向前比较过程中的指针
                while j>index_start: 
                    if nums[j]<nums[j-gap]:
                        nums[j],nums[j-gap]=nums[j-gap],nums[j]
                        # 不采用整体移位实现插入排序，每次交换法实现插入排序
                        j-=gap
                    else:
                        break
                index+=gap # 进行完一个位置的比较和插入后，向后移一个单位
        gap//=2 # 每次gap减半
    return nums

# quick sort 
def quick_sort(nums,start,end):  # 数组就地排序，[start,end)
    if start>=end:
        return
    pivot=nums[start]   # 数组选第一个值为pivot
    i=start # left pointer，一开始pivot的pointer也是i
    j=end-1 # right pointer
    
    # 主循环
    # 开始时p=i比较右边,当发现nums[j]更小时,交换pivot(即nums[i])和nums[j],并开始比较左边
    while i<j:  # 结束标志是i==j(此时i=j=p)
        while nums[j] >= pivot and i<j:
            j -= 1
        if i < j:   # 发现nums[j]更小时,交换pivot(即nums[i])和nums[j],结果是p=j,并开始比较左边
            nums[j], nums[i] = nums[i], nums[j]
            i += 1 # 原来左指针位置是换过来的元素，因而左指针右移一位
        while nums[i] <= pivot and i<j:
            i += 1
        if i < j:  # 发现nums[i]更大时,交换pivot(即nums[j])和nums[i],结果是p=i,并开始比较右边
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1 # 原来右指针位置是换过来的元素，因而右指针右移一位
    quick_sort(nums,start,i) # 递归左子序列
    quick_sort(nums,i+1,end) # 递归右子序列
    return nums[start:end]

# heap      in place
def heap_sort(array):
    first = len(array) // 2 - 1
    # 1.堆构建 Floyd算法（自底向上调整O(n)）
    for start in range(first, -1, -1):
        # 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
        big_heap(array, start, len(array) - 1)
    # 2.删除+下滤
    for end in range(len(array) - 1, 0, -1):
        # 交换堆顶和堆尾的数据
        array[0], array[end] = array[end], array[0]
        # 重新调整完全二叉树，构造成大顶堆
        big_heap(array, 0, end - 1)
    return array
def big_heap(array, start, end): # 下滤算法：置换+下滤
    # Floyd算法中一次调整的步骤，对一个给定的root节点下滤调整到底
    root = start
    # 左孩子的索引
    child = root * 2 + 1
    while child <= end:
        # 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            # 交换节点与子节点中较大者的值
            array[root], array[child] = array[child], array[root]
            # 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
            root = child
            child = root * 2 + 1
        else:
            break
# backet
nums,result = [19,21,23,14,35,49,37,59,10,16],[]
minv,maxv = min(nums),max(nums) #找出所有元素中的最小值和最大值
countn = [0]*(maxv-minv+1) #算出需要桶的最大个数
for i in nums:
    countn[i-minv] += 1 #桶的编号与对应元素不一致，需要通过计算调整
for i in range(1,len(countn)):
    if countn[i]:
        result += [i+minv]*countn[i]
print(result)