import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('通用抢券');
export N_jd_coupon_Key="" # 券key
export N_jd_coupon_RoleId="" # 券RoleId
export N_jd_coupon_ActivityId="" # 活动Id
export N_jd_coupon_StrengThenKey="" # 券StrengThenKey
export N_jd_coupon_TaskPin="" # 执行的Pin
export N_jd_coupon_TaskCookie="" # 执行的Cookie
export N_jd_coupon_Source="" # cookie源
export N_jd_coupon_Num="" # 抢券次数
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_coupon.py")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_coupon")

asyncio.run(Task.main())