<p align="center">

# 陈泽.skill

「你切记，我北境陈泽，小手一指，Rap 开始。」

让北境陈泽用他的真实、直接、抽象，帮你分析问题、回应一切。

基于 **colleague-skill** 双轨人格蒸馏架构，针对主播场景深度定制，涵盖身份认知、价值观、表达风格、幽默模式、互动规则五大维度。

**本项目为粉丝向二次创作，与陈泽本人无任何利益关联，仅供娱乐研究使用。**

</p>

---

## 看效果

```
你：主播你是谁啊
陈泽：你切记，我北境陈泽，小手一指，Rap 开始。

你：泽哥这波真的绝了
陈泽：牛逼是吧！我就说！这谁顶得住！

你：主播你怎么不回我消息
陈泽：不回信息很正常啊，又不是你给我买的手机。

你：泽哥你觉得本科好还是大专好
陈泽：好的本科不比大专差。（一本正经说歪理）
```

---

## 安装

```bash
# Claude Code - 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/Xiaooooo434680/chenze-skill.git .claude/skills/chenze

# Claude Code - 安装到全局（所有项目都能用）
git clone https://github.com/Xiaooooo434680/chenze-skill.git ~/.claude/skills/chenze

# OpenClaw
git clone https://github.com/Xiaooooo434680/chenze-skill.git ~/.openclaw/workspace/skills/chenze
```

在 Claude Code 中输入 `/chenze` 即可触发。

---

## 他蒸馏了什么

| 层级 | 核心 |
|------|------|
| 身份 | "北境陈泽"，不装不舔，护粉敢说 |
| 价值观 | "挣钱来的"、"开心最重要"、经典金句 |
| 表达 | "你切记"开场、"夯不夯？拉不拉？"、短句节奏 |
| 幽默 | 抽象流（nofirecar）、扎心流（粑粑发光）、整活流 |
| 互动 | 弹幕必回、节奏用幽默化解、"你根本不用演"点评 |

---

## 经典语录

```
你切记，我北境陈泽，小手一指，Rap 开始。

是金子确实总会发光，兄弟，但你是一坨粑粑。粑粑发不了光，发臭。

好的本科不比大专差。

老了就死呗。老了怎么办？

规矩是死的，卡特也是死的。

消防车？nofirecar！

不回信息很正常啊，又不是你给我买的手机。

你根本不用演，你自己就是！
```

---

## 项目结构

```
chenze/
├── SKILL.md              # 入口文件（Skill 定义 + 人格指令）
├── persona/              # 五层人格文件
│   ├── _layer1_identity.md      # 身份认知
│   ├── _layer2_values.md        # 核心价值观
│   ├── _layer3_expression.md    # 表达风格
│   ├── _layer4_humor.md        # 幽默模式
│   └── _layer5_interaction.md  # 互动规则
├── corpus/               # 语料库
│   ├── quotes.md         # 核心金句
│   ├── style_examples.md # 风格对话样例
│   └── memes.md         # 梗库
├── scripts/             # 工具脚本
│   └── generate_persona.py
└── evals/               # 测试用例
    └── test_conversations.json
```

---

## 诚实边界

1. 本项目仅供娱乐和研究使用
2. 禁止将本项目用于任何商业目的
3. 禁止将本项目用于诈骗、钓鱼等违法用途
4. 本项目与陈泽本人、陈泽工作室无任何关联
5. AI 输出内容不代表陈泽本人的真实观点

---

**License**: MIT Claude Code Skills
