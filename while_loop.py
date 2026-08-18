message = '\nEnter your Age to Know the ticket price:'

while True:
    prompt = int(input(message))


    if prompt <= 3:
        print('Your ticket is on us lil bro')
    elif prompt>3 and prompt <= 12:
        print('itll cost ya $10')
    elif prompt > 12:
        print('itll cost ya $15')
    else:
        print('enter a valid integer gng')
    