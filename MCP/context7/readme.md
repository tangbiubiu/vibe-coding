Context7是一个文档拉取服务，主要用于找到与你的环境完全对应的官方文档和代码示例。本文档内容来源于：[upstash/context7](https://github.com/upstash/context7/blob/master/docs/README.zh-CN.md)

它可以一定程度解决以下问题：
- 找不到相关API。
- 使用与你环境版本不匹配的API。
- 大模型幻觉，使用不存在的API。

## 安装方法
首先需要`Node.js >= v18.0.0`
### 通过Smithery安装

要通过[Smithery](https://smithery.ai/server/@upstash/context7-mcp)自动安装Context7 MCP Server for Claude Desktop：

```bash
npx -y @smithery/cli install @upstash/context7-mcp --client claude
```

### 在Cursor中安装

前往：`Settings` -> `Cursor Settings` -> `MCP` -> `Add new global MCP server`

推荐的方法是将以下配置粘贴到你的Cursor `~/.cursor/mcp.json`文件中。更多信息请参见[Cursor MCP文档](https://docs.cursor.com/context/model-context-protocol)。

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

<details>
<summary>替代方案：使用Bun</summary>

```json
{
  "mcpServers": {
    "context7": {
      "command": "bunx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

</details>

<details>
<summary>替代方案：使用Deno</summary>

```json
{
  "mcpServers": {
    "context7": {
      "command": "deno",
      "args": ["run", "--allow-net", "npm:@upstash/context7-mcp"]
    }
  }
}
```

</details>

### 在Windsurf中安装

将此内容添加到你的Windsurf MCP配置文件中。更多信息请参见[Windsurf MCP文档](https://docs.windsurf.com/windsurf/mcp)。

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 在VSCode中安装

[<img alt="在VS Code中安装 (npx)" src="https://img.shields.io/badge/VS_Code-VS_Code?style=flat-square&label=安装Context7%20MCP&color=0098FF">](https://insiders.vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522context7%2522%252C%2522config%2522%253A%257B%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522%2540upstash%252Fcontext7-mcp%2540latest%2522%255D%257D%257D)
[<img alt="在VS Code Insiders中安装 (npx)" src="https://img.shields.io/badge/VS_Code_Insiders-VS_Code_Insiders?style=flat-square&label=安装Context7%20MCP&color=24bfa5">](https://insiders.vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522context7%2522%252C%2522config%2522%253A%257B%2522command%2522%253A%2522npx%2522%252C%2522args%2522%253A%255B%2522-y%2522%252C%2522%2540upstash%252Fcontext7-mcp%2540latest%2522%255D%257D%257D)

将此内容添加到你的VSCode MCP配置文件中。更多信息请参见[VSCode MCP文档](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)。

```json
{
  "servers": {
    "Context7": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 在Zed中安装

可以通过[Zed扩展](https://zed.dev/extensions?query=Context7)安装，或者你可以将以下内容添加到你的Zed `settings.json`文件中。更多信息请参见[Zed Context Server文档](https://zed.dev/docs/assistant/context-servers)。

```json
{
  "context_servers": {
    "Context7": {
      "command": {
        "path": "npx",
        "args": ["-y", "@upstash/context7-mcp@latest"]
      },
      "settings": {}
    }
  }
}
```

### 在Claude Code中安装

运行此命令。更多信息请参见[Claude Code MCP文档](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/tutorials#set-up-model-context-protocol-mcp)。

```sh
claude mcp add context7 -- npx -y @upstash/context7-mcp@latest
```

### 在Claude Desktop中安装

将此内容添加到你的Claude Desktop `claude_desktop_config.json`文件中。更多信息请参见[Claude Desktop MCP文档](https://modelcontextprotocol.io/quickstart/user)。

```json
{
  "mcpServers": {
    "Context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

### 在 Copilot Coding Agent 中安装

将以下配置添加到 Copilot Coding Agent 的 `mcp` 配置部分（Repository->Settings->Copilot->Coding agent->MCP configuration）：

```json
{
  "mcpServers": {
    "context7": {
      "type": "http",
      "url": "https://mcp.context7.com/mcp",
      "tools": [
        "get-library-docs",
        "resolve-library-id"
      ]
    }
  }
}
```

更多信息请参见[官方GitHub文档](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp)。

## 使用方法
Context7将最新的代码示例和文档直接获取到你的LLM上下文中。

- 1️⃣ 按照往常，自然地编写你的提示
- 2️⃣ 告诉LLM`使用 context7`
- 3️⃣ 获取可用的代码回复