import importlib
import asyncio
from os import path
from function.PrintLog import PrintMethod

"""
cron: 10 6-23/1 * * *
new Env('店铺取关');
export N_jd_unfollow_shopUrl="" # 活动url
export N_jd_unfollow_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_unfollow_Container="" # 容器
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_nonc_unfollow.py")

if not path.exists(script_path):
    PrintMethod.error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_nonc_unfollow")

asyncio.run(Task.main())