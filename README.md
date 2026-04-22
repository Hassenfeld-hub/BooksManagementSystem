# 图书管理系统 (Books Management System)

一个基于 Python 开发的轻量级图书管理系统，旨在为用户提供便捷的书籍入库、查询及维护功能。项目已打包可执行文件，支持在 Windows 环境下直接运行。

## 🚀 项目特点

- **全功能管理**：支持书籍的添加（Add）、删除（Delete）、更新（Update）及查询（Search）。
- **数据持久化**：内置数据库逻辑，确保图书信息在程序关闭后仍能妥善保存。
- **双重运行模式**：
  - **开发者模式**：可通过 Python 源码进行二次开发与调试。
  - **用户模式**：提供已编译的 `.exe` 文件，无需安装 Python 环境即可直接使用。

## 📂 目录结构

```text
BooksManagementSystem/
├── BooksManagementSystem/                       # 源代码核心目录
│   ├── BooksManagementSystem.sql.template       # 数据库结构模板（需替换密码占位符后导入）
│   ├── config.json.template                     # 数据库连接配置模板
│   ├── library_db.py                            # 主程序逻辑与数据库操作
│   └── requirements.txt                         # Python 依赖列表
├── .gitignore                                   # 排除敏感文件（config.json、*.sql 等）
├── library_db.exe                               # 已打包的 Windows 可执行程序
└── README.md                                    # 项目说明文档
```

## 🔒 安全配置说明 (Security Setup)

> **重要**：本项目使用外置配置文件管理数据库凭据，请严格按照以下步骤操作，**切勿将真实密码提交到版本库**。

### 第一步：配置数据库连接

1. 复制配置模板文件：
   ```bash
   cp BooksManagementSystem/config.json.template BooksManagementSystem/config.json
   ```
2. 编辑 `BooksManagementSystem/config.json`，填入你自己的数据库信息：
   ```json
   {
     "host": "localhost",
     "user": "root",
     "password": "YOUR_ACTUAL_PASSWORD",
     "database": "booksmanagementsystem",
     "charset": "utf8mb4"
   }
   ```
3. **`config.json` 已被 `.gitignore` 排除，不会被提交到版本库。**

### 第二步：初始化数据库

1. 复制 SQL 模板并替换密码占位符：
   ```bash
   cp BooksManagementSystem/BooksManagementSystem.sql.template /tmp/init.sql
   ```
2. 打开 `/tmp/init.sql`，将所有 `your_admin_password` 和 `your_reader_password` 替换为你自己设置的强密码。
3. 在 MySQL 中执行该脚本：
   ```bash
   mysql -u root -p < /tmp/init.sql
   ```
4. 导入完成后删除临时文件：
   ```bash
   rm /tmp/init.sql
   ```

### 安全最佳实践 (Best Practices)

- ✅ **使用强密码**：避免使用 `123456`、`password123` 等弱密码。
- ✅ **不要提交 `config.json`**：该文件包含真实密码，已通过 `.gitignore` 排除。
- ✅ **不要提交 `*.sql` 文件**：SQL 导出文件可能包含敏感数据，已通过 `.gitignore` 排除。
- ✅ **定期轮换密码**：数据库管理员和读者账号密码应定期更新。
- ✅ **检查 Git 历史**：如果曾经意外提交了真实密码，请立即重置相关账号密码，并考虑使用 `git filter-branch` 或 [BFG Repo Cleaner](https://rtyley.github.io/bfg-repo-cleaner/) 清理 Git 历史记录。
## 🛠️ 技术栈 (Technology Stack)

本项目采用 **Python 3** 生态系统构建，结合了高效的图形界面与轻量级数据库方案：

*   **核心语言**：![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white) 
    *   利用 Python 的简洁性实现业务逻辑处理。
*   **图形界面 (GUI)**：![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue) / ![PyQt](https://img.shields.io/badge/GUI-PyQt5-green)
    *   提供直观的用户交互窗口，支持书籍信息的增删改查操作。
*   **数据库**：![SQLite](https://img.shields.io/badge/Database-SQLite3-003B57?style=flat&logo=sqlite&logoColor=white)
    *   采用本地轻量级 SQL 数据库，实现数据的持久化存储，无需配置复杂的服务器。
*   **程序打包**：![PyInstaller](https://img.shields.io/badge/Tools-PyInstaller-yellow)
    *   将 Python 源码封装为独立的 `.exe` 文件，确保在未安装 Python 环境的 Windows 系统上也能运行。
<img width="1502" height="948" alt="image" src="https://github.com/user-attachments/assets/d26146be-de89-4467-83e7-bcf9cc5fa012" />
<img width="1502" height="948" alt="image" src="https://github.com/user-attachments/assets/fe9bd176-50e1-4031-b6a4-1944853bc63a" />
<img width="1502" height="948" alt="image" src="https://github.com/user-attachments/assets/bfb95026-4347-4482-bda8-1ab4fd715b91" />
<img width="1502" height="948" alt="image" src="https://github.com/user-attachments/assets/33f8f27e-da48-4785-9e86-284774e70fd9" />




