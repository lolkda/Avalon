import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 0 0 1 1 *
new Env('秒杀签到');
export N_jd_signBeanAct_Source="" # 容器
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_nonc_signBeanAct.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_nonc_signBeanAct")

asyncio.run(Task.main())