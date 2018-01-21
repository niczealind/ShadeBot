import random

def get_roll(inp):
    top = int(inp)
    randomNum = random.randint(1, top)
    return int(randomNum)

def get_message(name):
    top = int(10)
    result = get_roll(top)
    return_string = ''

    if (result == 1):
        return_string = "%s is taken into Shadebot's arms and held closely." % (name)

    if (result == 2):
        return_string = "Shadebot embraces %s tightly and refuses to let go." % (name)

    if (result == 3):
        return_string = "%s is picked up with a bear hug and is then released." % (name)

    if (result == 4):
        return_string = "%s is picked up in a hug and is swung around." % (name)

    if (result == 5):
        return_string = "Shadebot refuses to hug %s!" % (name)
        
    if (result == 6):
        return_string = "Shadebot tried to hug %s, but they run away." % (name)
        
    if (result == 7):
        return_string = "%s is tossed into the air then caught in a hug by Shadebot." % (name)
        
    if (result == 8):
        return_string = "Shadebot refuses to hug %s, give them a fist bump instead." % (name)
        
    if (result == 9):
        return_string = "Shadebot and %s run towards each other and they both jump and catch each other mid air." % (name)
        
    if (result == 10):
        return_string = "Shadebot hugs %s, and gently caresses their back." % (name)
    
    return return_string
    
async def hug(client, message):
        i = str(message.content).split(' ')
        name = i[1]
        fmessage = get_message(name)
        await client.send_message(message.channel, fmessage)
        
