current_users = ['admin','jojo', 'kela','aalo','notaalo']

new_users = ['papaya', 'notpapaya','kela','aalo']
if current_users:
    current_users_lower= [usr.lower() for usr in current_users]
    for users in new_users:

        if users.lower() in current_users_lower:
            print(f"username{users} is not available to use")
        else:
            print(f"username available")    
else:
    print("we need to find some users!!!!!")