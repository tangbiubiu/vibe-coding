该模块可以大幅减少 Cursor 等平台上的高级请求（例如 OpenAI 工具调用）数量。在某些情况下，它可以帮助将多达 25 个工具调用合并为一个反馈感知请求，从而节省资源并提高性能。

本文档内容来源于：[noopstudios/interactive-feedback-mcp](https://github.com/noopstudios/interactive-feedback-mcp)

## 安装和配置
1. 先决条件：
    - Python 3.11 或更新版本。
    - uv（Python 包管理器）。使用以下命令安装：
        - Windows：pip install uv
        - Linux/Mac：curl -LsSf https://astral.sh/uv/install.sh | sh

2. 获取代码：
    - 克隆此存储库： `git clone https://github.com/noopstudios/interactive-feedback-mcp.git`
    - 或者下载源代码。
3. 导航到目录：
`cd path/to/interactive-feedback-mcp`
4. 安装依赖项：
    - `uv sync`（这将创建一个虚拟环境并安装包）
5. 运行 MCP 服务器：
    - `uv run server.py`
6. 在 cursor 中配置：
    - Cursor 通常允许在其设置中指定自定义 MCP 服务器。您需要将 Cursor 指向此正在运行的服务器。具体机制可能有所不同，因此请参阅 Cursor 的文档以了解如何添加自定义 MCP。

    - 手动配置（例如，通过mcp.json） 记得将路径更改/Users/fabioferreira/Dev/scripts/interactive-feedback-mcp为您在系统上克隆存储库的实际路径。

```json
{
  "mcpServers": {
    "interactive-feedback-mcp": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/fabioferreira/Dev/scripts/interactive-feedback-mcp",
        "run",
        "server.py"
      ],
      "timeout": 600,
      "autoApprove": [
        "interactive_feedback"
      ]
    }
  }
}
```
您可能会使用服务器标识符，就像interactive-feedback-mcp在 Cursor 中配置它时一样。

## 使用方法
将以下内容添加到 rule 或 prompt 中。
```
Whenever you want to ask a question, always call the MCP interactive_feedback.
Whenever you’re about to complete a user request, call the MCP interactive_feedback instead of simply ending the process. Keep calling MCP until the user’s feedback is empty, then end the request.
```

