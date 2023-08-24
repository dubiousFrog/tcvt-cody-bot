def handle_response(message) -> str:
    p_message = message.lower()

    if "ball" in p_message:
        return "WOOF WOOF BARK WOOF WOOF BARK"
    if '<@1144323023923585115>' in p_message:
        return "Woof"
    #return 'Woof'
'''
    if p_message == "hello":
        return 'hey there'
    
    if p_message == 'roll':
        return str(random.randint(1, 6))
    
    if p_message == '!help':
        return "`This is a help message you can modify`"
''' 
