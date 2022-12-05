file1 = open('CalorieList.txt')
Lines = file1.readlines()
Lines = [line.strip() for line in Lines]
num = [i for i, x in enumerate(Lines) if x=='']  # [3,5,8,12], occurence of '' in Lines
num.insert(0,0)  # insert 0
num.insert(len(Lines)+1,len(Lines))  # insert last element position
ElfCalorie = []
for i in range(1,len(num)-1):  # separate out lists using '' as marker
    if i ==1:
        ElfCalorie.append(Lines[0:num[1]])
    ElfCalorie.append(Lines[num[i]+1:num[i+1]])
ElfCalorie = [list(map(int, Food)) for Food in ElfCalorie]  # typecast to integers
SumList = [sum(Food) for Food in ElfCalorie]  # sum up individual lists
print(f"The elf with the most calories has {max(SumList)} calories.")
SortedSumList = sorted(SumList)[len(SumList)-3:len(SumList)+1]
print(f"The top three elves combined have {sum(SortedSumList)} calories.")
