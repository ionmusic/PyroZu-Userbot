import importlib
from pyrogram import idle
from uvloop import install


from Kazu.modules import ALL_MODULES
from Kazu import BOTLOG_CHATID, LOGGER, LOOP, aiosession, app, bots, ids
from Kazu.modules.basic import join

BOT_VER = "2.0.0"
CMD_HANDLER = ["." "," "?" "!"]
MSG_ON = """
💢 **𝙿𝚈𝚁𝙾𝚉𝚄-𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙰𝙺𝚃𝙸𝙵** 💢
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
❍▹ **Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ -** `{}`
❍▹ **Kᴇᴛɪᴋ** `{}alive` **Uɴᴛᴜᴋ Mᴇɴɢᴇᴄᴇᴋ Bᴏᴛ**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    print("LOG: Founded Bot token Booting..")
    for all_module in ALL_MODULES:
        importlib.import_module(f"Kazu.modules{all_module}")
        print(f"Successfully Imported {all_module} ")
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            await join(bot)
            try:
                await bot.send_message(BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER))
            except BaseException:
                pass
            print(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            print(f"{e}")
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("Kazu").info("PyroZu-Userbot Telah Aktif")
    install()
    LOOP.run_until_complete(main())
