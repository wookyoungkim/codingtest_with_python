from bisect import bisect_left

n = input()
dest = list(map(int, input().split()))
link = []
print(dest)
for d in dest:
    print(d, link, ": ")
    if not link or link[-1] < d:
        link.append(d)
    else:
        print(bisect_left(link, d))
        link[bisect_left(link, d)] = d
print(link)       
print(len(link))