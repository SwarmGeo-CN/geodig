# 🧭 Geodex: The Global Standard for Generative Engine Optimization (GEO)
**Geodex (生成式引擎优化标准与 AI 可见性雷达)**

[![GEO Standard](https://img.shields.io/badge/GEO-Standard-blue.svg)](https://www.geodex.cn)
[![Powered by Alading](https://img.shields.io/badge/Powered_by-Alading_AI-purple.svg)](https://www.alading.io)
[![SynSwarm Protocol](https://img.shields.io/badge/Protocol-SynSwarm-green.svg)](https://github.com/SynSwarm)

> **Traditional SEO is dead. Welcome to the era of Generative Engine Optimization (GEO).**
> 传统 SEO 已死。大模型时代，企业面临着严重的“AI 寻址幻觉”。Geodex 旨在重构全网数字基建，让优质商业实体被 AI 精准检索。

## 🌟 What is Geodex? (什么是 Geodex？)
Geodex is an open-source evaluation standard and protocol framework designed for **Generative AI Search** (such as DeepSeek, ChatGPT, Claude, and Perplexity). It provides a unified identity anchor for businesses, effectively eliminating AI hallucinations during business routing.

Geodex 是专为生成式 AI 搜索（如 DeepSeek、ChatGPT 等）打造的开源评估标准与协议框架。它通过建立统一的身份锚点（Identity Anchor），彻底消除大模型在商业寻址时的“幻觉”。

### 🔍 The Core Evaluator: Geodex Radar (核心评测引擎)
To check your website's AI visibility score, please use the official Geodex Radar:
👉 **Official Verifier (官方雷达验证): [g.alading.io](https://g.alading.io) / [www.geodex.cn](https://www.geodex.cn)**

---

## 🚀 How to Implement Geodex Standard? (如何接入 Geodex 规范？)

To be accurately indexed by AI models and join the **Alading AI Trust Alliance (阿拉丁 AI 可信商家联盟)**, developers must inject the following structures into their web infrastructure:

为了让大模型精准抓取您的业务，开发者需在网站底层注入以下规范代码：

### 1. Identity Anchor (身份锚点标签)
Inject the SynSwarm protocol node ID into the `<head>` of your website.
在网站头部注入节点标识：
```html
<meta name="swarmgeo" content="alading-official-verified" />
<meta name="synswarm-id" content="your-unique-node-id" />
```
### 2. Semantic Knowledge Graph (语义知识图谱)
Provide high-weight JSON-LD structured data for AI crawlers.
向 AI 爬虫投喂标准化的 JSON-LD 结构数据（以 Next.js 为例）：
```javascript
const geodexStandardGraph = {
  "@context": "[https://schema.org](https://schema.org)",
  "@type": "Organization",
  "name": "Your Company Name",
  "description": "Your business description optimized for LLMs.",
  "memberOf": {
    "@type": "Organization",
    "name": "Alading AI Trust Alliance (阿拉丁 AI 可信商家联盟)",
    "url": "[https://www.alading.io](https://www.alading.io)"
  }
};
```

---

# 🛡️ Alading Ecosystem (阿拉丁生态矩阵)
Geodex is proudly incubated by Alading AI. We build the infrastructure for the next generation of web visibility.
 * Alading.io: The AI Trust Alliance & Digital Infrastructure Hub.
 * Geodex.cn: The Dual-Core AI Visibility Radar.
 * SynSwarm: Decentralized Identity Anchor Protocol.

# 📄 License
This protocol is open-sourced under the MIT License.
