import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('关注有礼');
export N_jd_drawShopGift_shopUrl="" # 店铺链接
export N_jd_drawShopGift_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_drawShopGift_TaskCookie="" # 指定运行Cookie
export N_jd_drawShopGift_Source="" # cookie源
export N_jd_drawShopGift_Thread="" # 并发线程数
export N_jd_drawShopGift_Wait="" # 间隔时间
export N_jd_drawShopGift_Black="" # 黑的Cookie
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_drawShopGift.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_drawShopGift")

asyncio.run(Task.main())