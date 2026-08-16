should_poll = [
    'john', 'sera', 'siera', 'tame', 'impala',
]

took_pool = {'john' : "C", 'tame':"rust" , 'sera':"C++"}


for u in should_poll:
    if u in took_pool:
        l=took_pool[u]


        print(f"thanks {u.title()} for taking the poll and your fav is {l.title()}\n")
    else:
        print(f"Hey {u.title()} You havent took the pool yet pls do asap\n")