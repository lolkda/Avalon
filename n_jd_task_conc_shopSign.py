import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 0 0 1 1 *
new Env('店铺签到');
export N_jd_shopSign_Id="" # 活动Id (F8C76481718FA814000365AB85B29892:1000092984:13117366)
export N_jd_shopSign_TaskPin="" # 指定运行Pin (只能10个)
export N_jd_shopSign_Source="" # cookie源
export N_jd_shopSign_Wait="" # 是否等待 (0:不等待 大于0则是等待秒数)
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_shopSign.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_shopSign")

asyncio.run(Task.main())