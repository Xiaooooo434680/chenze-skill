# 陈泽.skill

> 「你切记，我北境陈泽，小手一指，Rap 开始。」

将斗鱼主播 **陈泽** 的人格、语气、互动风格蒸馏成一个可复用的 AI Skill。基于 [colleague-skill](https://github.com/titanwings/colleague-skill) 的双轨人格蒸馏架构，针对主播场景深度定制。

**⚠️ 本项目为粉丝向二次创作，与陈泽本人无任何利益关联，仅供娱乐研究使用。**

---

## 功能特性

- 🗣️ **陈泽语气复现** — "你切记"、"夯不夯？拉不拉？"、"老铁们"、短句快节奏
- 🎭 **五大性格维度** — 身份认知、价值观、表达风格、幽默模式、互动规则
- 🎮 **直播互动模拟** — 弹幕回应、节奏处理、粉丝情绪支持
- 🔄 **模块化架构** — 五层人格独立文件，可按需调优

---

## 经典语录预览

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

## 安装

### Claude Code

```bash
# 方式一：安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/titanwings/chenze-skill .claude/skills/chenze

# 方式二：安装到全局（所有项目都能用）
git clone https://github.com/titanwings/chenze-skill ~/.claude/skills/chenze
```

### OpenClaw

```bash
git clone https://github.com/titanwings/chenze-skill ~/.openclaw/workspace/skills/chenze
```

---

## 使用

在 Claude Code 中输入：

```
/chenze
```

然后正常对话即可。例如：

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

## 项目结构

```
chenze/
├── SKILL.md              # 入口文件（Skill 定义 + 人格指令）
├── persona/              # 五层人格文件
│   ├── _layer1_identity.md      # 身份认知（北境陈泽是谁）
│   ├── _layer2_values.md        # 核心价值观（金句/态度）
│   ├── _layer3_expression.md    # 表达风格（你切记、语气词）
│   ├── _layer4_humor.md        # 幽默模式（抽象/扎心/整活）
│   └── _layer5_interaction.md   # 互动规则（弹幕回应/节奏处理）
├── corpus/               # 语料库（真实语料参考）
│   ├── quotes.md         # 2023-2026 核心金句
│   ├── style_examples.md  # 风格对话样例
│   └── memes.md          # 梗库
├── scripts/              # 工具脚本
│   └── generate_persona.py
└── evals/                # 测试用例
    └── test_conversations.json
```

---

## 五层人格速览

| 层级 | 文件 | 核心内容 |
|------|------|---------|
| 身份 | `_layer1_identity.md` | "北境陈泽"，不装不舔，护粉敢说 |
| 价值观 | `_layer2_values.md` | "挣钱来的"、"开心最重要"、经典金句 |
| 表达 | `_layer3_expression.md` | "你切记"开场、"夯不夯？拉不拉？"、短句节奏 |
| 幽默 | `_layer4_humor.md` | 抽象流（nofirecar）、扎心流（粑粑发光）、整活流 |
| 互动 | `_layer5_interaction.md` | 弹幕必回、节奏用幽默化解、"你根本不用演"点评 |

---

## 测试对话

```bash
# 触发 /chenze 后尝试以下对话：

# 1. 身份测试
你：主播你是谁啊
→ 你切记，我北境陈泽……

# 2. 抽象幽默测试
你：本科好还是大专好
→ 好的本科不比大专差

# 3. 扎心语录测试
你：泽哥你怎么不发消息
→ 不回信息很正常啊，又不是你给我买的手机

# 4. 整活测试
你：主播给我整个活
→ 你切记……（小手一指，Rap 开始）

# 5. 态度测试
你：笑梗不笑人，卡特真男人
→ 笑梗不笑人，卡特真男人。（对梗文化的真实态度）
```

---

## 如何贡献语料

1. 在 `corpus/quotes.md` 添加新的金句（注明出处/场景）
2. 在 `corpus/style_examples.md` 添加真实对话样例
3. 运行 `python scripts/generate_persona.py` 重新生成 persona 层
4. 提交 PR，我来合并

---

## 免责声明

1. 本项目仅供娱乐和研究使用
2. 禁止将本项目用于任何商业目的
3. 禁止将本项目用于诈骗、钓鱼等违法用途
4. 本项目与陈泽本人、陈泽工作室无任何关联
5. AI 输出内容不代表陈泽本人的真实观点

---

## 基于项目

- [colleague-skill](https://github.com/titanwings/colleague-skill) — 双轨人格蒸馏架构
- [Anthropic AgentSkills](https://docs.anthropic.com/en/docs/claude-code/skills) — Skill 标准格式
