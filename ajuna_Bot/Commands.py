import discord
import json
import time
import random
from discord.commands import Option
from discord.ext import commands
from discord.ext.commands import Bot

import Dependencies
import Chemistry


def find_in_message(content, target):
    info = ""
    for x in content:
        if x[0:len(target)] == target:
            info = x[len(target) + 1:]
    return info


def init(bot: Bot):
    @bot.slash_command()
    async def test(ctx):
        await ctx.respond(
            embed=discord.Embed(
                title="This is a test message. If you're seeing this, then the slash command module works!",
                description="There isn't much here...",
                colour=Dependencies.colour()
            ))
    
    @bot.slash_command()
    async def chem(ctx: discord.commands.ApplicationContext,
                   name: Option(str, "Name of an organic compound", required=True, default='methane')):
        if Chemistry.hydrocarbon(name):
            h = Chemistry.hydrocarbon(name)
            d = f"""
            **Homologous Series** : `{h['h_series']}`
            **Functional Group** : `{h['f_group']}`
            **Type of organic compound** : `{h['o_type']}`
            **General formula** : `{h['general_formula'][0]}; {h['general_formula'][1]}`
            **Number of carbon atoms** : `{h['carbon']}`
            """
        else:
            d = f'{name} is not valid.'
        await ctx.respond(
            embed=discord.Embed(
                title=name,
                description=d,
                colour=Dependencies.colour()
            )
        )

    # @bot.slash_command(description="Fetches the minecraft server's status and players")
    # async def mc_server(ctx):
    #     with open('ajuna_Data/mc_data.json', 'r', encoding='utf-8') as file:
    #         data = json.load(file)
    #         ip = data['ip']
    #         server_name = data['server_name']
    #
    #     try:
    #         server = MinecraftServer.lookup(ip)
    #         if server.status() is None:
    #             description = f"IP : `{ip}`\n"
    #             line = "⚫"
    #         else:
    #             mc_status = server.status()
    #             description = f"**IP :** `{ip}`\n\n" \
    #                           f"**Average ping** : `{random.randint(9000, 10000) / 1000}ms`\n" \
    #                           f"**Version :** {mc_status.version.name}\n" \
    #                           f"**Players :** {mc_status.players.online}/{mc_status.players.max}\n"
    #             line = "🟢"
    #
    #             # Fetching players names
    #             try:
    #                 description += '\n'.join([f" \> {x.name}" for x in mc_status.players.sample])
    #             except Exception as e:
    #                 pass
    #             description += f"\n\n_Last checked : <t:{int(time.time())}:R> _"
    #
    #         final = discord.Embed(title=f"{line}  **{server_name}**",
    #                               description=description,
    #                               color=Dependencies.colour())
    #     except:
    #         final = discord.Embed(
    #             title=f"⚫ {server_name} is offline",
    #             description=f"**IP :** `{ip}`\n"
    #                         f"\n\n_Checked : <t:{int(time.time())}:R> _"
    #         )
    #     await ctx.respond(embed=final)

    @bot.slash_command()
    async def fetch_pfp(ctx: discord.commands.ApplicationContext,
                        name: Option(discord.Member, "Tag someone", required=False, default='')):
        if not name:
            selected_user = ctx.user
        else:
            selected_user = name
        pfp = selected_user.avatar.url
        final = discord.Embed(title=f"**{selected_user.name}'s profile picture**",
                              color=Dependencies.colour())
        final.set_image(url=pfp)
        await ctx.respond(embed=final)

    @bot.command()
    async def embed(ctx, *args):
        await ctx.message.delete()
        args = list(args)
        title = find_in_message(args, "title")
        description = find_in_message(args, "description")
        footer = find_in_message(args, "footer")
        try:
            colour = int(find_in_message(args, "colour"))
        except ValueError:
            colour = Dependencies.colour()
        if ctx.message.attachments:
            image_url = ctx.message.attachments[0].url
        else:
            image_url = find_in_message(args, "image_url")
        disposable = ("y" in find_in_message(args, "disposable").lower())

        final = discord.Embed(
            title=title,
            description=description,
            colour=colour
        )
        final.set_image(url=image_url)
        final.set_footer(text=footer)

        msg = await ctx.send(embed=final)

        if disposable:
            await Dependencies.dispose_message(msg)
