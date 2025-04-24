"""
xp_handler.py

Helper file to interact with the backend API server.

Brendan Dileo, April 2025
"""

import aiohttp 
from utils.levels import Level

API_URL = 'http://localhost:3001'

# Fetches the users rank based on amount of xp
def fetch_rank(xp: float):
    # Sort levels by xp highest to lowest
    sorted_levels = sorted(Level, key=lambda l: l.value, reverse=True)
    for level in sorted_levels:
        if xp >= level.value:
            return level.name 
    return Level.Noob.name

# Fetches a user from the backend api
async def fetch_user(username):
    # Creates a session for http requests
    async with aiohttp.ClientSession() as session:
        # Makes a GET request
        async with session.get(f'{API_URL}/user/{username}') as response:

            # Debug
            print(f"Fetching user {username} with status {response.status}")

            if response.status == 200:
                user_data = await response.json()
                # DEBUG
                print(f"User fetched: {user_data}")
                return await response.json()
            else:
                print(f"Failed to fetch user {username}, status: {response.status}")
            return None
    
# Creates a new user in the backend
async def create_user(username):
    # Creates a new session for handling http requests
    async with aiohttp.ClientSession() as session:
        # Makes the POST request to the backend sending the username in the req body as json
        async with session.post(f'{API_URL}/user', json={"username": username}) as response:

            # Debug
            print(f"User creation status: {response.status}")

            # Check if an entry was created
            if response.status == 201:
                return await response.json()
            return None 

# Updates user data in the backend
async def update_user(username, xp, level):
    
    print(f"Updating user {username} with XP {xp} and level {level}...")

    async with aiohttp.ClientSession() as session:
        # Makes a PUT request to the backend to update the users xp/level
        async with session.put(
            f'{API_URL}/user/{username}',
            json={"xp": xp, "level": level}
        ) as response:
            print(f"Update user status: {response.status}")
            return response.status == 200

# Adds xp to a user  
async def add_xp(username, amount):
    user = await fetch_user(username)

    # Debug
    print(f"User fetched for {username}: {user}") 

    if not user:
        
        print(f"User {username} not found, creating new user.")
        
        await create_user(username)
        user = await fetch_user(username)
        # Double validation
        if not user:
            return None 
        
        new_xp = user["xp"] + amount
        new_level = fetch_rank(new_xp)

        # Debug
        print(f"New XP: {new_xp}, New Level: {new_level}")

        if new_level not in Level.__members__:
            return None 

        await update_user(username, new_xp, Level[new_level].value)
        return {"username": username, "xp": new_xp, "level": new_level}

