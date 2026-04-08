#!/usr/bin/env python3
"""
陈泽.skill — Persona 生成脚本
从语料库自动提炼五层人格文件

用法：
    python scripts/generate_persona.py

说明：
    本脚本读取 corpus/ 目录下的语料，
    使用 LLM（需配置 API_KEY）提炼生成 persona/*.md 文件。
    无 API_KEY 时生成占位符提示。
"""

import os
import sys

SKILL_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SKILL_DIR)
CORPUS_DIR = os.path.join(PROJECT_DIR, "corpus")
PERSONA_DIR = os.path.join(PROJECT_DIR, "persona")

LAYER_FILES = {
    "identity": "_layer1_identity.md",
    "values": "_layer2_values.md",
    "expression": "_layer3_expression.md",
    "humor": "_layer4_humor.md",
    "interaction": "_layer5_interaction.md",
}

def read_corpus():
    """读取语料目录下的所有 .md 文件"""
    files = {}
    if not os.path.exists(CORPUS_DIR):
        print(f"警告：语料库目录不存在 {CORPUS_DIR}")
        return files
    for fname in os.listdir(CORPUS_DIR):
        if fname.endswith(".md"):
            fpath = os.path.join(CORPUS_DIR, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                files[fname] = f.read()
    return files

def generate_persona_from_llm(corpus_content: str, layer: str) -> str:
    """调用 LLM 从语料提炼人格层（需要 API_KEY）"""
    api_key = os.environ.get("OPENAI_API_KEY") or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return f"（请配置 API_KEY 以自动生成 {layer} 层内容）"

    # TODO: 实现 LLM 调用
    # prompt = f"根据以下语料，提炼{layer}层人格，用 Markdown 格式输出：\n{corpus_content}"
    raise NotImplementedError("LLM 生成待实现")

def main():
    print("陈泽.skill — Persona 生成器")
    print("=" * 40)

    corpus = read_corpus()
    if not corpus:
        print("语料库为空，请先在 corpus/ 目录下添加语料文件。")
        sys.exit(1)

    print(f"读取到 {len(corpus)} 个语料文件：")
    for name in corpus:
        print(f"  - {name}")

    print("\n待实现：LLM 自动提炼功能")
    print("当前请手动编辑 persona/*.md 文件以调优人格。")

if __name__ == "__main__":
    main()
