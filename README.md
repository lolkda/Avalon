## 特性

1. **纯异步架构**：基于 Python 的 asyncio 实现。
2. **高性能并发**：轻松处理数千个并发任务，适合高并发场景。
3. **跨平台**：支持 Windows、macOS 和 Linux。

---

## 使用说明

### 使用前配置
1. **框架授权**：
   - 请先联系开发者获取框架授权 Token，并配置 `N_Frame_Token` 变量填写授权。
   - **注意**：Token 首次执行时会自动绑定设备和 IP。若执行环境变更（如更换设备或 IP），需自行到群聊重置：[Telegram](https://t.me/NaiScan)。

### 环境变量
2. **环境变量配置**：
   - 在运行脚本前，请先阅读脚本中的环境变量配置要求。
   - 将所需变量配置到框架自带的 `env` 文件夹中的 `config.sh` 文件或系统环境变量中。
   - **注意**：当环境变量与框架 `env` 配置冲突时，框架变量会优先覆盖系统环境变量。

### 多容器配置
3. **多容器支持**：
   - 必须配置以下 `openApi` 开头的变量以启用多容器功能：
     ```bash
     export openApi_xxx_isOpen=""  # 启用容器（设置为 "true" 启用 或 "false" 关闭）。
     export openApi_xxx_Name=""    # 容器名称。
     export openApi_xxx_Host=""    # 容器链接，例如：http://192.168.1.100:5100。
     export openApi_xxx_User=""    # 容器 Client ID。
     export openApi_xxx_Password="" # 容器 Client Secret。
     ```
   - **多容器使用**：
     - 将 `xxx` 替换为任意名称以缓存容器 Token。
     - 在脚本中，使用 `N_jd_xxxxxxx_Container=""` 指定需要操作的容器名称，多个容器名称使用 `|` 分隔（例如 `openApi_xxx_User` 中的 `xxx`）。

### 代理配置
4. **任务使用代理**：
   - 填写 `PROXY_URL` 到环境变量中，并根据 API 或代理池填写 `PROXY_Method` 类型：
     - `1`：API 代理。
     - `2`：代理池。
   - **注意**：若未配置 `PROXY_URL` 变量，网络 IO 任务将使用本机 IP 执行。

---

## 免责声明

本项目仅用于学习和研究目的，作者和贡献者不对使用本库产生的任何直接或间接后果负责。用户在使用本库时应自行承担风险。

### 重要提示：
1. **非官方支持**：本库与任何官方组织或公司无关，作者和贡献者不提供任何形式的官方支持。
2. **无担保声明**：本库按“原样”提供，不提供任何明示或暗示的担保，包括但不限于适销性、特定用途适用性和非侵权性。
3. **责任限制**：在任何情况下，作者和贡献者均不对因使用或无法使用本库导致的任何损害（包括但不限于数据丢失、业务中断或利润损失）承担责任。
4. **用户责任**：用户应确保其使用本库的行为符合相关法律法规，并承担因使用本库而产生的全部责任。

---

### 其他说明
- 请确保在使用本库前，充分理解其功能和限制。
- 如有任何问题或建议，欢迎通过项目的 GitHub 仓库提交 Issue 或 Pull Request。
