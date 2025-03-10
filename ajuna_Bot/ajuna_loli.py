from discord.ext import commands, tasks
import json

import Commands
import Events

import dotenv
dotenv.load_dotenv()

with open('ajuna_Data/config.json', 'r') as file:
    _d = json.load(file)
    bot_state = _d['state']
    command_prefix = _d['prefix']

bot = commands.Bot(command_prefix=command_prefix)

Events.init(bot)
Commands.init(bot, bot_state)

with open(f'ajuna_Data/{bot_state}_token.txt', 'r') as file:
    bot.run(file.read())
