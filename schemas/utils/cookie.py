from pydantic import Field, BaseModel
from typing import Union, Optional

class OpenApiGetCookie(BaseModel):
    """通过 OpenAPI 获取 Cookie 时所需的参数模型。

    该类用于定义从指定的青龙面板实例中获取 Cookie 列表所需的核心信息，
    包括目标面板、存储 Cookie 的环境变量键名以及可选的状态过滤器。

    Attributes:
        source (str): 目标青龙面板的名称。该名称对应于 OpenAPI 环境变量中
            配置的源名称，例如 'JD' 或 'ELM'。
        key (str): 存储 Cookie 值的环境变量的键名（即变量名）。
            例如："JD_COOKIE"。
        status (Optional[bool]): 用于筛选 Cookie 状态的可选过滤器。
            该字段可以是以下三种值之一：
            - True:  仅获取已启用（有效）的 Cookie。
            - False: 仅获取已禁用（无效）的 Cookie。
            - None (默认值): 获取所有 Cookie，无论其状态如何。
    """
    source:str
    key:str
    status:Optional[bool] = None