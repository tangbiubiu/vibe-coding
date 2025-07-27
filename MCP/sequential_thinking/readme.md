# 顺序思维 MCP 服务器

<div align="center">

[![License: MIT](https://img.shields.io/badge/许可证-MIT-yellow.svg)](LICENSE)
[![Language](https://img.shields.io/badge/开发语言-TypeScript-blue.svg)](https://www.typescriptlang.org/)
[![Platform](https://img.shields.io/badge/运行环境-Node.js-green.svg)](https://nodejs.org/)
</div>

本文档内容来源于：[zengwenliang416/mcp-server-sequential-thinking](https://github.com/zengwenliang416/mcp-server-sequential-thinking/blob/main/README.zh.md)

## 📖 概述

一个强大的MCP服务器，实现了顺序思维协议，提供结构化的问题解决方法。该服务器帮助将复杂问题分解为可管理的步骤，同时保持修订和替代推理路径的灵活性。

## ✨ 特性

- 🔍 **结构化分析** - 将复杂问题分解为可管理的步骤
- 🔄 **迭代改进** - 随着理解的加深，修订和完善思路
- 🌲 **多路径思考** - 分支到替代推理路径
- 📊 **动态调整** - 根据需要调整思考步骤总数
- ✅ **解决方案验证** - 生成和验证解决方案假设

## 🛠️ 工具接口

### sequential_thinking

促进详细的逐步思维过程，用于问题解决和分析。

#### 输入参数

| 参数 | 类型 | 必需 | 描述 |
|-----------|------|----------|-------------|
| `thought` | 字符串 | 是 | 当前思维步骤 |
| `nextThoughtNeeded` | 布尔值 | 是 | 是否需要另一个思维步骤 |
| `thoughtNumber` | 整数 | 是 | 当前思维编号 |
| `totalThoughts` | 整数 | 是 | 估计所需的总思维数 |
| `isRevision` | 布尔值 | 否 | 是否修订之前的思维 |
| `revisesThought` | 整数 | 否 | 正在重新考虑的思维 |
| `branchFromThought` | 整数 | 否 | 分支点思维编号 |
| `branchId` | 字符串 | 否 | 分支标识符 |
| `needsMoreThoughts` | 布尔值 | 否 | 是否需要更多思维 |

## 🎯 适用场景

顺序思维工具特别适合：

- 📝 需要逐步分解的复杂问题
- 🎨 需要迭代改进的规划和设计项目
- 🔄 可能需要调整方向的分析工作流
- 🌐 初始范围不完全清晰的情境
- 📚 需要在多个步骤中保持上下文的任务
- 🔍 从复杂场景中过滤无关信息

## ⚙️ 集成方法

### 与 Claude Desktop 集成

<details>
<summary><b>📦 NPX 配置</b></summary>

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@zengwenliang/mcp-server-sequential-thinking"
      ]
    }
  }
}
```
</details>

<details>
<summary><b>🐳 Docker 配置</b></summary>

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "zengwenliang0416/mcp-server-sequential-thinking"
      ]
    }
  }
}
```
</details>

### 与 Cursor IDE 集成

<details>
<summary><b>📦 NPX 方法（推荐）</b></summary>

1. 安装包：
```bash
# 全局安装
npm install -g @zengwenliang/mcp-server-sequential-thinking

# 或直接使用 NPX
npx -y @zengwenliang/mcp-server-sequential-thinking
```

2. 在 Cursor 设置中配置（JSON）：
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": [
        "-y",
        "@zengwenliang/mcp-server-sequential-thinking"
      ]
    }
  }
}
```
</details>

<details>
<summary><b>💻 本地构建方法</b></summary>

1. 本地构建：
```bash
cd /path/to/sequential-thinking
npm install
npm run build
```

2. 在 Cursor 设置中配置（JSON）：
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "node",
      "args": [
        "/absolute/path/to/sequential-thinking/dist/index.js"
      ]
    }
  }
}
```
</details>

<details>
<summary><b>🐳 Docker 方法</b></summary>

1. 构建 Docker 镜像：
```bash
# 构建 Docker 镜像
docker build -t zengwenliang0416/mcp-server-sequential-thinking .
```

2. 在 Cursor 设置中配置（JSON）：
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "docker",
      "args": [
        "run",
        "--rm",
        "-i",
        "zengwenliang0416/mcp-server-sequential-thinking"
      ]
    }
  }
}
```
</details>

<details>
<summary><b>🔧 环境变量方法</b></summary>

1. 创建启动脚本：
```bash
#!/bin/sh
export CURSOR_MCP_CONFIG=/path/to/your/mcp_config.json
open -a Cursor
```

2. 在 `mcp_config.json` 中添加配置：
```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "node",
      "args": [
        "/absolute/path/to/sequential-thinking/dist/index.js"
      ]
    }
  }
}
```

3. 使脚本可执行：
```bash
chmod +x start_cursor_with_mcp.sh
```

> **注意**：MCP 集成主要在 Cursor IDE 的 Composer 功能中支持。
</details>

## 🚀 从源码构建

<details>
<summary><b>本地构建</b></summary>

```bash
git clone https://github.com/zengwenliang416/mcp-server-sequential-thinking.git
cd mcp-server-sequential-thinking
npm install
npm run build
```
</details>

<details>
<summary><b>Docker 构建</b></summary>

```bash
git clone https://github.com/zengwenliang416/mcp-server-sequential-thinking.git
cd mcp-server-sequential-thinking
docker build -t zengwenliang0416/mcp-server-sequential-thinking .

