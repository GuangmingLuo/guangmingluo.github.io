# 📰 每日科技早报自动化脚本

## 功能介绍

这个脚本用于自动抓取科技新闻 RSS 源，生成 Hugo 兼容的 markdown 文件，发布到您的博客中。

## 📁 文件结构

```
scripts/
├── fetch_daily_news.py    # 主抓取脚本
├── requirements.txt       # Python 依赖
└── README.md             # 使用说明
```

## 🚀 使用方法

### 1. 本地手动运行

```bash
# 安装依赖
cd scripts
pip install -r requirements.txt

# 运行脚本（会询问是否覆盖）
python fetch_daily_news.py

# 自动模式（直接覆盖，用于 CI/CD）
python fetch_daily_news.py --auto
```

### 2. GitHub Actions 自动运行

项目已配置 GitHub Actions，每天早上 8 点（北京时间）自动运行。

**需要完成的设置：**
1. 确保您的仓库开启了 GitHub Actions
2. 推送代码到 GitHub 后，Actions 会自动生效
3. 可以在仓库的 "Actions" 标签页手动触发测试

## ⚙️ 配置说明

### 修改新闻来源

编辑 `fetch_daily_news.py` 中的 `RSS_SOURCES` 列表：

```python
RSS_SOURCES = [
    {
        "name": "您的来源名称",
        "url": "https://example.com/rss",
    },
    # 添加更多来源...
]
```

### 修改运行时间

编辑 `.github/workflows/daily-news.yml` 中的 cron 表达式：

```yaml
schedule:
  - cron: '0 0 * * *'  # UTC 0:00 = 北京时间 8:00
```

## 📋 生成的文件

脚本会在 `content/daily-news/` 目录下生成文件，格式为：

```
YYYY-MM-DD-daily-tech-news.md
```

## 🎨 自定义样式

您可以修改 `generate_markdown()` 函数来自定义输出的 markdown 格式。

## 🔧 故障排除

### RSS 源抓取失败

- 检查网络连接
- 确认 RSS 源 URL 是否有效
- 某些网站可能有反爬虫机制

### GitHub Actions 不工作

- 确认 Actions 在仓库设置中已启用
- 检查 workflow 文件是否有语法错误
- 查看 Actions 运行日志

## 📝 注意事项

1. 请遵守各网站的 robots.txt 和使用条款
2. 不要频繁请求，避免给目标网站造成压力
3. 自动生成的内容建议人工审核后再发布
4. 尊重版权，合理使用抓取的内容
