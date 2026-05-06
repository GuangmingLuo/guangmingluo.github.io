#!/usr/bin/env python3
"""
每日科技早报自动抓取脚本
自动生成 Hugo 兼容的 markdown 文件
"""

import os
import sys
import argparse
import requests
from datetime import datetime, date
import feedparser
import json
from pathlib import Path

# 配置
CONTENT_DIR = Path(__file__).parent.parent / "content" / "daily-news"
TODAY = date.today()
DATE_STR = TODAY.strftime("%Y-%m-%d")
OUTPUT_FILENAME = f"{DATE_STR}-daily-tech-news.md"
OUTPUT_FILEPATH = CONTENT_DIR / OUTPUT_FILENAME

# 默认的科技新闻 RSS 源
RSS_SOURCES = [
    {
        "name": "36氪",
        "url": "https://36kr.com/feed",
    },
    {
        "name": "InfoQ 中国",
        "url": "https://www.infoq.cn/feed/rss",
    },
    {
        "name": "机器之心",
        "url": "https://www.jiqizhixin.com/rss",
    },
]

def ensure_content_dir():
    """确保内容目录存在"""
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

def fetch_rss_feed(url):
    """抓取 RSS 源"""
    try:
        print(f"正在抓取: {url}")
        feed = feedparser.parse(url)
        return feed.entries
    except Exception as e:
        print(f"抓取失败: {e}")
        return []

def generate_markdown(news_items, sources):
    """生成 Hugo 格式的 markdown 文件"""
    
    # 头部元数据
    markdown_content = f"""---
title: "{TODAY.strftime('%Y年%m月%d日')} 每日科技早报"
date: {TODAY.strftime('%Y-%m-%d')}T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "早报"]
description: "{TODAY.strftime('%Y年%m月%d日')} 科技新闻摘要，涵盖人工智能、云计算、开源社区等领域的最新动态。"
---

## 📰 今日科技要闻

"""
    
    # 添加新闻内容
    for source_name, items in news_items.items():
        if items:
            markdown_content += f"### {source_name}\n\n"
            for i, item in enumerate(items[:5], 1):  # 每个来源最多取5条
                title = item.get('title', '').replace('"', '\\"')
                link = item.get('link', '')
                summary = item.get('summary', '').replace('\n', ' ')[:150]
                
                markdown_content += f"{i}. **[{title}]({link})**\n"
                if summary:
                    markdown_content += f"   {summary}...\n"
                markdown_content += "\n"
    
    # 添加页脚
    markdown_content += f"""---

*本早报由自动抓取生成，数据来源：{', '.join(sources)}。*
*更新时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    return markdown_content

def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='每日科技早报抓取脚本')
    parser.add_argument('--auto', action='store_true', help='自动模式，不询问直接覆盖文件')
    args = parser.parse_args()
    
    print("=" * 50)
    print(f"📰 开始生成 {TODAY.strftime('%Y-%m-%d')} 科技早报")
    print("=" * 50)
    
    ensure_content_dir()
    
    # 检查文件是否已存在
    if OUTPUT_FILEPATH.exists():
        if args.auto:
            print(f"⚠️ 文件已存在，自动模式下直接覆盖: {OUTPUT_FILENAME}")
        else:
            print(f"⚠️ 文件已存在: {OUTPUT_FILENAME}")
            response = input("是否覆盖？(y/n): ").strip().lower()
            if response != 'y':
                print("已取消操作。")
                return
    
    # 抓取新闻
    all_news = {}
    used_sources = []
    
    for source in RSS_SOURCES:
        entries = fetch_rss_feed(source['url'])
        if entries:
            all_news[source['name']] = entries
            used_sources.append(source['name'])
            print(f"✅ 获取到 {len(entries)} 条新闻 - {source['name']}")
    
    if not all_news:
        print("❌ 未能获取到任何新闻")
        return
    
    # 生成 markdown
    print("\n正在生成 markdown 文件...")
    markdown_content = generate_markdown(all_news, used_sources)
    
    # 保存文件
    with open(OUTPUT_FILEPATH, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"✅ 文件已生成: {OUTPUT_FILEPATH}")
    print(f"📊 共包含 {len(used_sources)} 个来源的新闻")
    if not args.auto:
        print("\n提示: 请检查内容后手动提交到 Git！")

if __name__ == "__main__":
    main()
