![Global GTM Strategy — five independent growth skills](docs/assets/cover.svg)

# Global GTM Strategy

**海外市场研究与 GTM 战略 · 判断出海先进入哪个市场、服务谁，以及用什么方式获得首批付费客户。**

[![Validate](https://github.com/NextVariable/global-gtm-strategy-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/NextVariable/global-gtm-strategy-skill/actions/workflows/validate.yml) [![MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE) [![Agent Skills](https://img.shields.io/badge/Agent_Skills-compatible-6e56cf.svg)](https://agentskills.io/specification)

[快速开始](#quick-start) · [任务示例](examples/first-task.md) · [方法](#method) · [验证](#validation) · [五个 Skill 合集](https://github.com/NextVariable/global-growth-skills)

输入 **产品、客户与替代方案、已有访谈或购买记录、预算与交付能力**，得到 **优先市场与客户、价值主张、进入路径、下一项验证**。可以独立使用；已有项目资料或其他 Skill 的交接都能直接接入。指令以中文编写，对客产物按目标受众选择语言。

## In practice

> 先服务能接受手动 CSV 的美国小品牌，从已付款试点的下一次真实任务验证复购。暂缓需要跨店权限、自动同步或本地托管的客户。
>
> 每月 12 小时支持，先给两家各最多 4 小时，另留 4 小时缓冲；一次 99 美元试点不等于订阅留存。

以上是合成任务的结果节选。[查看输入和完整任务说明 →](examples/first-task.md)

## Quick start

在你的项目目录运行，选择要安装到的客户端：

```sh
npx skills add NextVariable/global-gtm-strategy-skill --skill global-gtm-strategy-skill
```

需要跨项目使用时加 `-g`。此安装方式需要 Node.js 22.20+；也可以直接复制技能目录。

<details>
<summary>手动安装到 Codex（Git；已有目录时停止）</summary>

```sh
git clone https://github.com/NextVariable/global-gtm-strategy-skill.git
cd global-gtm-strategy-skill
mkdir -p "$HOME/.agents/skills"
target="$HOME/.agents/skills/global-gtm-strategy-skill"
if [ -e "$target" ] || [ -L "$target" ]; then
  echo "Already exists: $target"
else
  cp -R skills/global-gtm-strategy-skill "$target"
fi
```

完整保留 `skills/global-gtm-strategy-skill/` 内的方法、模板和许可。已有同名目录时先保存旧版及个人修改，再比较版本；不要把两份目录直接合并。其他客户端使用其配置的 Skill 目录。

</details>

重新加载客户端后调用 `$global-gtm-strategy-skill`。方法通过客户端工具工作；可选计算/状态脚本使用 Python 3.10+ 标准库。

```text
使用 $global-gtm-strategy-skill。
产品与当前阶段：……
这次要解决：……
已确认的能力、材料和限制：……
可投入的时间、预算与人员：……
请完成我需要的产物；未知的关键条件明确说明。
```

项目资料保存在你自己的工作目录，安装包只放通用方法。实际外发、发布、支出或客户系统操作依赖相应工具和授权。

## Method

入口只保留任务判断和必要边界，按需加载相关方法，不要求每次读完或跑完整个流程。

| 方法 | 解决什么 |
|---|---|
| [市场与细分](skills/global-gtm-strategy-skill/references/market-selection.md) | 比较客户任务、可达性、进入条件和淘汰理由 |
| [客户与需求](skills/global-gtm-strategy-skill/references/customer-research.md) | 招募访谈、观察真实工作、区分使用者与付款者 |
| [竞争与替代](skills/global-gtm-strategy-skill/references/alternatives.md) | 还原当前做法、切换成本与增长路径 |
| [商业机会](skills/global-gtm-strategy-skill/references/opportunity.md) | 检查收入口径、单位经济、服务产能和现金约束 |
| [进入策略](skills/global-gtm-strategy-skill/references/entry-strategy.md) | 把定位、触达、评估、购买和验证连起来 |

## Validation

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate.py
```

[验证说明](validation/README.md)区分结构与记录检查、计算测试、模型任务和真实业务结果。自动检查不替代语义审阅；合成试用不能证明获客、收入或留存提升。客户端实际加载、目标用户理解和业务效果应在自己的环境验证。

## Ecosystem

[01 市场战略](https://github.com/NextVariable/global-gtm-strategy-skill) → [02 定位内容](https://github.com/NextVariable/global-growth-content-skill) → [03 发布获客](https://github.com/NextVariable/global-launch-acquisition-skill) → [04 客户增长](https://github.com/NextVariable/global-sales-retention-skill) → [05 实验复盘](https://github.com/NextVariable/global-growth-experiments-skill)

五个独立仓库，按当前问题选用。共享产品背景、证据与版本，结果可以回到前面的决策；其他四个不是安装依赖。

## Contributing

改进建议请带一个具体任务、期望结果和实际问题。开发、检查与提交方式见 [CONTRIBUTING.md](CONTRIBUTING.md)；功能问题可提交 [Issue](https://github.com/NextVariable/global-gtm-strategy-skill/issues/new/choose)。

## English

Choose an international market and customer segment, understand alternatives and buying roles, and design the next validation. Research and strategy, with explicit evidence and resource constraints. Install the complete skill directory and invoke `$global-gtm-strategy-skill`. Instructions are Chinese-first; deliverables follow the target audience. Model and external tools are supplied by your client.

[MIT](LICENSE). 适用第三方许可保存在[许可声明](THIRD_PARTY_NOTICES.md)中。
