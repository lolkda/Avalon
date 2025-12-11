# 5. 企业微信机器人
# 官方说明文档：https://work.weixin.qq.com/api/doc/90000/90136/91770
# 下方填写密钥，企业微信推送 webhook 后面的 key
export QYWX_KEY=""

# 企业微信反向代理地址
export QYWX_ORIGIN=""

# 6. 企业微信应用
# 参考文档：http://note.youdao.com/s/HMiudGkb
# 下方填写素材库图片id（corpid,corpsecret,touser,agentid），素材库图片填0为图文消息, 填1为纯文本消息
export QYWX_AM=""

# 8. Push Plus
# 官方网站：http://www.pushplus.plus
# 下方填写您的Token，微信扫码登录后一对一推送或一对多推送下面的token，只填 PUSH_PLUS_TOKEN 默认为一对一推送
export PUSH_PLUS_TOKEN=""
# 一对一多推送（选填）
# 下方填写您的一对多推送的 "群组编码" ，（一对多推送下面->您的群组(如无则新建)->群组编码）
# 1. 需订阅者扫描二维码 2、如果您是创建群组所属人，也需点击“查看二维码”扫描绑定，否则不能接受群组消息推送
export PUSH_PLUS_USER=""

# 10. gotify
# gotify_url 填写gotify地址,如https://push.example.de:8080
# gotify_token 填写gotify的消息应用token
# gotify_priority 填写推送消息优先级,默认为0
export GOTIFY_URL=""
export GOTIFY_TOKEN=""
export GOTIFY_PRIORITY=0

# 2. BARK
# 下方填写app提供的设备码，例如：https://api.day.app/123 那么此处的设备码就是123
export BARK_PUSH=""
# 下方填写推送图标设置，自定义推送图标(需iOS15或以上)
export BARK_ICON=""
# 下方填写推送声音设置，例如choo，具体值请在bark-推送铃声-查看所有铃声
export BARK_SOUND=""
# 下方填写推送消息分组，默认为"qing"
export BARK_GROUP=""

# 3. Telegram
# 下方填写自己申请@BotFather的Token，如10xxx4:AAFcqxxxxgER5uw
export TG_BOT_TOKEN=""
# 下方填写 @getuseridbot 中获取到的纯数字ID
export TG_USER_ID=""
# Telegram 方法
# 下方填写代理方法，代理类型为 http sock5
export TG_PROXY_TEPE=""
# Telegram 代理IP（选填）
# 下方填写代理IP地址，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "127.0.0.1"
# 如需使用，请自行解除下一行的注释
export TG_PROXY_HOST=""
# Telegram 代理端口（选填）
# 下方填写代理端口号，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "1080"
# 如需使用，请自行解除下一行的注释
export TG_PROXY_PORT=""
# Telegram 代理的认证参数（选填）
export TG_PROXY_AUTH=""
# Telegram api自建反向代理地址（选填）
# 教程：https://www.hostloc.com/thread-805441-1-1.html
# 如反向代理地址 http://aaa.bbb.ccc 则填写 aaa.bbb.ccc
# 如需使用，请赋值代理地址链接，并自行解除下一行的注释
export TG_API_HOST=""

# 青龙openApi相关配置
# export openApi_jd_isOpen=""
# export openApi_jd_Name=""
# export openApi_jd_Host=""
# export openApi_jd_User=""
# export openApi_jd_Password=""

# export openApi_scan_isOpen=""
# export openApi_scan_Name=""
# export openApi_scan_Host=""
# export openApi_scan_User=""
# export openApi_scan_Password=""

# 日志等级
export log_level="20" # 默认日志等级

# 请求配置
export Max_Connection="1000"
export Req_Timeout="10"  # 请求超时时间
export Clear_PROXY="true" # 代理清理
export Retention_Time="15" # 代理使用时间
export PROXY_Method="" # pool 或 api
export PROXY_URL="" # api链接

# Wxpusher
export WP_APP_TOKEN_ONE=""

# ==========================================> sql <==========================================

export sql_Type="" # 数据库类型
export sql_Driven=""
export sql_User=""
export sql_Pwd=""
export sql_Host=""
export sql_Port=""
export sql_DB=""

# ==========================================> 其他变量 <==========================================

export Recombin_Mode="2" # 1随机模式, 2优先模式, 3轮换模式
export Recombin_ARG1="10"
export Recombin_ARG2=""
export Recombin_envs="" # 局部模式配置

# Gemini
export gemini_api_key=""
export gemini_base_url="" # 默认 https://generativelanguage.googleapis.com/v1beta

export login_url="" # 推送时候的登录链接

# 京东CK检测
export Check_updatedAt_Time="" # 转换wskey的间隔时长
export Check_Source="" # 需要操作的cookie源

# 京东算法接口
export JD_CLIENT_VERSION=""
export JD_BUILD=""
export JD_SIGN_API="" # sign接口
export JD_H5ST_API="" # H5st接口
export JD_Exchange_API="" # H5st接口
export JD_CODE_API=""

# 发财挖宝
export N_jd_Happy_HelpPin="" # 被助力pin
export N_jd_Happy_HelpCommand="" # 被助力口令
export N_jd_Happy_HelpCookie="" # 被助力Cookie
export N_jd_Happy_Source="" # cookie源
export N_jd_Happy_Black="" # 黑的Cookie
export N_jd_Happy_Num="" # 需要多少助力
export N_jd_Happy_Thread="" # 并发线程
export N_jd_Happy_Wait="" # 并发间隔

