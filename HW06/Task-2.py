# Объедините все списки в списке в один отсортированный список и верните только повторяющиеся элементы.
#Input: lists = [[1,4,5],[2,4,7],[1,2,6]]
#Output: [1,2,4]
lists = [[1,4,5],[2,4,7],[1,2,6]]
res = [x for l in lists for x in l]
lst=list(filter(lambda x: res.count(x)>1, res))
result = {x for x in lst if lst.count(x)>1}
print(result) # множество еще само отсортировало список и вывела только 1 раз повторяющийся список