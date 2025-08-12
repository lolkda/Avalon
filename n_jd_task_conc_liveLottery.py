import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 0 0 1 1 *
new Env("直播抽奖");
export N_jd_liveLottery_shopUrl="" # 活动链接
export N_jd_liveLottery_TaskPin="" # 运行指定cookie
export N_jd_liveLottery_TaskCookie="" # 额外运行cookie
export N_jd_liveLottery_Source="Scan" # cookie源
export N_jd_liveLottery_Thread="10" # 并发线程数
export N_jd_liveLottery_Wait="0" # 并发等待间隔
export N_jd_liveLottery_Black="" # 黑的Cookie
export N_jd_liveLottery_Min="1" # 奖励最小值
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_task_conc_liveLottery.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_task_conc_liveLottery")

asyncio.run(Task.main())