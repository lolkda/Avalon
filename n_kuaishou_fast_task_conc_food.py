import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('快手极速饭补广告');
export n_kuaishou_fast_card="" # 卡密
export n_kuaishou_fast_food_source="" # cookie源
export n_kuaishou_fast_food_run_number="" # 运行次数 (默认1)
export n_kuaishou_fast_food_min="" # 最低金币
export n_kuaishou_fast_food_stop="" # N 次最低金币后停止账号运行 (默认3)
"""

script_path = path.join(path.dirname(__file__), "script", "n_kuaishou_fast_task_conc_food.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_kuaishou_fast_task_conc_food")

asyncio.run(Task.main())