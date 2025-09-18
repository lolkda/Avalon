import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 0 0 1 1 *
new Env('购物评价');
export N_jd_comment_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_comment_TaskCookie="" # 指定运行Cookie
export N_jd_comment_Source="" # cookie源
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_comment.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_comment")

asyncio.run(Task.main())