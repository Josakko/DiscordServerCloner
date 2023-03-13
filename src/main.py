import os
import json
import time
from functions.cloner import cloner
from functions.panel import Panel, Panel_Run
from discord import Client, Intents
from rich.prompt import Prompt, Confirm
from time import sleep


try:
  client = Client(intents=Intents.all())
except Exception as error:
  print("> An error ocurred, please try again:", error)

with open("./config.json", "r") as json_file:
  data = json.load(json_file)

os.system('cls' if os.name == 'nt' else 'clear')


def clear(option=False):
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  if option:
    user = client.user
    guild = client.get_guild(int(INPUT_GUILD_ID))
    Panel_Run(guild, user)
  else:
    Panel()


async def clone_server():
  start_time = time.time()
  guild_from = client.get_guild(int(INPUT_GUILD_ID))
  print("")
  guild_to = client.get_guild(await cloner.guild_create(client, guild_from))
  await cloner.channels_delete(guild_to)
  if data["settings"]["roles"]:
    await cloner.roles_create(guild_to, guild_from)
  if data["settings"]["categories"]:
    await cloner.categories_create(guild_to, guild_from)
  if data["settings"]["channels"]:
    await cloner.channels_create(guild_to, guild_from)
  if data["settings"]["emojis"]:
    await cloner.emojis_create(guild_to, guild_from)
  print("\n> Done Cloning Server in " + str(round(time.time() - start_time, 2)) + " seconds")

@client.event
async def on_ready():
  clear(True)
  await clone_server()

class cloner_main:

  def __init__(self):
    self.INPUT_GUILD_ID = None
    with open("./config.json", "r") as json_file:
      self.data = json.load(json_file)

  def clear(self):
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    Panel()

  def edit_config(self, option, value, settings=False):
    if settings:
      self.data["settings"][option] = value
    else:
      self.data[option] = value
    with open("./config.json", "w") as json_file:
      json.dump(self.data, json_file, indent=4)

  def edit_settings_function(self):
    print("\nDo you want to copy:")
    categories = Confirm.ask("> Categories?")
    channels = Confirm.ask("> Channels?")
    roles = Confirm.ask("> Roles?")
    permissions =  Confirm.ask("> Permissions?")
    emojis = Confirm.ask("> Emojis?")
    for option in ["categories", "channels", "roles", "emojis", "permissions"]:
      self.edit_config(option, locals()[option], settings=True)

  def main(self):
    self.clear()
    if self.data["token"] == "None":
      self.TOKEN = Prompt.ask("\n> Enter your Token")
      with open("./config.json", "w") as json_file:
        self.data["token"] = self.TOKEN
        json.dump(self.data, json_file, indent=4)
      sleep(0.5)
    else:
      print("> Token Found")
      self.TOKEN = self.data.get("token", None)
    self.clear()
    edit_settings = Confirm.ask("\n> Do you want to edit the settings?")
    self.clear()
    if edit_settings:
      self.edit_settings_function()
    self.clear()

    self.INPUT_GUILD_ID = Prompt.ask("\n> Enter the Server ID")
    sleep(0.5)

    return self.INPUT_GUILD_ID, self.TOKEN


if __name__ == "__main__":
  INPUT_GUILD_ID, TOKEN = cloner_main().main()
  try:
    client.run(TOKEN, bot=False)
    clear()
  except Exception as error:
    print("> An error ocurred, please try again:", error)
    data["token"] = False
