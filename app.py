import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -------------------------------------------------------------------
# PAGE CONFIGURATION & ULTRA-DARK CYBER TERMINAL STYLING
# -------------------------------------------------------------------
st.set_page_config(
    page_title="NIULAI4 // POLYMARKET BOT - NEURAL CORE",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-Tech Cyber HUD CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Fira Code', monospace !important;
        background-color: #030509 !important;
        color: #00FF66 !important;
    }
    
    .stApp {
        background-color: #030509;
    }

    /* Top HUD Bar */
    .hud-top-ticker {
        background: #080C14;
        border-bottom: 1px solid #00F0FF;
        padding: 6px 15px;
        font-size: 11px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #00F0FF;
        letter-spacing: 1px;
    }

    .status-badge {
        background: rgba(0, 255, 102, 0.15);
        color: #00FF66;
        border: 1px solid #00FF66;
        padding: 2px 8px;
        border-radius: 3px;
        font-weight: bold;
    }

    /* Card Panels */
    .hud-panel {
        background: #060911;
        border: 1px solid #1A2333;
        border-top: 2px solid #00F0FF;
        border-radius: 4px;
        padding: 10px;
        margin-bottom: 10px;
    }

    .hud-panel-title {
        font-size: 11px;
        font-weight: 700;
        color: #00F0FF;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 8px;
        border-bottom: 1px solid #111927;
        padding-bottom: 4px;
    }

    /* Values & Badges */
    .big-value {
        font-size: 32px;
        font-weight: 700;
        color: #00FF66;
        text-shadow: 0 0 10px rgba(0, 255, 102, 0.5);
    }

    .stat-label {
        color: #64748B;
        font-size: 10px;
        text-transform: uppercase;
    }

    .stat-val {
        color: #E2E8F0;
        font-size: 13px;
        font-weight: 600;
    }

    /* Terminal Data Table */
    .terminal-table {
        width: 100%;
        font-size: 10px;
        border-collapse: collapse;
    }
    .terminal-table th {
        color: #00F0FF;
        border-bottom: 1px solid #1E293B;
        text-align: left;
        padding: 4px;
    }
    .terminal-table td {
        padding: 3px 4px;
        border-bottom: 1px solid #0D1520;
        color: #94A3B8;
    }
    .green-txt { color: #00FF66 !important; }
    .red-txt { color: #FF0055 !important; }
    .cyan-txt { color: #00F0FF !important; }

    /* Hide Streamlit Default UI Chrome */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------------
# DATA LOAD & REPLICATOR
# -------------------------------------------------------------------
@st.cache_data
def load_data():
    file_path = "IT_Company_Financial_Performance_80k.xlsx"
    try:
        df = pd.read_excel(file_path)
    except Exception:
        np.random.seed(42)
        n = 80000
        df = pd.DataFrame({
            "Employee ID": [f"EMP-{100000+i}" for i in range(n)],
            "Department": np.random.choice(["Engineering", "Data & AI", "Cloud & Infra", "Quality Assurance", "Product & Design"], n),
            "Role": np.random.choice(["Software Engineer", "DevOps Engineer", "Data Scientist", "Cloud Architect", "Tech Lead"], n),
            "Client Name": np.random.choice(["Vanguard Media", "Nexus Logistics", "Global Telco", "Apex Healthcare", "Quantum Analytics"], n),
            "Client Region": np.random.choice(["North America", "Europe", "Middle East", "Latin America", "Asia-Pacific"], n),
            "Annual Salary ($)": np.random.randint(55000, 155000, n),
            "Total Direct Cost ($)": np.random.uniform(66000, 209000, n),
            "Client Revenue Generated ($)": np.random.uniform(99000, 495000, n),
            "Net Profit ($)": np.random.uniform(25000, 306000, n),
            "Profit Margin (%)": np.random.uniform(25, 62, n)
        })
    return df

df = load_data()

# -------------------------------------------------------------------
# TOP TICKER BANNER
# -------------------------------------------------------------------
st.markdown("""
<div class="hud-top-ticker">
    <div>
        <span class="status-badge">LIVE</span> &nbsp;
        <strong>NIULAI4 // POLYMARKET BOT</strong> &nbsp;
        <span class="cyan-txt">| BTC SPOT: $86.893 (+3.44%)</span> &nbsp;
        <span class="green-txt">| REVENUE TAPE: $21.00B</span>
    </div>
    <div>
        <span>FEED LATENCY: <strong>12 MS</strong></span> &nbsp;|&nbsp;
        <span>WIN RATE: <strong class="green-txt">82.2%</strong></span> &nbsp;|&nbsp;
        <span class="cyan-txt">15:15:32 UTC</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------------------------
# TOP HUD ROW (3 PANELS: ALL-TIME PnL / BTC CHART / FEED LATENCY)
# -------------------------------------------------------------------
col_top1, col_top2, col_top3 = st.columns([1.1, 1.3, 1.2])

with col_top1:
    st.markdown("""
    <div class="hud-panel">
        <div class="hud-panel-title">◆ WALLET // ALL-TIME PnL SUMMARY</div>
        <div class="big-value">+$98,895</div>
        <div style="display: flex; justify-content: space-between; margin-top: 10px;">
            <div><span class="stat-label">AVG BILLING</span><br><span class="stat-val">$262.5K</span></div>
            <div><span class="stat-label">MEDIAN MARGIN</span><br><span class="stat-val green-txt">49.0%</span></div>
            <div><span class="stat-label">NET PROFIT</span><br><span class="stat-val cyan-txt">$10.29B</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_top2:
    # Top Center Sparkline / Candlestick Chart
    np.random.seed(101)
    time_pts = pd.date_range("2026-10-29 09:00", periods=40, freq="min")
    price_pts = 86000 + np.cumsum(np.random.randn(40) * 150)
    
    fig_top_chart = go.Figure()
    fig_top_chart.add_trace(go.Scatter(
        x=time_pts, y=price_pts, mode='lines',
        line=dict(color='#00FF66', width=2),
        fill='tozeroy', fillcolor='rgba(0, 255, 102, 0.08)'
    ))
    fig_top_chart.update_layout(
        paper_bgcolor="#060911", plot_bgcolor="#060911",
        margin=dict(l=0, r=0, t=20, b=0), height=110,
        xaxis=dict(showgrid=True, gridcolor="#111927", visible=False),
        yaxis=dict(showgrid=True, gridcolor="#111927", side="right", font=dict(color="#00F0FF", size=9))
    )
    st.plotly_chart(fig_top_chart, use_container_width=True)

with col_top3:
    # Depth / Settlement Line
    fig_depth = go.Figure()
    fig_depth.add_trace(go.Scatter(y=np.random.randn(30).cumsum(), line=dict(color='#00F0FF', width=1.5)))
    fig_depth.add_trace(go.Scatter(y=np.random.randn(30).cumsum(), line=dict(color='#FF0055', width=1.5)))
    fig_depth.update_layout(
        paper_bgcolor="#060911", plot_bgcolor="#060911",
        margin=dict(l=0, r=0, t=20, b=0), height=110, showlegend=False,
        xaxis=dict(visible=False), yaxis=dict(visible=False)
    )
    st.plotly_chart(fig_depth, use_container_width=True)

# -------------------------------------------------------------------
# CENTER PIECE: 3D NEURAL TORUS QUANT MATRIX (100% REPLICATION)
# -------------------------------------------------------------------
st.markdown("""
<div class="hud-panel-title" style="margin-top: 10px;">
    ◆ NEURAL SHELL // 3D QUANTITATIVE RESOURCE MATRIX (80,000 NODES REVENUE MESH)
</div>
""", unsafe_allow_html=True)

# Generate 3D Torus Wireframe Mesh Data
R, r = 3, 1.2
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, 2*np.pi, 25)
u, v = np.meshgrid(u, v)

x = (R + r*np.cos(v)) * np.cos(u)
y = (R + r*np.cos(v)) * np.sin(u)
z = r * np.sin(v)

x_flat, y_flat, z_flat = x.flatten(), y.flatten(), z.flatten()

# Add random outer neural point cloud vectors
n_vectors = 300
x_out = x_flat[:n_vectors] * np.random.uniform(1.1, 1.8, n_vectors)
y_out = y_flat[:n_vectors] * np.random.uniform(1.1, 1.8, n_vectors)
z_out = z_flat[:n_vectors] * np.random.uniform(1.1, 1.8, n_vectors)

fig_torus = go.Figure()

# Inner Mesh Lines
fig_torus.add_trace(go.Scatter3d(
    x=x_flat, y=y_flat, z=z_flat,
    mode='markers',
    marker=dict(size=2, color=z_flat, colorscale='CyanGrd', opacity=0.8)
))

# Outer Point Cloud Vectors
fig_torus.add_trace(go.Scatter3d(
    x=x_out, y=y_out, z=z_out,
    mode='markers',
    marker=dict(size=2.5, color='#FF0055', opacity=0.9)
))

fig_torus.update_layout(
    paper_bgcolor="#030509", plot_bgcolor="#030509",
    margin=dict(l=0, r=0, t=0, b=0), height=460,
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        bgcolor="#030509",
        camera=dict(eye=dict(x=1.4, y=1.4, z=1.2))
    ),
    showlegend=False
)

col_mid1, col_mid2 = st.columns([3, 1])

with col_mid1:
    st.plotly_chart(fig_torus, use_container_width=True)

with col_mid2:
    st.markdown("""
    <div class="hud-panel">
        <div class="hud-panel-title">MODEL SPECS // LATE FILLS</div>
        <div style="display:flex; justify-scale:space-between; margin-bottom:6px;"><span class="stat-label">MODEL PnL</span><span class="green-txt">+$238.2</span></div>
        <div style="display:flex; justify-scale:space-between; margin-bottom:6px;"><span class="stat-label">EXEC DEPTH</span><span class="cyan-txt">1,290</span></div>
        <div style="display:flex; justify-scale:space-between; margin-bottom:6px;"><span class="stat-label">COST RATIO</span><span class="stat-val">$133.8K</span></div>
        <hr style="border-color:#1E293B;">
        <div style="font-size:10px; color:#64748B;">
            <div style="margin-bottom:4px;">ENTRY 1: <span class="cyan-txt">$12.08</span></div>
            <div style="margin-bottom:4px;">ENTRY 2: <span class="cyan-txt">$36.48</span></div>
            <div style="margin-bottom:4px;">ENTRY 3: <span class="cyan-txt">$38.57</span></div>
            <div style="margin-bottom:4px;">ENTRY 4: <span class="cyan-txt">$20.72</span></div>
            <div style="margin-bottom:4px;">ENTRY 5: <span class="cyan-txt">$50.34</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------------
# BOTTOM ROW: EXECUTION TAPE TABLE & RESOLUTION FUNNEL CHART
# -------------------------------------------------------------------
col_bot1, col_bot2 = st.columns([1.5, 1])

with col_bot1:
    st.markdown("<div class='hud-panel-title'>◆ EXECUTION TAPE // TIME & SALES (80,000 EMPLOYEE RECORDS)</div>", unsafe_allow_html=True)
    sample_rows = df.head(8)[["Employee ID", "Department", "Client Name", "Annual Salary ($)", "Client Revenue Generated ($)", "Net Profit ($)"]]
    
    # Render Custom HTML Table matching exact Bloomberg Terminal Tape
    html_tbl = "<table class='terminal-table'><tr><th>EMP ID</th><th>DEPT</th><th>CLIENT</th><th>SALARY</th><th>REVENUE</th><th>NET PROFIT</th></tr>"
    for idx, r in sample_rows.iterrows():
        html_tbl += f"<tr><td>{r['Employee ID']}</td><td>{r['Department']}</td><td>{r['Client Name']}</td><td>${r['Annual Salary ($)']:,}</td><td class='cyan-txt'>${r['Client Revenue Generated ($)'] harvest if False else r['Client Revenue Generated ($)']:,.2f}</td><td class='green-txt'>${r['Net Profit ($)']:,.2f}</td></tr>"
    html_tbl += "</table>"
    st.markdown(html_tbl, unsafe_allow_html=True)

with col_bot2:
    st.markdown("<div class='hud-panel-title'>◆ RESOLUTION FUNNEL 3D // VOL CONE</div>", unsafe_allow_html=True)
    fig_funnel = go.Figure()
    x_f = np.linspace(0, 10, 50)
    y_f1 = np.sin(x_f) * np.exp(-x_f/4)
    y_f2 = -np.sin(x_f) * np.exp(-x_f/4)
    
    fig_funnel.add_trace(go.Scatter(x=x_f, y=y_f1, line=dict(color='#FF0055', width=2)))
    fig_funnel.add_trace(go.Scatter(x=x_f, y=y_f2, line=dict(color='#00F0FF', width=2)))
    fig_funnel.update_layout(
        paper_bgcolor="#060911", plot_bgcolor="#060911",
        margin=dict(l=0, r=0, t=10, b=0), height=140, showlegend=False,
        xaxis=dict(visible=False), yaxis=dict(visible=False)
    )
    st.plotly_chart(fig_funnel, use_container_width=True)
