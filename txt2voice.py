import asyncio

from edge_tts import Communicate
TEXT = "你好哟，我是智能语音助手，小伊"
VOICE = "zh-CN-XiaoyiNeural"
OUTPUT_FILE = "/Users/liuyue/Downloads/test.mp3"


async def _main() -> None:
    communicate = Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(_main())