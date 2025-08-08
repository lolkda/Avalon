import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('店铺取关');
export N_jd_unfollow_shopUrl="" # 活动url
export N_jd_unfollow_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_unfollow_Source="" # cookie源
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_unfollow.py")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_unfollow")

asyncio.run(Task.main())