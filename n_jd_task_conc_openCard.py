import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 0 0 1 1 *
new Env('入会有礼');
export N_jd_openCard_shopUrl="" # 店铺链接
export N_jd_openCard_Min="" # 最少多少奖励入会 (默认50)
export N_jd_openCard_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_openCard_TaskCookie="" # 指定运行Cookie
export N_jd_openCard_Source="" # cookie源
export N_jd_openCard_Thread="" # 并发线程数
export N_jd_openCard_Black="" # 黑的Cookie
export N_jd_drawShopGift_Wait="" # 间隔时间
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_openCard.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_openCard")

asyncio.run(Task.main())