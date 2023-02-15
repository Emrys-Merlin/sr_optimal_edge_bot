import os

import discord
from dotenv import find_dotenv, load_dotenv

from optimal_edge.util import bl_sc_select

load_dotenv(find_dotenv())


BL_TEXT = """Use *Breaking the Limit* (add edge pool before the role + reroll 6s)"""
SC_TEXT = """Use *Second Chance* (reroll all failure dice)"""
TIE_TEXT = """You found a I tie combination. Do whatever you want ;-)"""


def main():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    tree = discord.app_commands.CommandTree(client)

    # guild=discord.Object(id=XXXXX)
    @tree.command(
        name="optimaledge",
        description="Reports whether Breaking the Limit or Second Chance is superior.",
    )
    async def optimal_edge(interaction, pool: int, edge: int, limit: int):
        """Report whether Breaking the Limit or Second Chance is superior.

        Parameters
        ----------
        interaction : _type_
            Some discord bot object
        pool : int
            The dice pool (without edge)
        edge : int
            Edge attribute
        limit : int
            Limit for the role
        """
        res = bl_sc_select(pool, edge, limit)
        if res == 1:
            text = BL_TEXT
        elif res == 0:
            text = TIE_TEXT
        else:
            text = SC_TEXT
        await interaction.response.send_message(text)

    @client.event
    async def on_ready():
        """Announce slash-commands"""
        # guild=discord.Object(id=XXXXX)
        await tree.sync()
        print("Ready!")

    client.run(os.environ["DISCORD_TOKEN"])


if __name__ == "__main__":
    main()
