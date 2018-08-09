import discord
from discord.ext import commands
import rocket_snake as rs
from rocket_snake import constants as const

import random

bot = commands.Bot(command_prefix = 'RL!')

async def get_platform(platform):
    if platform.lower() == 'steam':
        return const.STEAM
    elif platform.lower() == 'ps4':
        return const.PS4
    elif platform.lower() == 'xbox':
        return const.XBOX1


@bot.command(name = 'stats')
async def get_stats(ctx, uid, platform):

    platform = await get_platform(platform)

    player = await rlsclient.get_player(uid, platform)
    avatar = player.avatar_url
    stats = player.stats

    embed = discord.Embed(
        title = f'{player.display_name}\'s stats',
        colour = discord.Colour.blue(),
    )

    embed.set_footer(text = 'Powered by www.rocketleaguestats.com')

    embed.set_thumbnail(url = avatar)
    embed.add_field(name = 'Wins', value = stats['wins'])
    embed.add_field(name = 'MVPs', value = stats['mvps'])
    embed.add_field(name = 'Shots', value = stats['shots'])
    embed.add_field(name = 'Goals', value = stats['goals'])
    embed.add_field(name = 'Assists', value = stats['assists'])
    embed.add_field(name = 'Saves', value = stats['saves'])

    await ctx.send(embed = embed)

@bot.command(name = 'mutate')
async def mutate(ctx):
    string = '```'
    for key in mutators:
        mutate = random.choice(mutators[key])
        string += f'{key}: {mutate}\n'
    string += '```'
    await ctx.send(string)

@bot.command(name = 'fuck')
async def fuck(ctx):
    await bot.close()

if __name__ == '__main__':
    mutators = {
        'Match_length': ['5 Minutes', '10 Minutes', '20 Minutes', 'Unlimited'],
        'Max_score': ['Unlimited', '1 Goal', '3 Goals', '5 Goals'],
        'Game_speed': ['Default', 'Slo-Mo', 'Time Warp'],
        'Ball_max_speed': ['Default', 'Slow', 'Fast', 'Super Fast'],
        'Ball_type': ['Default', 'Cube', 'Puck', 'Basketball'],
        'Ball_weight': ['Default', 'Light', 'Heavy', 'Super Light'],
        'Ball_size': ['Default', 'Small', 'Large', 'Gigantic'],
        'Ball_bounciness': ['Default', 'Low', 'High', 'Super High'],
        'Boost_amount': ['Default', 'Unlimited', 'Recharge (Slow)', 'Recharge (Fast)', 'No Boost'],
        'Boost_strength': ['1x', '1.5x', '2x', '10x'],
        'Rumble': ['None', 'Default', 'Slow', 'Civilized', 'Destruction Derby', 'Spring Loaded'],
        'Gravity': ['Default', 'Low', 'High', 'Super High'],
        'Demolish': ['Default', 'Disabled', 'Friendly Fire', 'On Contact', 'On Contact (FF)'],
        'Respawn_time': ['3 Seconds', '2 Seconds', '1 Second', 'Disable Goal Reset'],
        'Bot_loadout': ['Default', 'Random']
    }

    rlsclient = rs.RLS_Client("NB9V509PT0RVN5LQGIPZVBQM6ISMPTRD")

    # get token.txt
    with open('token.txt') as token:
        token = token.readline()

    bot.loop.run_until_complete(bot.run(token.strip()))
