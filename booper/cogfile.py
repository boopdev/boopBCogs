import discord, asyncio
from discord.ext import commands

class BooperCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def boop(self, ctx, user : discord.Member):
        return await ctx.send(
            f"{ctx.author.mention} booped {user.mention}!"
        )
        
def setup(client):
    client.add_cog(BooperCommands(client))
