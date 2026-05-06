#!/bin/bash
# 每日科技早报脚本设置脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "======================================"
echo "📰 每日科技早报脚本设置"
echo "======================================"

# 创建虚拟环境
echo ""
echo "🔧 创建 Python 虚拟环境..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ 虚拟环境创建成功"
else
    echo "ℹ️  虚拟环境已存在"
fi

# 激活虚拟环境并安装依赖
echo ""
echo "📦 安装 Python 依赖..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ 设置完成！"
echo ""
echo "使用方法："
echo "  cd scripts"
echo "  source venv/bin/activate"
echo "  python fetch_daily_news.py"
echo ""
