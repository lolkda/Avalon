import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('京东CK检测');
scriptEnv:
    export Check_Source cookie源
    export login_url 登录面板地址
    export check_updatedAt_time 再次转换默认16小时
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_nonc_check.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_nonc_check")

asyncio.run(Task.main())