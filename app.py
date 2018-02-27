import asyncio
import logging

from tornado.platform.asyncio import AsyncIOMainLoop

from birthday import application

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    AsyncIOMainLoop().install()
    loop = asyncio.get_event_loop()
    application.make_app()
    logger.info("Listening on port 8080")
    loop.run_forever()