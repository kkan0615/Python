#Find a 'the' in essay
#Must be find 'the', not a their, them, etc
#Split function will make 'essay' valiable to list.

essay = input().lower().replace(',' , '').replace('.', '').split()
counts = 0

counts = essay.count('the')

print(essay)
print(counts)

