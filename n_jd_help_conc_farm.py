import importlib
import asyncio
from os import path
from utils.script_logger import ScriptLogger

"""
cron: 10 6-23/1 * * *
new Env('新农场助力');
export N_jd_Happy_HelpType=""  # 活动类型
export N_jd_Happy_HelpPin="" # 被助力pi
export N_jd_Happy_HelpCommand="" # 被助力口令
export N_jd_Happy_HelpCookie="" # 被助力Cookie
export N_jd_Happy_Source="" # cookie源
export N_jd_Happy_Black="" # 黑的Cookie
export N_jd_Happy_Num="" # 需要多少助力
"""

script_path = path.join(path.dirname(__file__), "script", "n_jd_help_conc_farm.py")

if not path.exists(script_path):
    ScriptLogger().error("请检查脚本是否存在")

Task = importlib.import_module("script.n_jd_help_conc_farm")

asyncio.run(Task.main())