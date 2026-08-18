message = "what toppings whould you like?\n"
prompt = ""
while prompt != 'quit':
    prompt= input(message)
    if prompt != 'quit':
        print(f'ok we`ll add {prompt.title()} at you pizzy !!\n')
    else:
        print('Quitting the program')
        
