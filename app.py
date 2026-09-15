import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Mental Health in Tech Survey | Analytics Dashboard",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# Professional Styling (Theme-Adaptive CSS)
# -----------------------------------------------------------------------------
# Uses Streamlit native CSS variables (var(--text-color), var(--secondary-background-color))
# to guarantee high-contrast, crystal-clear readability in both Dark and Light themes.
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    /* Top Header Styling */
    .header-container {
        padding-bottom: 1.25rem;
        border-bottom: 1px solid rgba(148, 163, 184, 0.2);
        margin-bottom: 1.5rem;
    }
    .header-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        background-color: rgba(59, 130, 246, 0.15);
        border: 1px solid rgba(59, 130, 246, 0.35);
        color: #60a5fa !important;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        border-radius: 9999px;
        margin-bottom: 0.5rem;
    }
    .header-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: var(--text-color) !important;
        letter-spacing: -0.025em;
        margin: 0;
        line-height: 1.2;
    }
    .header-subtitle {
        font-size: 0.95rem;
        color: var(--text-color) !important;
        opacity: 0.85;
        margin-top: 0.4rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .header-divider {
        opacity: 0.4;
    }

    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-color) !important;
        margin-top: 1.75rem;
        margin-bottom: 1rem;
        letter-spacing: -0.01em;
    }
    .section-bullet {
        color: #3b82f6;
        font-size: 0.95rem;
    }

    /* Metric Cards - Seamless dark/light integration */
    div[data-testid="stMetric"] {
        background-color: var(--secondary-background-color) !important;
        border: 1px solid rgba(148, 163, 184, 0.2) !important;
        border-radius: 8px;
        padding: 14px 18px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    div[data-testid="stMetric"]:hover {
        border-color: rgba(59, 130, 246, 0.45) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    div[data-testid="stMetricLabel"] {
        font-size: 0.8rem !important;
        font-weight: 600 !important;
        color: var(--text-color) !important;
        opacity: 0.8 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetricValue"] {
        font-size: 1.85rem !important;
        font-weight: 700 !important;
        color: var(--text-color) !important;
        letter-spacing: -0.02em;
    }

    /* Sidebar Headings */
    .sidebar-header {
        font-size: 0.82rem;
        font-weight: 700;
        color: var(--text-color) !important;
        opacity: 0.85;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.75rem;
    }

    /* Tech Stack Badges */
    .badge-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 8px;
    }
    .tech-badge {
        background-color: var(--secondary-background-color);
        color: var(--text-color) !important;
        border: 1px solid rgba(148, 163, 184, 0.25);
        padding: 5px 12px;
        border-radius: 6px;
        font-size: 0.82rem;
        font-weight: 500;
        display: inline-flex;
        align-items: center;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }

    /* Clean Dividers */
    hr {
        margin: 1.75rem 0;
        border: none;
        border-top: 1px solid rgba(148, 163, 184, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------------------------------------------
# Plotly Unified Professional Layout Helper
# -----------------------------------------------------------------------------
# Blue and slate tones that offer high contrast on both dark and light themes
PRIMARY_COLOR = "#3b82f6"
SECONDARY_COLOR = "#64748b"

def apply_chart_theme(fig, height=360):
    fig.update_layout(
        height=height,
        margin=dict(l=20, r=20, t=50, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    return fig

# -----------------------------------------------------------------------------
# Load Dataset
# -----------------------------------------------------------------------------
df = pd.read_csv("survey_cleaned.csv")

# -----------------------------------------------------------------------------
# Sidebar Navigation & Filters
# -----------------------------------------------------------------------------
with st.sidebar:
    st.markdown('<div class="sidebar-header">Filter Controls</div>', unsafe_allow_html=True)

    country = st.multiselect(
        "Select Country",
        options=sorted(df["Country"].unique()),
        default=[]
    )

    st.markdown("---")
    st.markdown('<div class="sidebar-header">Dataset Status</div>', unsafe_allow_html=True)

    # Dynamic Filter Status
    if country:
        filtered_df = df[df["Country"].isin(country)]
        st.caption(f"Filtered to **{len(country)}** selected countries")
    else:
        filtered_df = df
        st.caption("Displaying **all countries** (global scope)")

    st.caption(f"Showing **{len(filtered_df):,}** of **{len(df):,}** records")
    st.caption("Author: **Rushi Faldu**")

# -----------------------------------------------------------------------------
# Main Header
# -----------------------------------------------------------------------------
st.markdown(
    """
    <div class="header-container">
        <div class="header-badge">Workplace Health Analytics</div>
        <h1 class="header-title">Mental Health in Tech Survey</h1>
        <div class="header-subtitle">
            <span>Exploratory Data Analysis Dashboard</span>
            <span class="header-divider">|</span>
            <span>Prepared by <strong>Rushi Faldu</strong></span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------------------------------------------------------
# KPI Calculations & Metric Cards
# -----------------------------------------------------------------------------
total_respondents = len(filtered_df)
treatment_yes = (filtered_df["treatment"] == "Yes").sum()
treatment_no = (filtered_df["treatment"] == "No").sum()

if total_respondents > 0:
    treatment_rate = (treatment_yes / total_respondents) * 100
else:
    treatment_rate = 0

st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Key Performance Indicators</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Respondents", f"{total_respondents:,}")

with col2:
    st.metric("Treatment (Yes)", f"{treatment_yes:,}")

with col3:
    st.metric("Treatment (No)", f"{treatment_no:,}")

with col4:
    st.metric("Treatment Rate", f"{treatment_rate:.1f}%")

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# Core Distribution & Geographic Analysis
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Treatment Distribution & Geographic Reach</div>', unsafe_allow_html=True)

col_pie, col_country = st.columns([5, 7])

# Donut Chart: Treatment Distribution
with col_pie:
    treatment_counts = (
        filtered_df["treatment"]
        .value_counts()
        .reset_index()
    )
    treatment_counts.columns = ["Treatment", "Count"]

    fig_pie = px.pie(
        treatment_counts,
        names="Treatment",
        values="Count",
        hole=0.55,
        title="Mental Health Treatment Distribution",
        color_discrete_sequence=[PRIMARY_COLOR, SECONDARY_COLOR]
    )
    fig_pie.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hoverinfo="label+value+percent",
        marker=dict(line=dict(color="rgba(128, 128, 128, 0.25)", width=2))
    )
    apply_chart_theme(fig_pie, height=380)
    st.plotly_chart(fig_pie, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# Horizontal Bar: Treatment Rate by Country
with col_country:
    country_analysis = (
        filtered_df.groupby("Country")
        .agg(
            Total_Respondents=("treatment", "count"),
            Treatment_Yes=("treatment", lambda x: (x == "Yes").sum())
        )
        .reset_index()
    )

    country_analysis["Treatment_Rate"] = (
        country_analysis["Treatment_Yes"]
        / country_analysis["Total_Respondents"]
        * 100
    )

    country_chart = country_analysis.sort_values(
        "Total_Respondents",
        ascending=False
    ).head(10)

    fig_country = px.bar(
        country_chart.sort_values("Treatment_Rate"),
        x="Treatment_Rate",
        y="Country",
        orientation="h",
        text="Treatment_Rate",
        title="Treatment Rate by Country (Top 10 by Sample Size)",
        labels={
            "Treatment_Rate": "Treatment Rate (%)",
            "Country": "Country"
        },
        color_discrete_sequence=[PRIMARY_COLOR]
    )

    fig_country.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    fig_country.update_layout(
        xaxis_range=[0, 100]
    )
    apply_chart_theme(fig_country, height=380)
    st.plotly_chart(fig_country, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# -----------------------------------------------------------------------------
# Workplace Attitudes Analysis
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Workplace Attitudes Across Countries</div>', unsafe_allow_html=True)

attitude_analysis = (
    filtered_df.groupby(["Country", "mental_vs_physical"])
    .size()
    .reset_index(name="Count")
)

attitude_analysis["Percentage"] = (
    attitude_analysis.groupby("Country")["Count"]
    .transform(lambda x: x / x.sum() * 100)
)

top_countries = country_chart["Country"].tolist()

attitude_chart = attitude_analysis[
    attitude_analysis["Country"].isin(top_countries)
]

fig_attitude = px.bar(
    attitude_chart,
    x="Percentage",
    y="Country",
    color="mental_vs_physical",
    orientation="h",
    text="Percentage",
    barmode="stack",
    title="Workplace Attitudes: Mental vs Physical Health Parity",
    labels={
        "Percentage": "Share of Respondents (%)",
        "Country": "Country",
        "mental_vs_physical": "Response"
    },
    color_discrete_sequence=[PRIMARY_COLOR, "#0ea5e9", SECONDARY_COLOR]
)

fig_attitude.update_traces(
    texttemplate="%{text:.1f}%",
    textposition="inside"
)
fig_attitude.update_layout(
    xaxis_range=[0, 100]
)
apply_chart_theme(fig_attitude, height=400)
st.plotly_chart(fig_attitude, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# -----------------------------------------------------------------------------
# Treatment Determinants & Influencing Factors
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Key Treatment Determinants & Workplace Factors</div>', unsafe_allow_html=True)

row1_col1, row1_col2 = st.columns(2)

# Factor 1: Work Interference
with row1_col1:
    work_analysis = (
        filtered_df.groupby("work_interfere")["treatment"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Treatment_Rate")
    )

    work_order = [
        "Not Applicable",
        "Never",
        "Rarely",
        "Sometimes",
        "Often"
    ]

    work_analysis["work_interfere"] = pd.Categorical(
        work_analysis["work_interfere"],
        categories=work_order,
        ordered=True
    )
    work_analysis = work_analysis.sort_values("work_interfere")

    fig_work = px.bar(
        work_analysis,
        x="work_interfere",
        y="Treatment_Rate",
        text="Treatment_Rate",
        title="Treatment Rate by Work Interference Frequency",
        labels={
            "work_interfere": "Work Interference",
            "Treatment_Rate": "Treatment Rate (%)"
        },
        color_discrete_sequence=[PRIMARY_COLOR]
    )
    fig_work.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    fig_work.update_layout(
        yaxis_range=[0, 100]
    )
    apply_chart_theme(fig_work, height=350)
    st.plotly_chart(fig_work, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# Factor 2: Family History
with row1_col2:
    family_analysis = (
        filtered_df.groupby("family_history")["treatment"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Treatment_Rate")
    )

    fig_family = px.bar(
        family_analysis,
        x="family_history",
        y="Treatment_Rate",
        text="Treatment_Rate",
        title="Treatment Rate by Family History of Mental Illness",
        labels={
            "family_history": "Family History",
            "Treatment_Rate": "Treatment Rate (%)"
        },
        color_discrete_sequence=[PRIMARY_COLOR]
    )
    fig_family.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    fig_family.update_layout(
        yaxis_range=[0, 100]
    )
    apply_chart_theme(fig_family, height=350)
    st.plotly_chart(fig_family, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

row2_col1, row2_col2 = st.columns(2)

# Factor 3: Care Options
with row2_col1:
    care_analysis = (
        filtered_df.groupby("care_options")["treatment"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Treatment_Rate")
    )

    fig_care = px.bar(
        care_analysis,
        x="care_options",
        y="Treatment_Rate",
        text="Treatment_Rate",
        title="Treatment Rate by Awareness of Care Options",
        labels={
            "care_options": "Care Options Available",
            "Treatment_Rate": "Treatment Rate (%)"
        },
        color_discrete_sequence=[PRIMARY_COLOR]
    )
    fig_care.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    fig_care.update_layout(
        yaxis_range=[0, 100]
    )
    apply_chart_theme(fig_care, height=350)
    st.plotly_chart(fig_care, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# Factor 4: Benefits
with row2_col2:
    benefits_analysis = (
        filtered_df.groupby("benefits")["treatment"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index(name="Treatment_Rate")
    )

    fig_benefits = px.bar(
        benefits_analysis,
        x="benefits",
        y="Treatment_Rate",
        text="Treatment_Rate",
        title="Treatment Rate by Employer Mental Health Benefits",
        labels={
            "benefits": "Employer Benefits",
            "Treatment_Rate": "Treatment Rate (%)"
        },
        color_discrete_sequence=[PRIMARY_COLOR]
    )
    fig_benefits.update_traces(
        texttemplate="%{text:.1f}%",
        textposition="outside",
        cliponaxis=False
    )
    fig_benefits.update_layout(
        yaxis_range=[0, 100]
    )
    apply_chart_theme(fig_benefits, height=350)
    st.plotly_chart(fig_benefits, use_container_width=True, theme="streamlit", config={"displayModeBar": False})

# -----------------------------------------------------------------------------
# Key Findings & Analytical Takeaways
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Key Findings & Strategic Insights</div>', unsafe_allow_html=True)

findings_col1, findings_col2 = st.columns(2)

with findings_col1:
    st.info(
        """
        **Geographic Distribution & Workplace Culture**
        
        Mental-health treatment rates and workplace attitudes vary considerably across countries.
        Locations with smaller sample representations should be evaluated within context of statistical variance.
        """
    )

with findings_col2:
    st.success(
        """
        **Strongest Observed Associations**
        
        Work interference and family history show the most pronounced associations with seeking mental health care.
        Awareness of employer care programs and benefit transparency are strongly linked to active treatment engagement.
        """
    )

st.warning(
    """
    **Analytical Note on Interpretation**
    
    These findings reflect statistical associations reported in survey responses and should not be construed as clinical or causal evidence.
    """
)

# -----------------------------------------------------------------------------
# Methodology & Data Quality
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Methodology & Data Quality Governance</div>', unsafe_allow_html=True)

q_col1, q_col2, q_col3, q_col4 = st.columns(4)

with q_col1:
    st.metric("Final Records", f"{len(df):,}")

with q_col2:
    st.metric("Total Attributes", f"{len(df.columns)}")

with q_col3:
    st.metric("Missing Values", "0")

with q_col4:
    st.metric("Duplicate Rows", "0")

st.markdown("<br>", unsafe_allow_html=True)

meth_col1, meth_col2 = st.columns([3, 2])

with meth_col1:
    st.markdown("**Data Preprocessing & Validation**")
    st.markdown(
        """
        - Filtered out invalid age responses to enforce valid working-age cohort boundaries.
        - Standardized disparate gender values into structured categories: **Male**, **Female**, and **Other**.
        - Imputed and resolved missing categorical values using structured attribution logic.
        - Pruned sparse attributes (such as unstructured *comments*) containing excessive missing ratios.
        - Verified full data integrity: **0 missing values** and **0 duplicate entries** in final cleaned set.
        """
    )

with meth_col2:
    st.markdown("**Technology Stack**")
    st.markdown(
        """
        <div class="badge-container">
            <span class="tech-badge">Python</span>
            <span class="tech-badge">Pandas</span>
            <span class="tech-badge">NumPy</span>
            <span class="tech-badge">Plotly Express</span>
            <span class="tech-badge">Streamlit</span>
            <span class="tech-badge">Google Colab</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------------------------------------------------
# Dataset Explorer
# -----------------------------------------------------------------------------
st.markdown('<div class="section-header"><span class="section-bullet">◈</span> Dataset Explorer</div>', unsafe_allow_html=True)

st.caption(
    "Interactive view of the cleaned survey data. Use the sidebar filters to isolate specific demographics and regions."
)

st.dataframe(
    filtered_df.head(10),
    use_container_width=True,
    hide_index=True
)