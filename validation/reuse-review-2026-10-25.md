# 第三方材料与许可核对（2026-10-25）

本轮以 GitHub 当前公开版本为起点，检查五个增长 Skill 的全部已跟踪 Markdown、Python、Shell 和 PowerShell 文件（许可全文排除在相似性目标外）。各仓文件数：{"global-growth-content-skill": 97, "global-growth-experiments-skill": 20, "global-gtm-strategy-skill": 23, "global-launch-acquisition-skill": 26, "global-sales-retention-skill": 20}。对照 4059 份上游及历史安装快照文件：Gingiris 提交 `68deea2a4917d669c3c986a0e10ef26ba4c4b0ec`、Alireza Rezvani 提交 `6d2f02ea077eead1bee5411a31bcc6db5a11a70c`，另含历史内容审查实际引用的八类本机 Gingiris 安装快照。

方法为英文单词及逐个汉字分词、小写归一化、连续 20 token 窗口精确比对。未发现命中。这一筛查仅排查长片段的字面复用；不能发现全部改写、翻译、短片段或结构借鉴，不能证明完全原创。未执行上游脚本或安装其插件。对照来源与版本的 SHA-256 清单保存在本次交付的 reuse-review.json。

GTM 包中原有七份许可全文原样保留。补充来源与作者对应关系，并明确 Apache-2.0 reference-c 的上游身份和 NOTICE 尚不能确认；不能依据一份通用许可文本宣布所有材料已合规。Content 的历史方法对照已明确记载 Gingiris 来源，本次补入随安装目录分发的来源说明及 MIT 全文，使只安装 skills 子目录的用户仍可拿到声明。未把来源改写成原创，也未删除历史对照记录。

本次未识别出需要替换的明确侵权文本或代码。其他三个增长包未发现需要据此改动的明确问题，因此保留实现。MIT 需随实际复制或实质部分保留版权和许可全文；如后续识别 Apache 衍生材料，应核对版权、NOTICE 与改动标识，而不是只留通用许可全文。本轮不是完整法律意见或原创性认证。
