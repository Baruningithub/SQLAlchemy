from main import Session,user

session=Session()

l=[{
    "username" : "Barun",
    "mail":"mail@ty"
    },
    {
    "username" : "Brun",
    "mail":"mail@t"
    },{
    "username" : "arun",
    "mail":"mal@ty"
    },{
    "username" : "Baru",
    "mail":"mailw@ty"
    },{
    "username" : "Barun",
    "mail":"ma@ty"
    },{
    "username" : "Baun",
    "mail":"mail@3ty"
    }
    
]

# new_user=user(id=1,name='BArun',email='mail@email')

# session.add(new_user)
i=0
for d in l:
    new_user=user(id=i,name=d['username'],email=d['mail'])
    session.add(new_user)
    i+=1
    session.commit()
