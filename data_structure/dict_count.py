count = dict()
names = ['csev','cwen','csev','zhen','cwen']
for name in names:
    # if name not in count:
    #     count[name] = 1
    # else:
    #     count[name] = count[name] + 1
    count[name] = count.get(name, 0) + 1
print(count)