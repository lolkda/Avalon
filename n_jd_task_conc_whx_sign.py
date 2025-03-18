import importlib
import asyncio
from os import path
from function.PrintLog import PrintMethod

"""
cron: 10 6-23/1 * * *
new Env('店铺刮刮乐');
scriptEnv:so
    export login_url 登录面板地址
    export check_updatedAt_time 再次转换默认16小时
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_whxsign.so")

if not path.exists(script_path):
    PrintMethod.error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_whxsign")

asyncio.run(Task.main())
