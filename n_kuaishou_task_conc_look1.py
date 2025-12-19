import importlib
import asyncio
from os import path
from utils.logger import ScriptLogger
"""
cron: 10 6-23/1 * * *
new Env('快手看广告得金币强撸版');
export n_kuaishou_card="" # 卡密
export n_kuaishou_look_source="" # cookie源
export n_kuaishou_look_run_number="" # 运行次数 (默认1)
export n_kuaishou_look_min="" # 最低金币
export n_kuaishou_look_stop="" # N 次最低金币后停止账号运行 (默认3)
export n_kuaishou_look_augment="true" # 开启任务追加
export n_kuaishou_look_ex_number="" # 追加次数
export n_kuaishou_look_update_did="" # 低于设定的最少奖励更新did
export n_kuaishou_look_update_did_min="" # did更新阈值(低于该值更新did)
"""

script_path = path.join(path.dirname(__file__), "script", "n_kuaishou_task_conc_look1.so")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_kuaishou_task_conc_look1")

asyncio.run(Task.main())