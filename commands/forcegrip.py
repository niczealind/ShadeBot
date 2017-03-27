import random

def get_roll(inp):
    top = int(inp)
    randomNum = random.randint(1, top)
    return int(randomNum)

def get_message(name):
    top = int(5)
    result = get_roll(top)
    return_string = ''

    if (result == 1):
        return_string = "%s is picked up with Force Grip and tossed the edge!" % (name)

    if (result == 2):
        return_string = "%s is picked up with Force Grip, but they are able to break out!" % (name)

    if (result == 3):
        return_string = "%s is picked up with Force Grip and then released!" % (name)

    if (result == 4):
        return_string = "%s is picked up with Force Grip, BunkoJuice comes to their rescue!" % (name)

    if (result == 5):
        return_string = "Force Grip fails on %s!" % (name)
    
    return return_string
    
async def forcegrip(client, message):
        i = str(message.content).split(' ')
        name = i[1]
        fmessage = get_message(name)
        await client.send_message(message.channel, fmessage)
        
