import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('店铺刮刮乐');
export N_jd_whxsign_shopUrl="" # 活动url
export N_jd_whxsign_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_whxsign_TaskCookie="" # 指定运行Cookie
export N_jd_whxsign_Source="" # cookie源
export N_jd_whxsign_Thread="" # 并发的线程数
export N_jd_whxsign_Black="" # 黑的Cookie
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_whxsign.py")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_whxsign")

asyncio.run(Task.main())