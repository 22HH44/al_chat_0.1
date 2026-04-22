import sys
import os

# 打印当前 Python 解释器路径
print("当前 Python 路径:", sys.executable)

# 打印 Python 会在哪些文件夹里找库
print("库搜索路径:", sys.path)

# 尝试导入
try:
    import uvicorn
    print("✅ Uvicorn 导入成功！版本:", uvicorn.__version__)
except ImportError:
    print("❌ 找不到 Uvicorn")
