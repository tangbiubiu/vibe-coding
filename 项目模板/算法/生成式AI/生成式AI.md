📁 config/ → 模型, prompts, 日志的配置文件
📁 data/ → Prompts, embeddings, 和其他动态内容
📁 examples/ → 展示关键features的示例
📁 notebooks/ → 用来快速验证和原型制作的空间
📁 tests/ → 测试

📁 src/ → 核心脚本，所有的逻辑都在这里
├── agents/ → Agent 类: planner, executor, base agent
├── memory/ → 短期记忆和记忆持久化模块
├── pipelines/ → 聊天流程、文档处理和任务路由
├── retrieval/ → 向量库搜索和文档召回
├── skills/ → 拓展能力：网络搜索、代码执行
├── vision_audio/ → 多模态任务：音视频等
├── prompt_engineering/→ 提示词工程：模板、chain...
├── llm/ → 大模型的路由
├── fallback/ → LLM故障时的恢复逻辑
├── guardrails/ → PII过滤器、输出验证、安全检查
├── handlers/ → 输入/输出处理和错误管理
└── utils/ → 日志记录、缓存、速率限制、token计数

内容来源于https://github.com/HeyNina101/generative_ai_project ，略有修改。