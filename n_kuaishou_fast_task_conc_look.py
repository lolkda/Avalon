import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('快手极速看广告得金币');
export n_kuaishou_fast_card="" # 卡密
export n_kuaishou_fast_look_source="" # cookie源
export n_kuaishou_fast_look_run_number_Key="" # 运行次数 (默认1)

"""

script_path = path.join(path.dirname(__file__), "script", "n_kuaishou_fast_task_conc_look.py")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_kuaishou_fast_task_conc_look")

asyncio.run(Task.main())