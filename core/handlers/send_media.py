from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo
from aiogram import Bot
from aiogram.utils.chat_action import ChatActionSender

async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(path=r"your_audio_path", filename='AudioFile.mp3')
    await bot.send_audio(message.chat.id, audio=audio)

async def get_document(message: Message, bot: Bot):
    document = FSInputFile(path=r"your_docunemt_path")
    await bot.send_document(message.chat.id, document=document, caption='Its document')

async def get_meadia_group(message: Message, bot: Bot):
    photo1_mg = InputMediaPhoto(type='photo', media=FSInputFile(r"core/media/00.jpg"),
                                caption='Its meow-meow mediagroup')
    photo2_mg = InputMediaPhoto(type='photo', media=FSInputFile(r"core/media/images_fdd50fee21934.jpg"))
    video_mg = InputMediaVideo(type='video', media=FSInputFile(r"core/media/Funny Cats😀#shorts.mp4"))
    media = [photo2_mg, photo1_mg, video_mg]
    await bot.send_media_group(message.chat.id, media)

async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(r"core/media/x46tcgju.jpg")
    await bot.send_photo(message.chat.id, photo, caption='Floppa pic')

async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(r"core/media/ee525973-d6cc-46df-9af8-672128d4dcfb.png")
    await bot.send_sticker(message.chat.id, sticker)

async def get_video(message: Message, bot: Bot):    #ChatActionSender чтобы пользователь видел плашку что бот отправляет видео (to make the user see the die that the bot sends the video)
    async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=Bot):
        video = FSInputFile(r"core/media/Big floppa jumpscare!.mp4")
        await bot.send_video(message.chat.id, video)

async def get_video_note(message: Message, bot: Bot):
    async with ChatActionSender.upload_video_note(chat_id=message.chat.id, bot=Bot):
        video_note = FSInputFile(r"core/media/doc_2024-02-20_13-26-13.mp4")
        await bot.send_video_note(message.chat.id, video_note)

async def get_voice(message: Message, bot: Bot):
    async with ChatActionSender.record_voice(chat_id=message.chat.id, bot=Bot):
        voice = FSInputFile(r"core/media/audio_2024-02-20_13-27-26.ogg")
        await bot.send_voice(message.chat.id, voice)