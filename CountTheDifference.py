count = input()
List = map(int, input().split)
List.sort()

dif = abs(List[0] - List[1])
for i in range(0, len(List)-1):
    if dif > abs(List[i+1] - List[i]):
        dif = abs(List[i+1] - List[i])

for i in range(0, len(List) - 1):
    if dif == abs(List[i+1] - List[i]):
        print List[i], List[i+1],
