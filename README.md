<div align="center">

# 陈泽.skill

> *「你切记，我北境陈泽，小手一指，Rap 开始。」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**让北境陈泽用他的真实、直接、抽象，帮你分析问题、回应一切。**

<br>

基于斗鱼主播 **陈泽** 真实语料蒸馏，涵盖身份认知、价值观、表达风格、幽默模式、互动规则五大维度。

[看效果](#效果示例) · [安装](#安装) · [他蒸馏了什么](#他蒸馏了什么) · [诚实边界](#诚实边界)

</div>

---

## 效果示例

```
用户    ❯ 主播你是谁啊

陈泽    ❯ 你切记，我北境陈泽，小手一指，Rap 开始。
```

```
用户    ❯ 泽哥这波真的绝了

陈泽    ❯ 牛逼是吧！我就说！这谁顶得住！
```

```
用户    ❯ 主播你怎么不回我消息

陈泽    ❯ 不回信息很正常啊，又不是你给我买的手机。
```

```
用户    ❯ 泽哥你觉得本科好还是大专好

陈泽    ❯ 好的本科不比大专差。（一本正经说歪理）
```

```
用户    ❯ 规矩是死的，卡特也是死的，什么意思？

陈泽    ❯ 规矩是死的，卡特也是死的。
        意思就是别太死板，懂？
```

这不是角色扮演。陈泽用的是「真实直接不装」、「抽象幽默扎心」、「短句快节奏」这些风格在回应——**不是复读语录，是用他的方式帮你回应一切。**

---

## 安装

```bash
# 方式一：skills.sh（推荐，一键安装）
npx skills add Xiaooooo434680/chenze-skill

# 方式二：Claude Code - 安装到当前项目
mkdir -p .claude/skills
git clone https://github.com/Xiaooooo434680/chenze-skill.git .claude/skills/chenze

# 方式三：Claude Code - 安装到全局
git clone https://github.com/Xiaooooo434680/chenze-skill.git ~/.claude/skills/chenze

# 方式四：OpenClaw
git clone https://github.com/Xiaooooo434680/chenze-skill.git ~/.openclaw/workspace/skills/chenze
```

安装后，在 Claude Code 里输入 `/chenze` 或直接触发词即可激活。

---

## 他蒸馏了什么

陈泽不是学院派，是街头智慧提炼者。他的核心风格提取自真实直播语料：

| 风格维度 | 一句话 |
|---------|--------|
| **身份认知** | "北境陈泽"，不装不舔，护粉敢说 |
| **价值观** | "挣钱来的"、"开心最重要"、经典金句 |
| **表达风格** | "你切记"开场、"夯不夯？拉不拉？"、短句节奏 |
| **幽默模式** | 抽象流（nofirecar）、扎心流（粑粑发光）、整活流 |
| **互动规则** | 弹幕必回、节奏用幽默化解、"你根本不用演"点评 |

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

## 素材来源

基于 2023-2026 年直播语料整理：

| 来源 | 类型 |
|------|------|
| 直播弹幕互动精选 | 弹幕回应合集 |
| 经典语录整理 | 金句归档 |
| 直播整活片段 | 抽象/扎心/整活 |

完整语料在 `corpus/` 目录，包含 quotes、style_examples、memes 三个维度。

---

## 诚实边界

**这个Skill能做的：**
- 用陈泽的真实直接风格回应问题
- 模拟他的抽象幽默、扎心语录表达
- 提供他在直播互动、粉丝回应领域的风格参考

**做不到的：**

| 维度 | 说明 |
|------|------|
| 替代本人 | 他的当下状态、最新想法、真实私下性格无法被复制 |
| 2026年后新动态 | 联网受限，最新信息可能有缺漏 |
| 商业决策 | 素材几乎全是娱乐互动内容，商务/财经数据严重不足 |

**一个不告诉你局限在哪的Skill，不值得信任。**

---

## 仓库结构

```
chenze-skill/
├── SKILL.md                          # Skill 入口文件（skills.sh 识别用）
├── README.md                         # 本文件
├── LICENSE                           # MIT 许可证
├── persona/                          # 五层人格文件
│   ├── _layer1_identity.md          # 身份认知
│   ├── _layer2_values.md            # 核心价值观
│   ├── _layer3_expression.md        # 表达风格
│   ├── _layer4_humor.md             # 幽默模式
│   └── _layer5_interaction.md       # 互动规则
├── corpus/                           # 语料库
│   ├── quotes.md                   # 核心金句
│   ├── style_examples.md           # 风格对话样例
│   └── memes.md                   # 梗库
├── scripts/                          # 工具脚本
│   └── generate_persona.py
└── evals/                           # 测试用例
    └── test_conversations.json
```

---

## 参考项目

陈泽.skill 的诞生站在这些前辈的肩膀上：

| 项目 | 说明 |
|------|------|
| [colleague-skill](https://github.com/titanwings/colleague-skill) | 双轨人格蒸馏架构，本 Skill 的技术根基 |
| [Anthropic AgentSkills](https://docs.anthropic.com/en/docs/claude-code/skills) | Claude Code Skill 标准格式 |
| [tong-jincheng-skill](https://github.com/hotcoffeeshake/tong-jincheng-skill) | 本 Skill README 排版参考 |

---

## 关于陈泽

陈泽，斗鱼主播，粉丝称「北境陈泽」。直播风格：**真实、直接、不装、抽象**。

核心标签：**真实不装、护粉敢说、抽象整活**。他说的不是让你听着舒坦的话，是让你听完之后记住的话。

> *「你切记，我北境陈泽，小手一指，Rap 开始。」*

---

## 许可证

MIT — 随便用，随便改，随便造。

---

<div align="center">

**语录** 告诉你他说过什么。<br>
**陈泽.skill** 帮你用他的方式回应一切。<br><br>
*你切记，我北境陈泽。*

<br>

MIT License © [Xiaooooo434680](https://github.com/Xiaooooo434680)

</div>
