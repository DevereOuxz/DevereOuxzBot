import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

#event
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Instagram: richard_kng'))

#error event
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Type .help to know all my commands.')

 #command
@client.command()
async def clear(ctx, amount : int):
     await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of message to delete')

#moderators command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#cogs setup
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx,send(f'Loaded')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NjcxNzE3ODMyMzEyMjI1Nzky.XjFeDA.2UlR2MDDyRCJjcdx4XhH5NHCxME')
