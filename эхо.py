from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message,ContentType,Poll

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
BOT_TOKEN = '7166309582:AAH2fJ9K-JPmHTHc8kXTOkbtoifDPRm0M1o'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')

# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)

async def send_sticker_echo(message:Message):
    await message.answer_sticker(message.sticker.file_id)

async def send_video_echo(message:Message):
    await message.answer_video(message.video.file_id)

async def send_audio_echo(message: Message):
    if message.audio is not None and message.audio.file_id is not None:
        await message.answer_audio(message.audio.file_id)
    else:
        await message.answer("Sorry, I couldn't process your audio message.")

# Register the send_audio_echo function

async def send_voice_echo(message:Message):
    await message.answer_voice(message.voice.file_id)

async def send_doc_echo(message:Message):
    await message.answer_document(message.document.file_id)


async def send_contact_echo(message:Message):
    await message.answer_contact(phone_number=message.contact.phone_number,
                                  first_name=message.contact.first_name,
                                  last_name=message.contact.last_name,
                                  user_id=message.contact.user_id)


async def send_loc_echo(message:Message):
    await message.answer_location(latitude=message.location.latitude, longitude=message.location.longitude)


async def send_animation(message: Message):
    await message.reply_animation(message.animation.file_id)


async def send_dice(message: Message):
    print(1)
    await message.reply_dice(message.dice.emoji)


async def send_poll(message: Message):
    poll: Poll = message.poll
    questions: list[str] = list(map(lambda x: x.text, poll.options))
    await message.reply_poll(poll.question, questions, poll.is_anonymous, poll.type, poll.allows_multiple_answers,
                             poll.correct_option_id, poll.explanation, explanation_entities=poll.explanation_entities,
                             open_period=poll.open_period, close_date=poll.close_date, is_closed=poll.is_closed)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)

# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_doc_echo, F.document)
dp.message.register(send_loc_echo, F.location)
dp.message.register(send_contact_echo, F.contact)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_animation, F.animation)
dp.message.register(send_dice, F.dice)
dp.message.register(send_poll, F.poll)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
