import discord
from discord.ext import commands
import config


class AeroBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load_extensions(self, extensions):
        for extension in extensions:
            self.load_extension(extension)


bot = AeroBot(command_prefix='/', case_insensitive=True)
bot.load_extensions(config.extensions)
AeroBot.run(config.token)
