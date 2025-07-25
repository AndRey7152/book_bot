import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import Config, load_config
from database.database import init_db
from handlers.other import other_router
from handlers.user import user_routers
from keyboards.menu_commands import set_main_menu
from services.file_handlers import prepare_book

logger = logging.getLogger(__name__)

async def main():
    config : Config = load_config()
    
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format
    )
    
    logger.info('Starting bot')
    
    bot = Bot(token=config.bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    
    logger.info('Preparing book')
    book = prepare_book('book/book.txt')
    logger.info('The book is uploaded. Total pages: %d', len(book))
    
    dd: dict = init_db()
    
    dp.workflow_data.update(book=book, dp=dp)
    
    await set_main_menu()
    
    dp.include_router(user_routers)
    dp.include_router(other_router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    asyncio.run(main())