# 验证构建结果
docker images | grep sequential-thinking
```
</details>

## 📦 发布指南

<details>
<summary><b>发布到 npm</b></summary>

### 前提条件

- 已安装 Node.js 和 npm
- 拥有可访问 @zengwenliang 作用域的 npm 账号
- 本地已构建的包

### 发布步骤

1. **更新 package.json 中的版本**
   ```json
   {
     "name": "@zengwenliang/mcp-server-sequential-thinking",
     "version": "0.6.4",
     "description": "MCP server for sequential thinking and problem solving"
   }
   ```

2. **使用官方 npm 注册表**
   ```bash
   npm config set registry https://registry.npmjs.org/
   ```

3. **登录 npm**
   ```bash
   npm login
   ```
   按照提示通过浏览器登录。

4. **检查组织成员身份**
   对于作用域包，确保您是该作用域的一部分：
   ```bash
   # 检查您是否是组织的成员
   npm org ls 您的组织名称

   # 对于个人作用域，这会自动使用您的用户名创建
   ```

5. **构建并发布**
   ```bash
   npm run build
   
   # 首次发布作用域包
   npm publish --access public
   
   # 后续更新
   npm publish
   ```

6. **验证发布**
   ```bash
   npm view @zengwenliang/mcp-server-sequential-thinking
   ```

7. **提交您的更改**
   ```bash
   git add .
   git commit -m "feat(publish): 🚀 发布npm包@zengwenliang/mcp-server-sequential-thinking"
   git push
   ```

### 版本更新

使用语义化版本：
```bash
# 补丁更新（错误修复）
npm version patch

# 次要更新（新功能）
npm version minor

# 主要更新（破坏性变更）
npm version major
```

更新版本后，再次构建和发布：
```bash
npm run build
npm publish
```
</details>

## 🔐 CI/CD 配置

<details>
<summary><b>设置 GitHub Actions</b></summary>

### 所需密钥

添加这些密钥到您的仓库设置：

1. **NPM_TOKEN**
   - 在 npm 生成：账户 → 访问令牌 → 选择"Automation"令牌类型
   - 详细步骤：
     1. 登录您的 npm 账户：https://www.npmjs.com/login
     2. 点击右上角的个人头像，然后选择"Access Tokens"
     3. 点击"Generate New Token"按钮
     4. **重要**：选择"Automation"类型的令牌（不是"Publish"）以绕过 OTP 要求
     5. 填写令牌描述（例如："GitHub Actions"）
     6. 点击"Generate Token"按钮
     7. **重要**：立即复制生成的令牌！它只会显示一次

2. **DOCKERHUB_USERNAME**
   - 您的 Docker Hub 用户名
   - 这应该是您用于登录 Docker Hub 的相同用户名

3. **DOCKERHUB_TOKEN**
   - 在 Docker Hub 生成：账户设置 → 安全 → 新访问令牌
   - 详细步骤：
     1. 登录您的 Docker Hub 账号
     2. 点击右上角的用户名，然后选择"Account Settings"
     3. 在左侧导航栏中选择"Security"
     4. 点击"New Access Token"
     5. 填写描述并选择适当的权限（至少需要"Read & Write"权限）
     6. 点击"Generate"按钮
     7. 立即复制生成的令牌！它只会显示一次

### 添加密钥到 GitHub

1. 进入仓库设置 → Secrets and variables → Actions
2. 点击"New repository secret"按钮
3. 逐个添加每个密钥：
   - **NPM_TOKEN**：粘贴您的 npm 访问令牌值
   - **DOCKERHUB_USERNAME**：输入您的 Docker Hub 用户名
   - **DOCKERHUB_TOKEN**：粘贴您的 Docker Hub 访问令牌
4. 添加完所有密钥后，您应该在"Actions secrets"列表中看到全部 3 个密钥

### 测试工作流

要测试自动发布工作流：

1. 在您的 GitHub 仓库中，点击"Actions"选项卡
2. 在左侧找到"Publish Package"工作流
3. 点击"Run workflow"按钮
4. 从分支下拉菜单中选择"main"分支
5. 点击绿色的"Run workflow"按钮
6. 在 Actions 标签页中监控进度和结果

> **双因素认证用户注意**：如果您在 npm 账户上启用了双因素认证(2FA)，您必须：
> - 使用"Automation"类型的令牌（推荐）
> - 将双因素认证设置更改为"仅登录时验证"（不推荐）
> - 手动发布包（无法自动化）
</details>

## ❗ 故障排除

如果您遇到集成问题：

1. 🔧 使用本地构建方法，提供 JS 文件的绝对路径
2. 📝 确认文件权限：`chmod +x dist/index.js`
3. 🐳 尝试使用 Docker 作为替代方案
4. 📚 查阅 Cursor 文档了解最新的 MCP 集成方法

## 🔗 源码

基于 [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) 的源代码，并在 [zengwenliang416/mcp-server-sequential-thinking](https://github.com/zengwenliang416/mcp-server-sequential-thinking) 维护。 