# 玩一玩助力
export N_jd_wanyiwan_HelpPin="" # 被助力Pin
export N_jd_wanyiwan_HelpCommand="" # 被助力口令
export N_jd_wanyiwan_HelpCookie="" # 被助力Cookie
export N_jd_wanyiwan_Source="" # cookie源
export N_jd_wanyiwan_Black="" # 黑的Cookie

# 转赚红包
export N_jd_InviteFission_HelpPin="" # 被助力pin
export N_jd_InviteFission_HelpCommand="" # 被助力口令
export N_jd_InviteFission_HelpCookie="" # 被助力Cookie
export N_jd_InviteFission_Source="" # cookie源
export N_jd_InviteFission_Thread="" # 并发线程数
export N_jd_InviteFission_Black="" # 黑的Cookie
export N_jd_InviteFission_Num="" # 助力人数
export N_jd_InviteFission_Wait="" # 并发间隔

# 转赚红包: 抽奖
export N_jd_InviteFissionDraw_TaskPin=""  # 京东：Bn1VWXtvgTv5ewPoMR-X8A  特价：CmPJ1svf_qoTYXEwfOkKPg
export N_jd_InviteFissionDraw_TaskCookie="" # 被助力pin
export N_jd_InviteFissionDraw_Source="" # 被助力口令

# 入会有礼
export N_jd_openCard_shopUrl="" # 店铺链接
export N_jd_openCard_Min="" # 最少多少奖励入会 (默认50)
export N_jd_openCard_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_openCard_TaskCookie="" # 指定运行Cookie
export N_jd_openCard_Source="" # cookie源
export N_jd_openCard_Thread="" # 并发线程数
export N_jd_openCard_Black="" # 黑的Cookie
export N_jd_openCard_Wait="" # 并发间隔

# 关注有礼
export N_jd_drawShopGift_shopUrl="" # 店铺链接
export N_jd_drawShopGift_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_drawShopGift_TaskCookie="" # 指定运行Cookie
export N_jd_drawShopGift_Source="" # cookie源
export N_jd_drawShopGift_Thread="" # 并发线程数
export N_jd_drawShopGift_Wait="" # 并发间隔
export N_jd_drawShopGift_Black="" # 黑的Cookie

# 店铺签到
export N_jd_shopSign_Id="" # 活动Id
export N_jd_shopSign_TaskPin="" # 指定运行Pin
export N_jd_shopSign_Source="" # cookie源
export N_jd_shopSign_Wait="" # 并发间隔

# 新农场助力
export N_jd_Farm_HelpPin="" # 被助力pin
export N_jd_Farm_HelpCommand="" # 被助力口令
export N_jd_Farm_HelpCookie="" # 被助力Cookie
export N_jd_Farm_Source="" # cookie源
export N_jd_Farm_Black="" # 黑的Cookie
export N_jd_Farm_Num="" # 助力人数
export N_jd_Farm_Thread=""  # 并发的线程数
export N_jd_Farm_Wait="" # 并发间隔

# 刮刮乐
export N_jd_whxsign_shopUrl="" # 活动url
export N_jd_whxsign_TaskPin="" # 指定运行Pin (不写默认全部)
export N_jd_whxsign_TaskCookie="" # 指定运行Cookie
export N_jd_whxsign_Source="" # cookie源
export N_jd_whxsign_Black="" # 黑的Cookie
export N_jd_whxsign_Thread="" # 并发的线程数
export N_jd_whxsign_Wait="" # 并发间隔

# 通用抢券
export N_jd_coupon_ActivityId="" # 活动Id
export N_jd_coupon_Key="" # 券key
export N_jd_coupon_RoleId="" # 券RoleId
export N_jd_coupon_StrengThenKey="" # 券StrengThenKey
export N_jd_coupon_TaskPin="" # 执行的Pin
export N_jd_coupon_TaskCookie="" # 执行的Cookie
export N_jd_coupon_Source="" # cookie源
export N_jd_coupon_Num="" # 抢券次数
export N_jd_coupon_TimeOffset=""

# 店铺取关
export N_jd_unfollow_TaskPin="" # 执行的Pin
export N_jd_unfollow_TaskCookie="" # 执行的Cookie
export N_jd_unfollow_Source="" # cookie源
export N_jd_unfollow_wait="" # 并发间隔
export N_jd_unfollow_Thread="" # 并发线程数

# 微信红包团Scan
export N_jd_wxhongbao_Source="" # cookie源

# 微信红包团助力
export N_jd_Group_TaskId="" # 活动Id
export N_jd_Group_HelpPin="" # 被助力pin
export N_jd_Group_HelpCookie="" # 被助力Cookie
export N_jd_Group_Source="" # cookie源
export N_jd_Group_Thread="" # 并发线程数
export N_jd_Group_Black="" # 黑的Cookie
export N_jd_Group_Num="" # 助力人数
export N_jd_Group_Wait="" # 并发间隔

# 直播
export N_jd_liveLottery_shopUrl=""
export N_jd_liveLottery_TaskPin="" # 运行指定cookie
export N_jd_liveLottery_TaskCookie="" # 额外运行cookie
export N_jd_liveLottery_Source="" # cookie源
export N_jd_liveLottery_Thread="" # 并发线程数
export N_jd_liveLottery_Wait="" # 并发并发间隔
export N_jd_liveLottery_Black="" # 黑的Cookie
export N_jd_liveLottery_Min="" # 奖励最小值

# 秒杀签到
export N_jd_signBeanAct_Source="" # cookie源