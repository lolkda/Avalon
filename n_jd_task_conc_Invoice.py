import importlib
import asyncio
from os import path
from utils.logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('购物信息汇总');
"""

script_path = path.join(path.dirname(__file__), "scripts", "n_jd_task_conc_Invoice.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("scripts.n_jd_task_conc_Invoice")

asyncio.run(Task.main())