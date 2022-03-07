from pystyle import Anime, Colors, Colorate, System, Center, Write
import time
from discord_webhook import DiscordWebhook

ascii_art = r"""
s __      __      ___.   .__                   __             _________                                                 
/  \    /  \ ____\_ |__ |  |__   ____   ____ |  | __  ______/   _____/__________    _____   _____   ___________  ______
\   \/\/   // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / /  ___/\_____  \\____ \__  \  /     \ /     \_/ __ \_  __ \/  ___/
 \        /\  ___/| \_\ \   Y  (  <_> |  <_> )    <  \___ \ /        \  |_> > __ \|  Y Y  \  Y Y  \  ___/|  | \/\___ \ 
  \__/\  /  \___  >___  /___|  /\____/ \____/|__|_ \/____  >_______  /   __(____  /__|_|  /__|_|  /\___  >__|  /____  >
       \/       \/    \/     \/                   \/     \/        \/|__|       \/      \/      \/     \/           \/                                                                                                
"""[1:]

def systeme():
  Anime.Fade(text=Center.Center(ascii_art), color=Colors.red_to_yellow, mode=Colorate.Vertical, enter=True)
  webhook_spammer()



def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("WebHooks Spammer By yezzjoestar")

    systeme()

def webhook_spammer():
    System.Title("WebHooks Spammer By yezzjoestar")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art)))
    url = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url -> "))
    Msg = input(Colorate.Horizontal(Colors.yellow_to_red, "\n You Word-> "))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ The Message Will Be Spam As Long As The Tools Is Open!"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ I decline all responsibility for what you do with it."))
    a = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Want to continue? (Y/N) -> "))
    if a =="Y":
      while True:
        webhook = DiscordWebhook(url=url, content=Msg+" (WebHooks Spammez By yezzjoestar#0001)")
        time.sleep (0)
        response = webhook.execute()
        print(Colorate.Horizontal(Colors.yellow_to_red, ""))
    else:
      systeme()

init()
