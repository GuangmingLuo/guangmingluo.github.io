#!/bin/bash
# 快速运行每日科技早报抓取脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "⚠️  虚拟环境不存在，先运行设置脚本..."
    ./setup.sh
fi

# 激活虚拟环境并运行
source venv/bin/activate
python fetch_daily_news.py "$@"
