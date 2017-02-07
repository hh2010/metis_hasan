def match_ends(words):
    return sum(map(lambda x: len(x)>=2 and (x[0] == x[-1]), words))

# Examples
print match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
print match_ends(['', 'x', 'xy', 'xyx', 'xx'])
print match_ends(['aaa', 'be', 'abc', 'hello'])

def front_x(words):
    a = sorted(filter(lambda x: x[0] == 'x', words))
    return a + sorted([x for x in words if x not in a])

# Examples
print front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
print front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
print front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])

def sort_last(tuples):
    return sorted(tuples, key=(lambda x: x[1]))

# Examples
print sort_last([(1, 3), (3, 2), (2, 1)])
print sort_last([(2, 3), (1, 2), (3, 1)])
print sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])

def remove_adjacent(nums):
    try: return ([nums[0]] + [nums[x]
    for x in range(1, len(nums)) if nums[x] != nums[x-1]])
    except: return nums

# Examples
print remove_adjacent([1, 2, 2, 3])
print remove_adjacent([2, 2, 3, 3, 3])
print remove_adjacent([3, 2, 3, 3, 3])
print remove_adjacent([])

# I found this way to do in linear time online
# I am trying to think of a way to do this using less code
def linear_merge(list1, list2):
    result = []
    i = j = 0
    total = len(list1) + len(list2)
    while len(result) != total:
        if len(list1) == i:
            result += list2[j:]
            break
        elif len(list2) == j:
            result += list1[i:]
            break
        elif list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result

# Examples
print linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
print linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
print linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
