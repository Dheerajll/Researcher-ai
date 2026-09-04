# Decision Agent

An AI-powered decision-making assistant that helps you stop overthinking and start deciding.

## What It Does

This agent solves analysis paralysis by:

1. **Finding the best options** - Identifies relevant choices for your specific situation
2. **Comparing what actually matters** - Focuses on key differentiators, not noise
3. **Removing useless information** - Filters out marketing fluff, outdated info, and irrelevant details
4. **Giving one clear recommendation** - No "it depends" cop-outs
5. **Stating uncertainties explicitly** - Tells you what's unknown instead of guessing

## Quick Start

```bash
python decision_agent.py "Your decision question here"
```

### Examples

```bash
# Tech purchases
python decision_agent.py "Which laptop should I buy for software development under $2000?"

# Software tools
python decision_agent.py "Which project management tool should I use for a small software team?"

# General decisions
python decision_agent.py "Should I learn Python or JavaScript first?"
```

## Output Format

The agent provides:

- 🎯 **One clear recommendation** - Bold and unambiguous
- 💡 **Key reasoning** - Top 3 reasons plus trade-offs to accept
- ⚖️ **What actually mattered** - The key differentiators between options
- 🗑️ **Information discarded** - Noise that was filtered out
- ⚠️ **Uncertainties** - What's unknown (no guessing!)
- 📊 **Confidence level** - How certain the recommendation is
- 📝 **All options considered** - Brief comparison of alternatives

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Decision Question                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  1. Categorize Decision Type                                 │
│     (tech, software, learning, career, etc.)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Generate Relevant Options                                │
│     (from domain-specific databases)                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  3. Identify What Criteria Matter                            │
│     (weighted by importance)                                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  4. Filter Out Noise                                         │
│     (marketing, outdated info, edge cases)                  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  5. Find Key Differentiators                                 │
│     (what actually separates the options)                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│  6. Select Best Option + State Uncertainties                 │
│     (clear recommendation, no guessing)                     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    One Clear Recommendation                  │
└─────────────────────────────────────────────────────────────┘
```

## Core Classes

- `Option` - Represents a single choice with pros, cons, and uncertainties
- `ComparisonCriteria` - What matters for the decision (with weights)
- `DecisionResult` - Complete output with recommendation and reasoning
- `DecisionAgent` - Main agent that orchestrates the decision process

## Extending the Agent

To add more decision domains:

1. Add keywords to `_categorize_decision()`
2. Add options to `_generate_options()`
3. Add criteria to `_identify_criteria()`
4. Customize noise patterns in `_identify_noise()`

## Philosophy

> "Perfect is the enemy of good." - Voltaire

This agent is designed to combat analysis paralysis. It:
- **Prioritizes action over perfection**
- **Makes trade-offs explicit**
- **Admits uncertainty instead of fabricating confidence**
- **Filters signal from noise**

## License

MIT
