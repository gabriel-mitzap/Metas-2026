# app.py
from __future__ import annotations

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Metas 2026", layout="wide", initial_sidebar_state="expanded")

# -----------------------------
# Styling (Modern Light Theme)
# -----------------------------
st.markdown(
    """
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

      :root {
        --bg: #f8f9fb;
        --text: #1e293b;
        --muted: #64748b;
        --good: #10b981;
        --bad: #ef4444;
        --accent: #3b82f6;
        --card: #ffffff;
        --cardBorder: #e2e8f0;
        --primary-color: #10b981;
      }

      .stApp { 
        background-color: var(--bg); 
        font-family: 'Inter', sans-serif;
      }

      h1, h2, h3, .stSubheader {
        color: var(--text) !important;
        font-weight: 700 !important;
      }

      .block-container { padding-top: 2rem; padding-bottom: 2rem; }

      /* Sidebar Re-design */
      section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid var(--cardBorder);
      }
      
      /* Fix number input visibility in sidebar */
      section[data-testid="stSidebar"] input[type="number"] {
        background-color: #ffffff !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 4px !important;
        padding: 0.5rem !important;
      }
      
      /* Force dark text in all sidebar inputs */
      section[data-testid="stSidebar"] input,
      section[data-testid="stSidebar"] label,
      section[data-testid="stSidebar"] span,
      section[data-testid="stSidebar"] p,
      section[data-testid="stSidebar"] .stNumberInput label,
      section[data-testid="stSidebar"] .stNumberInput input {
        color: #1e293b !important;
      }
      
      /* Ensure placeholder text is visible too */
      section[data-testid="stSidebar"] input::placeholder {
        color: #64748b !important;
      }
      
      section[data-testid="stSidebar"] button[kind="secondary"] {
        background-color: #f1f5f9 !important;
        color: #1e293b !important;
        border: 1px solid #cbd5e1 !important;
      }
      
      section[data-testid="stSidebar"] button[kind="secondary"]:hover {
        background-color: #e2e8f0 !important;
      }
      
      /* Expander styling in sidebar */
      section[data-testid="stSidebar"] [data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 8px !important;
        margin-bottom: 0.5rem !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stExpander"] summary {
        background-color: #f8fafc !important;
        color: #1e293b !important;
        font-weight: 600 !important;
        padding: 0.75rem !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stExpander"] summary:hover {
        background-color: #f1f5f9 !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] {
        background-color: #ffffff !important;
        border: 1.5px dashed #cbd5e1 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
        min-height: 100px !important;
        transition: all 0.2s ease !important;
      }

      /* Neutralize default dark dropzone styles */
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 8px !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"]:hover {
        border-color: #3b82f6 !important;
        background-color: #f8fafc !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] svg {
        color: #64748b !important;
        fill: #64748b !important;
        width: 32px !important;
        height: 32px !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] label,
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] span,
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] p {
        color: #475569 !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stMarkdownContainer"] p {
        color: #475569 !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
        color: #94a3b8 !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
        margin-top: 0.5rem !important;
        background-color: #f1f5f9 !important;
        color: #475569 !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 6px !important;
        padding: 0.375rem 0.75rem !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover {
        background-color: #e2e8f0 !important;
        border-color: #cbd5e1 !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderFile"] {
        display: flex !important;
        align-items: center !important;
        gap: 0.5rem !important;
        padding-top: 0.25rem !important;
      }

      section[data-testid="stSidebar"] [data-testid="stFileUploader"] [data-testid="stFileUploaderDeleteBtn"] {
        margin-left: auto !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] small {
        color: #94a3b8 !important;
        font-size: 0.75rem !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] button {
        margin-top: 0.5rem !important;
        background-color: #f1f5f9 !important;
        color: #475569 !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 6px !important;
        padding: 0.375rem 0.75rem !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
      }
      
      section[data-testid="stSidebar"] [data-testid="stFileUploader"] button:hover {
        background-color: #e2e8f0 !important;
        border-color: #cbd5e1 !important;
      }
      
      .sidebar-header {
        font-size: 1.2rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f1f5f9;
      }

      .sidebar-section {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1.25rem;
        margin-bottom: 1rem;
      }

      .sidebar-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.75rem;
      }

      .sidebar-upload-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem;
        margin-bottom: 1rem;
      }

      .sidebar-upload-title {
        font-size: 0.75rem;
        font-weight: 700;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
      }

      .sidebar-upload-hint {
        color: #475569;
        font-size: 0.8rem;
        margin-top: 0.5rem;
      }

      /* PILLS STYLING */
      div[data-testid="stPills"] button,
      div[data-testid="stPills"] [role="button"],
      div[data-testid="stPills"] div[data-baseweb="button"] {
        border-radius: 20px !important;
        transition: all 0.2s ease !important;
        padding: 0.4rem 1rem !important;
        font-size: 0.9rem !important;
        background-color: transparent !important;
        color: #64748b !important;
        border: 2px solid #cbd5e1 !important;
        border-color: #cbd5e1 !important;
        outline: none !important;
        box-shadow: none !important;
        font-weight: 500 !important;
      }

      div[data-testid="stPills"] span,
      div[data-testid="stPills"] p,
      div[data-testid="stPills"] div {
        color: inherit !important;
      }
      
      div[data-testid="stPills"] button:active,
      div[data-testid="stPills"] button:focus,
      div[data-testid="stPills"] button[aria-pressed="true"],
      div[data-testid="stPills"] [role="button"][aria-pressed="true"],
      div[data-testid="stPills"] div[data-baseweb="button"][aria-pressed="true"] {
        background-color: #10b981 !important;
        border-color: #10b981 !important;
        color: #ffffff !important;
        box-shadow: none !important;
      }
      
      div[data-testid="stPills"] button *,
      div[data-testid="stPills"] [role="button"] *,
      div[data-testid="stPills"] div[data-baseweb="button"] * {
        color: inherit !important;
      }
      
      div[data-testid="stPills"] button:hover,
      div[data-testid="stPills"] [role="button"]:hover,
      div[data-testid="stPills"] div[data-baseweb="button"]:hover {
        background-color: #e2e8f0 !important;
        color: #0f172a !important;
        border-color: #cbd5e1 !important;
      }

      div[data-testid="stPills"] button[aria-pressed="false"],
      div[data-testid="stPills"] [role="button"][aria-pressed="false"],
      div[data-testid="stPills"] div[data-baseweb="button"][aria-pressed="false"] {
        background-color: transparent !important;
        color: #64748b !important;
        border-color: #cbd5e1 !important;
        box-shadow: none !important;
      }

      /* Container/Card Styling */
      [data-testid="stVerticalBlockBorderWrapper"] {
        border: 2px solid #000000 !important;
        background: var(--card) !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
      }

      /* KPI Styling */
      .kpi-card {
        background: var(--card);
        border: 1px solid var(--cardBorder);
        border-radius: 12px;
        padding: 1.25rem;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        position: relative;
        overflow: hidden;
      }

      .kpi-card::before {
        content: "";
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 4px;
        background: var(--stripe, var(--accent));
      }

      .kpi-card .label { 
        color: var(--muted); 
        font-size: 0.75rem; 
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.25rem; 
      }
      
      .kpi-card .value { 
        color: var(--text);
        font-size: 1.75rem; 
        font-weight: 800; 
        line-height: 1.2; 
      }
      
      .kpi-card .sub { 
        color: var(--muted); 
        margin-top: 0.25rem; 
        font-size: 0.85rem; 
      }

      .kpi-good { --stripe: var(--good); }
      .kpi-bad { --stripe: var(--bad); }
      .kpi-accent { --stripe: var(--accent); }

      /* Tabs Styling */
      .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        margin-bottom: 1.5rem;
      }
      .stTabs [data-baseweb="tab"] {
        height: 50px;
        background-color: transparent;
        color: var(--muted);
        font-weight: 600;
      }
      .stTabs [aria-selected="true"] {
        color: #000000 !important;
        border-bottom-color: #000000 !important;
      }

      /* Plotly chart border */
      [data-testid="stPlotlyChart"] {
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 0.75rem;
        background: #ffffff;
      }

      /* Data editor readability */
      [data-testid="stDataEditor"] {
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 12px !important;
        padding: 0.75rem !important;
      }

      /* BaseWeb grid overrides (Streamlit 1.52.x) */
      [data-testid="stDataEditor"] [role="grid"],
      [data-testid="stDataFrame"] [role="grid"] {
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
      }

      [data-testid="stDataEditor"] [role="columnheader"],
      [data-testid="stDataFrame"] [role="columnheader"] {
        background: #dbe3ec !important;
        color: #0f172a !important;
        font-weight: 800 !important;
        border-bottom: 1px solid #cbd5e1 !important;
        font-size: 1rem !important;
        padding-top: 0.45rem !important;
        padding-bottom: 0.45rem !important;
      }

      [data-testid="stDataEditor"] [role="gridcell"],
      [data-testid="stDataFrame"] [role="gridcell"] {
        color: #0f172a !important;
        background: #ffffff !important;
        border-bottom: 1px solid #e5e7eb !important;
        font-size: 0.95rem !important;
        line-height: 1.4 !important;
        padding-top: 0.45rem !important;
        padding-bottom: 0.45rem !important;
      }

      [data-testid="stDataEditor"] [role="row"]:nth-child(even) [role="gridcell"],
      [data-testid="stDataFrame"] [role="row"]:nth-child(even) [role="gridcell"] {
        background: #eef2f7 !important;
      }

      [data-testid="stDataEditor"] input,
      [data-testid="stDataFrame"] input {
        color: #0f172a !important;
        background: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
      }

      /* Mobile responsiveness */
      @media (max-width: 768px) {
        .block-container {
          padding-left: 1rem !important;
          padding-right: 1rem !important;
          padding-top: 1.25rem !important;
          padding-bottom: 1.25rem !important;
        }

        h1 {
          font-size: 2rem !important;
        }

        .stTabs [data-baseweb="tab"] {
          height: 40px !important;
          font-size: 0.9rem !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
          padding: 1rem !important;
        }

        .kpi-card .value {
          font-size: 1.4rem !important;
        }

        [data-testid="stPlotlyChart"] {
          padding: 0.5rem !important;
        }

        [data-testid="stDataEditor"] {
          padding: 0.5rem !important;
        }

        [data-testid="stDataEditor"] [role="columnheader"],
        [data-testid="stDataFrame"] [role="columnheader"] {
          font-size: 0.9rem !important;
          padding-top: 0.35rem !important;
          padding-bottom: 0.35rem !important;
        }

        [data-testid="stDataEditor"] [role="gridcell"],
        [data-testid="stDataFrame"] [role="gridcell"] {
          font-size: 0.9rem !important;
          padding-top: 0.35rem !important;
          padding-bottom: 0.35rem !important;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Schema + state
# -----------------------------
REQUIRED_COLS = ["Área", "Atividade", "Meta", "Completo"]
BASE_COLS_DEFAULT = ["Área", "Atividade", "Meta", "Completo"]

DF_KEY = "df_base_metas"
UPLOAD_NAME_KEY = "last_upload_name_metas"
EDITOR_VERSION_KEY = "editor_version_metas"


def empty_df() -> pd.DataFrame:
    return pd.DataFrame(columns=BASE_COLS_DEFAULT)


def clean_df(raw: pd.DataFrame) -> pd.DataFrame:
    df = raw.copy()
    df.columns = [str(c).strip() for c in df.columns]
    rename_map = {}
    for col in df.columns:
        key = col.strip().lower()
        if key in ("área", "area", "a?rea"):
            rename_map[col] = "Área"
        elif key == "atividade":
            rename_map[col] = "Atividade"
        elif key == "meta":
            rename_map[col] = "Meta"
        elif key == "completo":
            rename_map[col] = "Completo"
    if rename_map:
        df = df.rename(columns=rename_map)
    for c in REQUIRED_COLS:
        if c not in df.columns:
            df[c] = "" if c in ["Área", "Atividade"] else 0.0
    df["Meta"] = pd.to_numeric(df["Meta"], errors="coerce").fillna(0.0)
    df["Completo"] = pd.to_numeric(df["Completo"], errors="coerce").fillna(0.0)
    df["Área"] = df["Área"].astype(str)
    df["Atividade"] = df["Atividade"].astype(str)
    df = df[
        ~(
            (df["Área"].str.strip() == "")
            & (df["Atividade"].str.strip() == "")
            & (df["Meta"] == 0)
            & (df["Completo"] == 0)
        )
    ].reset_index(drop=True)
    return df[REQUIRED_COLS]


if DF_KEY not in st.session_state:
    st.session_state[DF_KEY] = empty_df()
if UPLOAD_NAME_KEY not in st.session_state:
    st.session_state[UPLOAD_NAME_KEY] = None
if EDITOR_VERSION_KEY not in st.session_state:
    st.session_state[EDITOR_VERSION_KEY] = 0

editor_key = f"data_editor_metas_{st.session_state[EDITOR_VERSION_KEY]}"

# -----------------------------
# Sidebar (Structured Design)
# -----------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-header">Configurações</div>', unsafe_allow_html=True)

    # Upload no topo
    st.markdown(
        '<div class="sidebar-upload-card"><div class="sidebar-upload-title">Importar CSV</div>',
        unsafe_allow_html=True,
    )
    uploaded = st.file_uploader("Envie o arquivo CSV", type=["csv"], label_visibility="collapsed")
    st.markdown(
        '<div class="sidebar-upload-hint">Dica: você pode arrastar e soltar o arquivo aqui.</div></div>',
        unsafe_allow_html=True,
    )
    
    # Quick Update
    if not st.session_state[DF_KEY].empty:
        current_df = st.session_state[DF_KEY].copy()
        areas = current_df["Área"].unique()
        
        for area in sorted(areas):
            area_data = current_df[current_df["Área"] == area]
            
            with st.expander(f"Área: {area}", expanded=False):
                for idx, row in area_data.iterrows():
                    atividade = row["Atividade"]
                    meta = row["Meta"]
                    completo = row["Completo"]
                    progress = (completo / meta * 100) if meta > 0 else 0
                    
                    st.markdown(f"**{atividade}**")
                    st.caption(f"Meta: {int(meta)} | Progresso: {progress:.1f}%")
                    
                    new_completo = st.number_input(
                        "Valor completo",
                        min_value=0.0,
                        value=float(completo),
                        step=1.0,
                        key=f"counter_{idx}_{int(completo)}",
                        label_visibility="visible",
                    )
                    
                    if new_completo != completo:
                        st.session_state[DF_KEY].at[idx, "Completo"] = new_completo
                        st.session_state[EDITOR_VERSION_KEY] += 1
                        st.rerun()
                    
                    if idx != area_data.index[-1]:
                        st.divider()

if uploaded is not None and uploaded.name != st.session_state[UPLOAD_NAME_KEY]:
    try:
        imported = pd.read_csv(uploaded)
        st.session_state[DF_KEY] = clean_df(imported)
        st.session_state[UPLOAD_NAME_KEY] = uploaded.name
        st.session_state[EDITOR_VERSION_KEY] += 1
        st.rerun()
    except Exception as e:
        st.sidebar.error(f"Erro: {e}")

# -----------------------------
# Data Processing
# -----------------------------
df = clean_df(st.session_state[DF_KEY]).copy()
TOTAL_MESES = 12.0
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
tick_vals = list(range(0, 13))
tick_text = [""] + meses
quarter_lines_2026 = [3, 6, 9, 12]

if not df.empty:
    df["Progresso_%"] = 0.0
    ok = df["Meta"] > 0
    df.loc[ok, "Progresso_%"] = (df.loc[ok, "Completo"] / df.loc[ok, "Meta"]) * 100
    df["Progresso_%"] = df["Progresso_%"].clip(0, 100).round(1)
    area_ratio = df.groupby("Área", as_index=False).agg(
        Meta_total=("Meta", "sum"),
        Completo_total=("Completo", "sum"),
    )
    area_ratio["Area_ratio"] = 0.0
    ok2 = area_ratio["Meta_total"] > 0
    area_ratio.loc[ok2, "Area_ratio"] = (
        area_ratio.loc[ok2, "Completo_total"] / area_ratio.loc[ok2, "Meta_total"]
    )
    progresso_geral = float(area_ratio["Area_ratio"].mean() * 100.0) if len(area_ratio) else 0.0
    area_sorted = area_ratio.sort_values("Area_ratio", ascending=False).reset_index(drop=True)
    top_area = area_sorted.loc[0, "Área"] if len(area_sorted) else "-"
    top_area_val = float(area_sorted.loc[0, "Area_ratio"] * 100.0) if len(area_sorted) else 0.0
    low_area = area_sorted.loc[len(area_sorted) - 1, "Área"] if len(area_sorted) else "-"
    low_area_val = float(area_sorted.loc[len(area_sorted) - 1, "Area_ratio"] * 100.0) if len(area_sorted) else 0.0
else:
    progresso_geral, top_area, top_area_val, low_area, low_area_val = 0.0, "-", 0.0, "-", 0.0


def render_kpis() -> None:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f'<div class="kpi-card kpi-accent">'
            f'<div class="label">Progresso Geral</div>'
            f'<div class="value">{progresso_geral:0.1f}%</div>'
            f'<div class="sub">Média das Áreas</div>'
            f"</div>",
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f'<div class="kpi-card kpi-good">'
            f'<div class="label">Destaque</div>'
            f'<div class="value">{top_area}</div>'
            f'<div class="sub">Score: {top_area_val:0.1f}%</div>'
            f"</div>",
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f'<div class="kpi-card kpi-bad">'
            f'<div class="label">Menos Avanço</div>'
            f'<div class="value">{low_area}</div>'
            f'<div class="sub">Score: {low_area_val:0.1f}%</div>'
            f"</div>",
            unsafe_allow_html=True,
        )


def build_area_chart_2026(area_df: pd.DataFrame) -> go.Figure:
    a = area_df.copy()
    a["Completo_meses"] = 0.0
    okm = a["Meta"] > 0
    a.loc[okm, "Completo_meses"] = (a.loc[okm, "Completo"] / a.loc[okm, "Meta"]) * TOTAL_MESES
    a["Completo_meses"] = a["Completo_meses"].clip(0.0, TOTAL_MESES)
    a = a.sort_values("Meta", ascending=True)
    
    fig = go.Figure()
    
    fig.add_bar(
        y=a["Atividade"],
        x=[TOTAL_MESES] * len(a),
        orientation="h",
        name="Meta (Ano)",
        marker=dict(color="#f1f5f9", line=dict(color="#e2e8f0", width=1)),
        hovertemplate="Meta: Ano 2026 (12 meses)<extra></extra>",
        showlegend=True,
    )
    
    colors = []
    for prog in a["Progresso_%"]:
        if prog >= 75:
            colors.append("#10b981")
        elif prog >= 50:
            colors.append("#3b82f6")
        elif prog >= 25:
            colors.append("#f59e0b")
        else:
            colors.append("#ef4444")
    
    labels = [
        f"{int(c)}/{int(m)} ({p:.1f}%)" if m > 0 else f"{int(c)}"
        for c, m, p in zip(a["Completo"], a["Meta"], a["Progresso_%"])
    ]
    
    fig.add_bar(
        y=a["Atividade"],
        x=a["Completo_meses"],
        orientation="h",
        marker=dict(color=colors),
        text=labels,
        textposition="outside",
        textfont=dict(size=13, color="#0f172a", family="Inter, sans-serif"),
        hovertemplate="Completo: %{customdata[0]}<br>Progresso: %{customdata[1]}<extra></extra>",
        customdata=list(zip(a["Completo"], a["Progresso_%"].map(lambda v: f"{v:.1f}%"))),
        showlegend=False,
    )
    
    legend_items = [
        ("Excelente (>=75%)", "#10b981"),
        ("Bom (50-74%)", "#3b82f6"),
        ("Atenção (25-49%)", "#f59e0b"),
        ("Crítico (<25%)", "#ef4444"),
    ]
    
    for label, color in legend_items:
        fig.add_bar(
            y=[None],
            x=[None],
            orientation="h",
            name=label,
            marker=dict(color=color),
            showlegend=True,
        )
    
    fig.update_layout(
        barmode="overlay",
        height=max(450, 110 * len(a)),
        margin=dict(l=10, r=100, t=100, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#1e293b", size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.15,
            xanchor="left",
            x=0,
            font=dict(size=11, color="#334155"),
        ),
        xaxis=dict(
            title=dict(text="Meses do Ano 2026", font=dict(size=13, color="#334155")),
            range=[0, 13],
            tickmode="array",
            tickvals=tick_vals,
            ticktext=tick_text,
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color="#0f172a", family="Inter, sans-serif"),
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(size=14, color="#0f172a", family="Inter, sans-serif"),
        ),
    )
    
    for q in quarter_lines_2026:
        fig.add_vline(x=q, line_width=1, line_dash="dot", line_color="#000000")
    
    for i, q_label in enumerate(["Q1", "Q2", "Q3", "Q4"]):
        fig.add_annotation(
            x=1.5 + i * 3,
            y=1.12,
            xref="x",
            yref="paper",
            text=q_label,
            showarrow=False,
            font=dict(color="#1e293b", size=12, family="Inter, sans-serif"),
        )
    
    return fig


def build_resumo_chart(resumo_df: pd.DataFrame) -> go.Figure:
    r = resumo_df.copy().sort_values("Progresso_%", ascending=True)
    
    colors = []
    for prog in r["Progresso_%"]:
        if prog >= 75:
            colors.append("#10b981")
        elif prog >= 50:
            colors.append("#3b82f6")
        elif prog >= 25:
            colors.append("#f59e0b")
        else:
            colors.append("#ef4444")
    
    fig = go.Figure()
    
    fig.add_bar(
        y=r["Área"],
        x=[100] * len(r),
        orientation="h",
        name="Meta (100%)",
        marker=dict(color="#f1f5f9", line=dict(color="#e2e8f0", width=1)),
        hovertemplate="Meta: 100%<extra></extra>",
        showlegend=True,
    )
    
    fig.add_bar(
        y=r["Área"],
        x=r["Progresso_%"].clip(0, 100),
        orientation="h",
        marker=dict(color=colors),
        text=[f"{v:.1f}%" for v in r["Progresso_%"]],
        textposition="outside",
        textfont=dict(size=13, color="#0f172a", family="Inter, sans-serif"),
        hovertemplate="Progresso: %{x:.1f}%<extra></extra>",
        showlegend=False,
    )
    
    legend_items = [
        ("Excelente (>=75%)", "#10b981"),
        ("Bom (50-74%)", "#3b82f6"),
        ("Atenção (25-49%)", "#f59e0b"),
        ("Crítico (<25%)", "#ef4444"),
    ]
    
    for label, color in legend_items:
        fig.add_bar(
            y=[None],
            x=[None],
            orientation="h",
            name=label,
            marker=dict(color=color),
            showlegend=True,
        )
    
    fig.update_layout(
        barmode="overlay",
        height=max(450, 120 * len(r)),
        margin=dict(l=10, r=80, t=100, b=40),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, sans-serif", color="#1e293b", size=12),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.15,
            xanchor="left",
            x=0,
            font=dict(size=11, color="#334155"),
        ),
        xaxis=dict(
            title=dict(text="Progresso (%)", font=dict(size=13, color="#334155")),
            range=[0, 115],
            showgrid=False,
            zeroline=False,
            tickfont=dict(size=12, color="#0f172a", family="Inter, sans-serif"),
        ),
        yaxis=dict(
            showgrid=False,
            tickfont=dict(size=14, color="#0f172a", family="Inter, sans-serif"),
        ),
    )
    
    for q in [25, 50, 75, 100]:
        fig.add_vline(x=q, line_width=1, line_dash="dot", line_color="#000000")
    
    for val in [25, 50, 75, 100]:
        fig.add_annotation(
            x=val,
            y=1.12,
            xref="x",
            yref="paper",
            text=f"{val}%",
            showarrow=False,
            font=dict(color="#1e293b", size=11, family="Inter, sans-serif"),
        )
    
    return fig


# -----------------------------
# Main Layout
# -----------------------------
st.title("Metas 2026")
tab_prog, tab_sum, tab_data = st.tabs(["Progresso", "Resumo", "Dados"])

with tab_prog:
    render_kpis()
    if df.empty:
        st.info('Suba um CSV ou adicione linhas em "Dados".')
    else:
        st.subheader("Progresso por Área")
        areas = sorted(df["Área"].dropna().unique().tolist())
        show_areas = st.pills("Filtrar Áreas", areas, default=areas, selection_mode="multi")
        
        if not show_areas:
            st.warning("Selecione pelo menos 1 Área.")
        else:
            for area in show_areas:
                area_df = df[df["Área"] == area]
                with st.container(border=True):
                    col1, col2 = st.columns([0.95, 0.05])
                    with col1:
                        st.markdown(f"### {area}")
                    st.plotly_chart(build_area_chart_2026(area_df), use_container_width=True, config={"displayModeBar": False})

with tab_sum:
    render_kpis()
    if df.empty:
        st.info('Suba um CSV ou adicione linhas em "Dados".')
    else:
        st.subheader("Resumo Geral")
        resumo = df.groupby("Área", as_index=False).agg(
            Meta_total=("Meta", "sum"),
            Completo_total=("Completo", "sum"),
        )
        resumo["Progresso_%"] = 0.0
        okr = resumo["Meta_total"] > 0
        resumo.loc[okr, "Progresso_%"] = (resumo.loc[okr, "Completo_total"] / resumo.loc[okr, "Meta_total"]) * 100
        resumo["Progresso_%"] = resumo["Progresso_%"].clip(0, 100).round(1)
        with st.container(border=True):
            st.plotly_chart(build_resumo_chart(resumo), use_container_width=True, config={"displayModeBar": False})

with tab_data:
    render_kpis()
    with st.container(border=True):
        st.subheader("Editor de Dados")
        
        base_df = st.session_state[DF_KEY] if DF_KEY in st.session_state else empty_df()
        if base_df.empty:
            st.info("Nenhum dado disponível. Importe um CSV ou adicione dados.")
            st.caption("Dica: você pode colar dados direto na tabela (Ctrl+V).")
        
        # Always create a fresh copy to compare against
        original_df = base_df.copy()
        
        # Display the editor
        edited_df = st.data_editor(
            original_df,
            use_container_width=True,
            hide_index=True,
            num_rows="dynamic",
            height=520,
            key=editor_key,
            column_config={
                "Área": st.column_config.TextColumn("Área", required=True, width="medium"),
                "Atividade": st.column_config.TextColumn("Atividade", required=True, width="large"),
                "Meta": st.column_config.NumberColumn("Meta", min_value=0.0, step=1.0, width="small"),
                "Completo": st.column_config.NumberColumn("Completo", min_value=0.0, step=1.0, width="small"),
            },
        )
        
        # Clean the edited dataframe
        cleaned = clean_df(edited_df)
        
        # Reset indices for proper comparison
        original_reset = original_df.reset_index(drop=True)
        cleaned_reset = cleaned.reset_index(drop=True)
        
        # Check if anything changed
        changed = False
        
        if len(original_reset) != len(cleaned_reset):
            changed = True
        else:
            # Check each column for changes
            for col in REQUIRED_COLS:
                if not original_reset[col].equals(cleaned_reset[col]):
                    changed = True
                    break
        
        # If data changed, update session state and increment version to refresh sidebar
        if changed:
            st.session_state[DF_KEY] = cleaned
            st.session_state[EDITOR_VERSION_KEY] += 1
            st.rerun()


st.set_page_config(page_icon='🗡', page_title='Streamlit Paywall Example')

st.markdown('## Chat with Tyrion Lannister ⚔️')
col1, col2 = st.columns((2,1))
with col1:
    st.markdown(
        f"""
        Chat with Tyrion Lannister to advise you on:
        - Office Politics
        - War Strategy
        - The Targaryens


        #### [Sign Up Now 🤘🏻]({config('https://buy.stripe.com/test_eVqeVc2Ml8Ztfpd6PS1Nu00')})
        """
    )
with col2:
    image = Image.open('./assets/DALL·E 2023-01-08 17.53.04 - futuristic knight robot on a horse in cyberpunk theme.png')
    st.image(image)


st.markdown('### Already have an Account? Login Below👇🏻')
with st.form("login_form"):
    st.write("Login")
    email = st.text_input('Enter Your Email')
    password = st.text_input('Enter Your Password')
    submitted = st.form_submit_button("Login")


if submitted:
    if password == config('SECRET_PASSWORD'):
        st.session_state['logged_in'] = True
        st.text('Succesfully Logged In!')
    else:
        st.text('Incorrect, login credentials.')
        st.session_state['logged_in'] = False


if 'logged_in' in st.session_state.keys():
    if st.session_state['logged_in']:
        st.markdown('## Ask Me Anything')
        question = st.text_input('Ask your question')
        if question != '':
            st.write('I drink and I know things.')
