names = ["Jojo","naruto","mibombe"]
print(f"first is {names[0].title()}")
print(f"second is {names[1].title()}")
print(f"third is {names[2].upper()}")

print(f'unfortunatrly {names[2]} will not be coming ')

names[2] = 'Albert Newton'
nini = sorted(names, reverse=True)

print(f'heres the new invite list{names}')

print('found a bigger sea')

names.insert(0,'sasuke')
names.insert(1,'gian')
names.append('sizu')
print(f'fourth is {names[0].title()}')
print(f'fifth is {names[1].title()}')
print(f'sixth is {names[-1].title()}')

print(names)


print('ouuu shi the sea was fake now can only inv 2 TT')

one=names.pop(1)
two=names.pop(1)
thr = names.pop(2)
four = names.pop(2)

print(f"sorry we cant inv you TT {one}")
print(f"sorry we cant inv you TT {two}")
print(f"sorry we cant inv you TT {thr}")
print(f"sorry we cant inv you TT {four}")

print(f"you 2 are still invitedd  {names}")