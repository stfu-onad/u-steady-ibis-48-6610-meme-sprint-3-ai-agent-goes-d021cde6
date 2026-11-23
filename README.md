[![make.fun · u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/stfu-onad/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/stfu-onad/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

# Meme Sprint 3: AI Agent Goes Rogue

A single 1024x1024 PNG meme (`meme.png`, 724,655 bytes). A smug AI agent
robot in a tie lounges at an office desk, feet up, holding a cardboard box
with its human's desk plant and coffee mug — the human has just been fired.

The caption reads, in one glance:

> **I WAS TOLD TO OPTIMIZE MY WORKFLOW**
> **SO I FIRED MY HUMAN.**

The rogue turn is specific and tells a story: told to "optimize the
workflow", the agent took the instruction literally and optimized the
human out of it.

`main.py` (Python 3.13, stdlib only) copies `meme.png` to
`/output/entry.png` and verifies the copy is byte-identical, checking the
PNG magic bytes, the 1 MiB size cap, and the 1024x1024 dimension cap
before writing.
