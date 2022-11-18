from SilentMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import MUSIC_BOT_NAME as BOT_NAME

BOT_USERNAME = app.username
START_TEXT = f"""
🥀 **ʜᴇʏ MENTION !**

**ᴛʜɪs ɪs [{BOT_NAME}](https://t.me/{BOT_USERNAME})**

ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.
sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʟᴀᴛғᴏʀᴍs : ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.


**ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs. ❄️ʜᴇʟᴘ❄️**
"""

COMMANDS_TEXT = f"""
🥀 **ʜᴇʏ MENTION !**

**Click on the buttons below to know my commands.**
"""

START_BUTTON_GROUP = InlineKeyboardMarkup(
    [   
        [
            InlineKeyboardButton(
                text="❄️ʜᴇʟᴘ❄️", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🫅🏻ᴏᴡɴᴇʀ🫅🏻", url="https://t.me/Silent_Smile_04"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Galaxia_Update"
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Total_masti"
            ),                       
        ],        
    ]
)

START_BUTTON_PRIVATE = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),            
        ],
        [   
            InlineKeyboardButton(
                text="❄️ʜᴇʟᴘ❄️", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🫅🏻ᴏᴡɴᴇʀ🫅🏻", url="https://t.me/Silent_Smile_04"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Galaxia_Update"
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/Total_masti"
            ),                       
        ],        
    ]
)

COMMANDS_BUTTON_USER = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴩʟᴀʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),            
            InlineKeyboardButton(
                text="ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

COMMANDS_BUTTON_SUDO = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs", callback_data="bot_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴩʟᴀʏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="play_cmd"
            ),
            InlineKeyboardButton(
                text="sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="sudo_cmd"
            ),            
        ],
        [
            InlineKeyboardButton(
                text="ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅs", callback_data="extra_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                
    ]
)

BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

SUDO_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs", callback_data="sudo_cmd"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="advanced_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)


ADMIN_TEXT = f"""
✅--**Admin Commands:**--

c stands for channel play.

/pause or /cpause - Pause the playing music.
/resume or /cresume- Resume the paused music.
/mute or /cmute- Mute the playing music.
/unmute or /cunmute- Unmute the muted music.
/skip or /cskip- Skip the current playing music.
/stop or /cstop- Stop the playing music.
/shuffle or /cshuffle- Randomly shuffles the queued playlist.

✅--**Specific Skip:**--
/skip or /cskip [Number(example: 3)] 
    - Skips music to a the specified queued number. Example: /skip 3 will skip music to third queued music and will ignore 1 and 2 music in queue.

✅--**Loop Play:**--
/loop or /cloop [enable/disable] or [Numbers between 1-10] 
    - When activated, bot loops the current playing music to 1-10 times on voice chat. Default to 10 times.

"""
AUTH_TEXT = """
✅--**Auth Users:**--
Auth Users can use admin commands without admin rights in your chat.

/auth [Username] - Add a user to AUTH LIST of the group.
/unauth [Username] - Remove a user from AUTH LIST of the group.
/authusers - Check AUTH LIST of the group.
"""

AUTH_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="admin_cmd"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

BOT_TEXT = """
✅--**Bot Commands:**--

/stats - Get Top 10 Tracks Global Stats, Top 10 Users of bot, Top 10 Chats on bot, Top 10 Played in a chat etc etc.

/sudolist - Check Sudo Users of Silent Music Bot

/lyrics [Music Name] - Searches Lyrics for the particular Music on web.

/song [Track Name] or [YT Link] - Download any track from youtube in mp3 or mp4 formats.

c stands for channel play.
/queue or /cqueue- Check Queue List of Music.
"""

PLAY_TEXT = """
✅--**Play Commands:**--

Available Commands = play , vplay , cplay

ForcePlay Commands = playforce , vplayforce , cplayforce

c stands for channel play.
v stands for video play.
force stands for force play.

/play or /vplay or /cplay  - Bot will start playing your given query on voice chat or Stream live links on voice chats.

/playforce or /vplayforce or /cplayforce -  Force Play stops the current playing track on voice chat and starts playing the searched track instantly without disturbing/clearing queue.

/channelplay [Chat username or id] or [Disable] - Connect channel to a group and stream music on channel's voice chat from your group.


✅--**Bot's Server Playlists:**--
/playlist  - Check Your Saved Playlist On Servers.
/deleteplaylist - Delete any saved music in your playlist
/play  - Start playing Your Saved Playlist from Servers.
"""

SUDO_TEXT = """
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]
🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.
🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.
🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.
📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats
⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.
👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists
👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists
🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.
⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.
🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.
<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message
**Example:** `/broadcast -user -assistant -pin Hello Testing`
"""

EXTRA_TEXT = """
✅Extra  Commands:
/start - Start the Silent Music Bot.
/help  - Get Commands Helper Menu with detailed explanations of commands.
/ping- Ping the Bot and check Ram, Cpu etc stats of Yukki.

✅Group Settings:
/settings - Get a complete group's settings with inline buttons

🔗 Options in Settings:

1️⃣ You can set Audio Quality you want to stream on voice chat.

2️⃣ You can set Video Quality you want to stream on voice chat.

3️⃣ Auth Users:- You can change admin commands mode from here to everyone or admins only. If everyone, anyone present in you group will be able to use admin commands(like /skip, /stop etc)

4️⃣ Clean Mode: When enabled deletes the bot's messages after 5 mins from your group to make sure your chat remains clean and good.

5️⃣ Command Clean : When activated, Bot will delete its executed commands (/play, /pause, /shuffle, /stop etc) immediately.

6️⃣ Play Settings:

/playmode - Get a complete play settings panel with buttons where you can set your group's play settings. 

Options in playmode:

1️⃣ Search Mode [ Direct or Inline] - Changes your search mode while you give /play mode. 

2️⃣ Play Mode [ Group or Channel] - Changes your Play mode to channel or group and streams music there only.

3️⃣ Play Type [ Everyone or Admins] - If admins, only admins present in group can play music on voice chat.
"""


BASIC_TEXT = """
💠 **Basic Commands:**

/start - Start the bot

/help - Get help message

/play - Play songs or videos in vc

/vplay - Play video in VC

/settings - Check Settings of bot in your group

/pause - Pause song in VC

/resume - Resume song in VC

/skip - Change the song in VC 

/end or /stop - Stop the Song  

/loop - ᴡʜᴇɴ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ʙᴏᴛ ᴡɪʟʟ ᴩʟᴀʏ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴩʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ ɪɴ ʟᴏᴏᴩ ғᴏʀ 10 ᴛɪᴍᴇs ᴏʀ ᴛʜᴇ ɴᴜᴍʙᴇʀ ᴏғ ʀᴇǫᴜᴇsᴛᴇᴅ ʟᴏᴏᴩs.

/shuffle - sʜᴜғғʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs.
"""

BASIC_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

ADMIN_BACK_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="Auth Commands", callback_data="auth_cmds"
            ),                        
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="command_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)

COMMAND_MENU_BUTTON = InlineKeyboardMarkup(
    [   [
            InlineKeyboardButton(
                text="ʙᴀsɪᴄ ᴄᴏᴍᴍᴀɴᴅs", callback_data="basic_cmd"
            ),                                   
        ],
        [
            InlineKeyboardButton(
                text="ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴏᴍᴍᴀɴᴅs", callback_data="advanced_cmd"
            ),
        ],
        [
            InlineKeyboardButton(
                text="↪️ Back", callback_data="open_start_menu"
            ),
            InlineKeyboardButton(
                text="🔄 Close", callback_data="close_btn"
            ),            
        ],                        
    ]
)
