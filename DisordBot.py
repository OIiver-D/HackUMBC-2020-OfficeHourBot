import discord
import os
from TOKENFILE import TOKEN
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

# only owner of server may call these commands
@client.command(name = 'load', hidden = True)
#@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("loaded.")

@client.command(name = 'unload', hidden = True)
#@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("unloaded.")

@client.command(name = 'reload', hidden = True)
#@commands.is_owner()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send("reloaded.")

@client.command(name = 'refresh', hidden = True)
async def refresh(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.unload_extension(f'cogs.{filename[:-3]}')
            client.load_extension(f'cogs.{filename[:-3]}')
    await ctx.send("Refreshed all cogs.")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
