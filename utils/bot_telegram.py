import configparser
import redis
from aiogram import Bot, Dispatcher, executor, types
import bot_common
config = configparser.ConfigParser()
config.read('bot.ini')
TOKEN = config["bot"]["tg_token"]
issues_link = "https://www.youtube.com/channel/UCwtU6EBcXZVjd8g2-fzdh4A"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
r = redis.Redis(decode_responses=True)


@dp.message_handler(commands=["start", "yardım"])
async def send_welcome(message: types.Message):
    await message.reply("Hoşgeldin! Ben avatürk botuyum sana yardım edeceğim "
                        "Kullanıcı adını ve şifreni vereceğim! İyi Oyunlar "
                        "Kullanıcı adını ve şifreni kimseyle paylaşma.\n"
                        "Kullanıcı adı ve Şifreni Al /bilgilerim\n"
                        "Şifreyi değiştir - /sifre_degistir \n""Hesabı sıfırla - "
                        f"/sifirla\n Yeni güncellemeleri takip etmek için {issues_link}\n"
                        "ABONE OL!")


@dp.message_handler(commands=["bilgilerim"])
async def password(message: types.Message):
    passwd = r.get(f"tg:{message.from_user.id}")
    if passwd:
        uid = r.get(f"auth:{passwd}")
    else:
        uid, passwd = bot_common.new_account(r)
        r.set(f"tg:{message.from_user.id}", passwd)
    await message.reply(f"Kullanıcı adı: {uid}\nŞifre: {passwd}")


@dp.message_handler(commands=["sifre_degistir"])
async def change_password(message: types.Message):
    passwd = r.get(f"tg:{message.from_user.id}")
    if not passwd:
        return await message.reply("Hesabınız oluşturulmadı")
    while True:
        new_passwd = bot_common.random_string()
        if r.get(f"auth:{new_passwd}"):
            continue
        break
    uid = r.get(f"auth:{passwd}")
    r.delete(f"auth:{passwd}")
    r.set(f"auth:{new_passwd}", uid)
    r.set(f"tg:{message.from_user.id}", new_passwd)
    await message.reply(f"Yeni şifreniz: {new_passwd}")


@dp.message_handler(commands=["sifirla"])
async def reset(message: types.Message):
    passwd = r.get(f"tg:{message.from_user.id}")
    if not passwd:
        return await message.reply("Hesabınız oluşturulmadı")
    uid = r.get(f"auth:{passwd}")
    bot_common.reset_account(r, uid)
    await message.reply(f"Hesabınız sıfırlandı.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
