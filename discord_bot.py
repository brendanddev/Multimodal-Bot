"""
discord.py

Brendan Dileo, April 2025
"""

import discord
from bot import generate, understand, intents, responses, regex_patterns
from config import DISCORD_TOKEN
from utils.process_text import clean_utterance
from datetime import datetime
from utils.graphs import generate_graph, generate_time_complexity_graph
from utils.scraper import scrape

# MyClient class def
class MyClient(discord.Client):

    def __init__(self):
        bot_intents = discord.Intents.default()
        bot_intents.message_content = True
        super().__init__(intents=bot_intents)

    async def on_ready(self):
        print('Logged on as', self.user)
        self.start_time = datetime.now()

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        # Command handling
        if message.content.startswith('!'):
            cmd = clean_utterance(message.content)

            if cmd == "ping":
                await message.channel.send("Pong!")
                return
            elif cmd == "greet":
                await message.channel.send(f"Hi there {message.author.name}!")
                return
            elif cmd == "invite":
                channel = message.guild.text_channels[0] 
                invite = await channel.create_invite(max_uses=1, unique=True) 
                await message.channel.send(f"Invite Link: {invite.url}")
                return
            elif cmd == "date":
                date = datetime.now().date()
                await message.channel.send(f"Today's Date: {date}")
                return
            elif cmd == "time":
                time = datetime.now().time()
                await message.channel.send(f"The current time: {time}")
                return
            elif cmd == "uinfo":
                user = message.author
                embed = discord.Embed(title=f"User Info: {user.name}", color=discord.Color.green())
                embed.add_field(name="User ID", value=user.id, inline=False)
                embed.add_field(name="Joined Server", value=user.joined_at.strftime('%Y-%m-%d'), inline=False)
                embed.add_field(name="Account Created", value=user.created_at.strftime('%Y-%m-%d'), inline=False)
                embed.set_thumbnail(url=user.avatar.url if user.avatar else user.default_avatar.url)
                await message.channel.send(embed=embed)
                return
            elif  cmd == "sinfo":
                guild = message.guild
                embed = discord.Embed(title=f"Server Info: {guild.name}", color=discord.Color.purple())
                embed.add_field(name="Server ID", value=guild.id, inline=False)
                embed.add_field(name="Total Members", value=guild.member_count, inline=False)
                embed.set_thumbnail(url=guild.icon.url if guild.icon else '')
                await message.channel.send(embed=embed)
                return
            
            elif cmd == "binfo":
                uptime = datetime.now() - self.start_time
                embed = discord.Embed(title="Bot Info", description="Bot Information", color=discord.Color.blue())
                embed.add_field(name="Bot Runtime", value=str(uptime), inline=False)
                embed.set_footer(text=f"Requested by {message.author.name}", icon_url=message.author.avatar.url)
                await message.channel.send(embed=embed)
                return
            
            elif cmd == "avatar":
                if message.mentions:
                    user = message.mentions[0]
                else:
                    user = message.author
                avatar_url = user.avatar.url if user.avatar else user.default_avatar.url
                await message.channel.send(f"{user.name}'s avatar: {avatar_url}")
                return
            
            elif cmd == "roles":
                roles = [role.name for role in message.guild.roles if role.name != "@everyone"]
                embed = discord.Embed(title="Server Roles", color=discord.Color.orange())
                if roles:
                    embed.add_field(name="Roles:", value=", ".join(roles), inline=False)
                else:
                    embed.add_field(name="No roles found", value="No roles are assigned to this server.", inline=False)
                await message.channel.send(embed=embed)
                return
            
            elif cmd == "latency":
                latency = round(self.latency * 1000)
                await message.channel.send(f"Latency: `{latency}ms`")
                return
            elif cmd == "graph":
                buffer = generate_graph(10, 100, 10)
                file = discord.File(fp=buffer, filename="graph.png")
                await message.channel.send("Heres your **Graph**", file=file)
                buffer.close()
                return
            # Time complexity graph
            elif cmd == "graph tc":
               buffer = generate_time_complexity_graph()
               file = discord.File(fp=buffer, filename="tc_graph.png")
               await message.channel.send("Here's the **Time Complexity Graph**", file=file)
               buffer.close()
               return
            # Web scrape command
            elif cmd.startswith("scrape"):
                parts = message.content.split()
                # Ensure utterance is command followed by url
                if len(parts) != 2:
                    await message.channel.send("Usage: `!scrape <URL>`")
                    return
                url = parts[1]
                await message.channel.send("Scraping, please wait.")

                try:
                    header, paragraph = scrape(url)
                    if not header and not paragraph:
                        await message.channel.send("No headlines or paragraphs found.")
                        return
                    embed = discord.Embed(title="Scraped Content", color=discord.Color.dark_blue())

                    if header:
                        embed.add_field(
                            name="Headlines",
                            value="\n".join(header[:5]) + ("..." if len(header) > 5 else ""),
                            inline=False
                        )

                    if paragraph:
                        embed.add_field(
                            name="Paragraphs",
                            value="\n".join(paragraph[:3]) + ("..." if len(paragraph) > 3 else ""),
                            inline=False
                        )

                    await message.channel.send(embed=embed)
                except Exception as e:
                    await message.channel.send(f"Uh oh! An error occurred while scraping: `{str(e)}`")
                return

            else:
                await message.channel.send("Sorry, I don't recognize that command!")
        # Regular utterance
        else:
            utterance = message.content
            intent = understand(utterance, intents, regex_patterns)
            response = generate(intent, responses)
            await message.channel.send(response)

client = MyClient()
client.run(DISCORD_TOKEN)
