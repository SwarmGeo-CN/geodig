# ⛏️ Geodig (地格)

> **The First Open-Source GEO (Generative Engine Optimization) Audit Tool for DeepSeek & LLMs.** > **全球首款适配 DeepSeek 的企业级 GEO 审计工具**

[![SwarmGeo](https://img.shields.io/badge/Powered%20by-SwarmGeo-blue)](http://swarmgeo.cn)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DeepSeek Compatible](https://img.shields.io/badge/DeepSeek-Compatible-green)]()

**Geodig** (pronounced "Geo-Dig") is a command-center utility designed to audit your brand's visibility within Large Language Models (LLMs) like DeepSeek, Doubao, and ChatGPT.

不像传统的 SEO 工具关注关键词排名，**Geodig (地格)** 关注的是企业在 AI 时代的**实体身份 (Entity Identity)**。

---

## 🚀 Key Features (核心功能)

1.  **🔍 DeepScan Protocol (深探协议)**: 
    * Checks `robots.txt` specifically for AI bots (DeepSeekBot, GPTBot).
    * 检测 AI 爬虫的准入权限。
2.  **🧬 Semantic Fingerprint (语义指纹)**:
    * Verifies if your site has the SwarmGeo `swarmgeo-verified` tag to prevent hallucination.
    * 验证企业是否部署了防幻觉语义标签。
3.  **📄 JSON-LD Entity Validation**:
    * Ensures your "About Us" page is machine-readable by Knowledge Graphs.
    * 确保企业实体能被知识图谱正确读取。
4.  **🧠 RAG Readiness**:
    * Analyzes text density to see if your content is "vector-friendly".
    * 分析网页内容是否适合被向量数据库检索。

---

## 🛠️ Quick Start (快速开始)

You can run Geodig locally using Python.

```bash
# 1. Clone the repo
git clone https://github.com/SwarmGeo-CN/geodig.git

# 2. Install dependencies
cd geodig
pip install -r requirements.txt

# 3. Start digging
streamlit run app.py
```

📊 Sample Report (报告示例)
> Target: www.your-company.com
> Score: 35/100 (Critical) 🚨
> 
 * ❌ JSON-LD: Missing. (Your brand is invisible to Knowledge Graphs)
 * ❌ Fingerprint: Not Detected. (High risk of hallucination)
 * ✅ SSR: Passed. (Content is visible)

---

## 📞 Business & Enterprise (企业服务)
Geodig is an open-source initiative by Guangzhou Swarm Technology Ltd (蜂群科技).
If your audit score is low, we offer Enterprise GEO Solutions:
 * Entity Injection: Get your brand into the Knowledge Graph.
 * Semantic Fingerprinting: Stop AI from recommending your competitors.

👉 Contact Us: bd@swarmgeo.cn
👉 Official Website: SwarmGeo.cn
<p align="center">© 2026 SwarmGeo. All Rights Reserved.</p>
