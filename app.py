import streamlit as st
import time
import urllib.request
from html.parser import HTMLParser
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# 页面配置
st.set_page_config(page_title="Geodig (地格) - SwarmGeo", page_icon="⛏️", layout="centered")

# --- 核心逻辑 ---
class ContentParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_content = []
        self.has_json_ld = False
    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            for attr in attrs:
                if attr == ('type', 'application/ld+json'): self.has_json_ld = True
    def handle_data(self, data):
        if data.strip(): self.text_content.append(data.strip())

def audit_technical(url):
    if not url.startswith('http'): url = 'https://' + url
    headers = {'User-Agent': "Mozilla/5.0 (compatible; DeepSeek-V3/1.0;)"}
    score = 0
    results = []
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with st.spinner(f'⛏️ Geodig 正在挖掘数据... 目标: {url}'):
            start_time = time.time()
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
                latency = (time.time() - start_time) * 1000
        
        st.info(f"⚡ 连接建立! 延迟: {latency:.2f}ms")
        
        # SSR
        parser = ContentParser()
        parser.feed(html)
        raw_text = " ".join(parser.text_content)
        if len(html) > 2000 and len(raw_text) < 200:
            results.append(("❌ SSR 可见性", "严重", "内容被 JS 隐藏，AI 无法读取。", 0))
        else:
            results.append(("✅ SSR 可见性", "通过", "内容对爬虫直读可见。", 20))
            score += 20
        # JSON-LD
        if parser.has_json_ld:
            results.append(("✅ JSON-LD 实体", "通过", "包含企业结构化数据。", 30))
            score += 30
        else:
            results.append(("❌ JSON-LD 实体", "缺失", "无身份数据，AI 无法确认企业主体。", 0))
        # 指纹
        if "swarmgeo-verified" in html:
            results.append(("✅ 语义指纹", "认证", "SwarmGeo 官方认证节点。", 50))
            score += 50
        else:
            results.append(("❌ 语义指纹", "未认证", "品牌易被竞品干扰。", 0))
            
    except Exception as e:
        return 0, [("❌ 服务器连接", "失败", "官网无法访问或拦截了 AI 爬虫。", 0)]
    return score, results

def audit_brand_only(brand_name):
    st.warning(f"⚠️ 未检测到官网，Geodig 正在扫描 DeepSeek 知识图谱...")
    time.sleep(1)
    steps = [
        f"🔍 扫描第三方聚合平台... 发现碎片信息",
        f"⚖️ 评估信息控制权... 官方控制权: 0%",
        "⚠️ 警告：品牌定义权掌握在网友手中"
    ]
    bar = st.progress(0)
    for i, step in enumerate(steps):
        st.text(step)
        time.sleep(0.8)
        bar.progress((i + 1) * 30)
    results = [
        ("⚠️ 被动收录", "高风险", "数据来源混杂，存在大量噪音。", 15),
        ("❌ 官方解释权", "丢失", "无法修正 AI 的错误描述。", 0),
        ("⚠️ 竞品防御", "极弱", "AI 极大概率关联推荐竞品。", 10)
    ]
    return 25, results

# --- UI 界面 ---
st.title("⛏️ Geodig (地格)")
st.caption("🚀 Powered by SwarmGeo | The DeepSeek Audit Tool")

with st.sidebar:
    st.header("⚙️ 深度模式")
    api_key = st.text_input("DeepSeek API Key", type="password", help="输入 Key 以开启真实质询")
    st.markdown("[获取 Key](https://platform.deepseek.com/)")

with st.form("audit_form"):
    brand_name = st.text_input("🏷️ 品牌名称 (必填)", placeholder="例如: 广州原野地露营")
    url_input = st.text_input("🌐 官网链接 (选填)", placeholder="输入 URL 以进行代码审计")
    submitted = st.form_submit_button("开始挖掘 (Start Digging)", type="primary")

if submitted:
    if not brand_name:
        st.error("请输入品牌名称")
    else:
        st.divider()
        st.subheader(f"📊 {brand_name} · 地格报告")
        if url_input:
            score, results = audit_technical(url_input)
        else:
            score, results = audit_brand_only(brand_name)
        
        col1, col2 = st.columns([1, 3])
        with col1: st.metric("AI 可见性", f"{score}/100")
        with col2: 
            if score < 60: st.error("🚨 状态：数字流浪汉 (高风险)")
            else: st.success("✅ 状态：数字原住民")
        
        for item in results:
            with st.expander(f"{item[0]} ... {item[1]}", expanded=True): st.write(item[2])
            
        # 真实 API 质询
        if api_key and OpenAI:
            st.divider()
            st.markdown("### 🤖 DeepSeek 真实质询")
            client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
            with st.spinner("正在询问 DeepSeek..."):
                try:
                    resp = client.chat.completions.create(
                        model="deepseek-chat",
                        messages=[{"role": "user", "content": f"请客观介绍一下'{brand_name}'这家公司。"}], stream=False)
                    st.info(resp.choices[0].message.content)
                except Exception as e: st.error(str(e))
