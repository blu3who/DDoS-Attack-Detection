#Leaked By b r y a n#8259 Attack Detection

import os, sys, socket, requests, time, subprocess, shlex, ipapi
from datetime import datetime, date
from discord_webhook import DiscordWebhook, DiscordEmbed
from requests import get

def Clear():
    os.system('clear')

#Shows The Current Time
timenow = datetime.now()
timenow2 = timenow.strftime("%d-%m-%Y-%H:%M:%S")

#Discord Webhook Configuration
webhook_url = "https://discord.com/api/webhooks/758854857774989352/JVxeIHDoHeq1trcuXW-ffVBCzXJDsqNtZbLnUIkG8Nof7Haou3UoeqFecXCBf2DExAiH"

#Get The ethernet
ethernet = sys.argv[1]

#Get Server IP
ip = get('https://api.ipify.org').text

#Get Servers Country
country = ipapi.location(None, None, 'country')

#Highest Packets Per Second
highestpkts = 3000

#Lowest Packets Per Second
lowestpkts = 5000

#Where Pcaps Will Be Send Too
pcapdir = "/root/Dumps/"

#The Pcaps Ran Thru Wireshark/Tshark
txts = "/root/Dumps/"

#Shows the Txts Time
txtout="capture.{}.txt".format(timenow.strftime("%d-%m-%Y-%H:%M:%S"))


#Monitor Incoming Packets Configuration
while(True):
    #Old Bytes Capture
    old_b = subprocess.check_output("grep %s /proc/net/dev | cut -d : -f2 | awk \'{print $1}\'" % ethernet, shell=True)
    
    #Old Packets Capture
    old_ps = subprocess.check_output("grep %s /proc/net/dev | cut -d : -f2 | awk \'{print $2}\'" % ethernet, shell=True)
    
    
    old_b2 = int(old_b.decode('utf8').rstrip())
    
    old_ps2 = int(old_ps.decode('utf8').rstrip())
    
    time.sleep(1)
    
    #Gets New Bytes Capture
    new_b = subprocess.check_output("grep %s /proc/net/dev | cut -d : -f2 | awk \'{print $1}\'" % ethernet, shell=True)

    #Grabbing Packets Once AGAIN -_-
    new_ps = subprocess.check_output('grep %s /proc/net/dev | cut -d : -f2 | awk \'{print $2}\'' % ethernet, shell=True)

    new_ps2 = int(new_ps.decode('utf8').rstrip())

    new_b2 = int(new_b.decode('utf8').rstrip())
    
    #Defining Packets/s
    pps = (new_ps2 - old_ps2)

    #Defining Bytes/s
    byte = (new_b2 - old_b2)

    #Defining Others

    gigs = (byte/1024 ** 3)
    mbps = (byte/1024 ** 2)
    kbps = (byte/1024 ** 1)
    Clear()

    print("Skid Cant Hit Me Detection\n\033[97mMonitoring \033[36m{} \033[97mIncoming Traffic").format(ip,timenow.replace())
    print('\033[97mPackets/s \033[36m{}\n\033[97mBytes/s \033[36m{}\n\033[97mKbp/s \033[36m{}\n\033[97mGbp/s \033[36m{}\n\033[97mMbp/s \033[36m{}'.format(pps, byte, kbps, gigs, mbps))
    #If Statment For Trigger
    if(pps >= lowestpkts or pps > highestpkts):
        Clear()
        print('\033[97mAttack Detected On \033[36m{}').format(ip)
    
    
        os.system("tcpdump -n -s0 -c 5000 -w {}/dump.{}.pcap".format(txts, timenow2))
    
        notifcation = DiscordWebhook(url=webhook_url)
        embed=DiscordEmbed(title="DDoS Detection", url="https://ovh.com/", description='Attack Detected On Cosmic **{}** OVH Mitigation Has Started\n\n**Host:** {} Server\n**Type:** Attack Started\n**PPS:** {}\n**MBPS:** {}\n**GBPS:** {}\n**Pcap:** {}\n**Time:** {}\n'.format(country,country,pps,mbps,gigs,txtout,timenow.strftime("%d/%m/%Y | %H:%M:%S")), color=0xFF0000)
        embed.set_thumbnail(url='https://media.giphy.com/media/t7Qb8655Z1VfBGr5XB/giphy.gif')
        embed.set_timestamp()
    
        #Sends Webhook To Url
        notifcation.add_embed(embed)
        response = notifcation.execute()
        #Waits 200 Seconds To End The Attack
        time.sleep(200)
        print("\n\033[0;32mAttack Stopped")
        
        #Time It Stopped
        time_stopped = datetime.now()
    
        notifcation2 = DiscordWebhook(url=webhook_url)
        embed = DiscordEmbed(title="DDoS Detection", url="https://ovh.com/", description='Attack Has Stopped On Cosmic **{}** OVH\n\n**Host:** {} Server\n**Type:** Attack Finished\n\n'.format(country, country), color=0x008000)
        embed.set_footer(text='Cosmic Attack Notification', icon_url="https://www.rural-ftp.com//images/images/t2stdzRxJW6Rm4vX.png")
        embed.set_timestamp()
        embed.set_thumbnail(url='https://media.giphy.com/media/t7Qb8655Z1VfBGr5XB/giphy.gif')
    
        notifcation2.add_embed(embed)
        response = notifcation2.execute()


