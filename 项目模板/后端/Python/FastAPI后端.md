# 技术栈
```
语言：python

- 数据验证：pydantic
- web框架：FastAPI
- 数据库：Tortoise ORM + mysql
- 认证系统：JWT + 自定义API认证中间件
- 缓存：FastAPI-Cache2
- 后台管理：FastAPI Admin Panel
- 日志管理：loguru
```

# 项目结构
```
.
├── apis/
│   ├── dependencies.py          # 依赖
│   └── v1/                      # 版本化接口
│       ├── api.py               # 路由
│       └── endpoints/
├── core/
│   ├── config/                  # 配置文件
│   │   └── config.toml
│   ├── logger.py                # log配置
│   └── security.py              # 安全认证
├── database                     # 数据库
│   └── config.toml              # 数据库配置文件
├── docs/                        # 项目文档
├── env/                         # 虚拟环境
├── main.py                      # 主入口
├── models/                      # 数据模型
├── pyproject.toml
├── README.md
├── schemas/                     # 数据校验
├── tests/                       # 单元测试/集成测试
├── utils/                       # 工具类
└── vibe_docs/                   # Vibe Coding所需的文档
```

# 数据库模型
用于规范数据库的结构。示例如下：

1. **用户表（USER）**
存储用户核心身份信息。

| 字段                     | 类型         | 描述               | 约束                        |
| ------------------------ | ------------ | ------------------ | --------------------------- |
| user_id                  | INT          | 用户唯一ID         | PRIMARY KEY, AUTO_INCREMENT |
| email                    | VARCHAR(255) | 邮箱               | UNIQUE, NOT NULL            |
| username                 | VARCHAR(50)  | 用户名             | NOT NULL                    |
| registration_date        | TIMESTAMP    | 注册日期           | DEFAULT CURRENT_TIMESTAMP   |
| avatar_url               | VARCHAR(255) | 头像URL            |                             |
| is_banned                | BOOLEAN      | 是否封禁           | DEFAULT FALSE               |

2. ​**订单主表 (ORDER)​**​
所有订单的共享信息。

| 字段         | 类型          | 描述                 | 约束                        |
| ------------ | ------------- | -------------------- | --------------------------- |
| order_id     | INT           | 订单ID               | PRIMARY KEY, AUTO_INCREMENT |
| user_id      | INT           | 用户ID               | FOREIGN KEY (User.user_id)  |
| order_type   | ENUM          | 订单类型（VIP/饰品） | 'vip','jewelry'             |
| order_status | VARCHAR(20)   | 订单状态             | e.g., 'paid','refunded'     |
| total_amount | DECIMAL(10,2) | 订单总金额           |                             |
| created_at   | TIMESTAMP     | 下单时间             | DEFAULT CURRENT_TIMESTAMP   |