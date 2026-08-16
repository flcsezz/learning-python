people = {
    
    'hokage' : ['konoha', 'notki' , 'yeski'],

    'tsuchikage' : ['land' ,'of' ,'mist'],
    
    'raikage' : ['land' , 'waves' , 'mortal'],

}

for peopl in people:
    places = people[peopl]


    print(f"\n\t{peopl.title()} Fav places are:")
    for places in places:
        print(f'\t>{places.title()}')
          

