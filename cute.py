import sys
sys.path.insert(0, 'discord.py-self')
sys.path.insert(0, 'discord.py-self_embed')

import discord
from discord.ext import commands
import discord_self_embed
import json

with open('config.json', 'r') as file:
    config = json.load(file)
  
token = config['token']
prefix = config['prefix']

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.command()
async def purr(ctx, amount: int):
    if isinstance(ctx.channel, discord.TextChannel):
        def is_author(message):
            return message.author == ctx.author

        deleted_messages = await ctx.channel.purge(limit=amount + 1, check=is_author)

    elif isinstance(ctx.channel, discord.DMChannel):
        def is_author(message):
            return message.author == ctx.author

        deleted_messages = []
        async for message in ctx.channel.history(limit=amount + 1):
            if is_author(message):
                await message.delete()
                deleted_messages.append(message)


bot.run(token)
