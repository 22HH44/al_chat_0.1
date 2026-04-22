#来自 Python 标准库，操作解释器运行环境
import sys
#用来替代字符串路径
from pathlib import Path

# 添加项目根目录到 PYTHONPATH
#Path(__file__)是获取当前文件的绝对路径，parent是当前路径的父路径。这个代码意思就相当于获取当前文件的上两级别目录。
ROOT_DIR = Path(__file__).parent.parent

"""
将ROOT_DIR路径放进项目根目录，加入 Python 查找路径。因为当前运行的位置是scripts/init_db.py。
而下面导入了与scripts同级的目录下的模块，默认是找不到同级别的目录下的模块的，所以将llm_backend加入Python查找路径。
加了之后sys.path 包含：
[
    ".../scripts",
    ".../project_root"
]
"""
sys.path.append(str(ROOT_DIR))

# 确保能找到 app 模块
# print(f"Python path: {sys.path}")
# print(f"Current directory: {Path.cwd()}")
# print(f"Root directory: {ROOT_DIR}")

import asyncio
from app.core.database import engine, Base
from app.models import User, Conversation, Message
from app.core.logger import get_logger

#返回一个
logger = get_logger(service="init_db")

async def init_db():
    try:
        logger.info("Initializing database...")
        async with engine.begin() as conn:
            # 删除所有表（如果存在）
            await conn.run_sync(Base.metadata.drop_all)
            # 创建所有表
            await conn.run_sync(Base.metadata.create_all)
        logger.info("Database initialization completed successfully!")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise

def main():
    try:
        asyncio.run(init_db())
    except RuntimeError as e:
        logger.error(f"Runtime error: {str(e)}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()