import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- Page Configuration ---
st.set_page_config(
    page_title="Workforce Intelligence Portal | PugArch Day 2",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Modern Custom Styling ---
st.markdown("""
<style>
    /* Metric Card Styling */
    div[data-testid="stMetric"] {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        padding: 1rem 1.25rem;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    div[data-testid="stMetric"] label {
        font-size: 0.85rem;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #0f172a;
        font-weight: 700;
    }
    /* Tabs & Section Headers */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 6px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# --- Data Engine ---
data_path = os.path.join(os.path.dirname(__file__), "data", "employees.csv")

def get_data():
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    # Default fallback dataset
    return pd.DataFrame({
        "employee_id": [101, 102, 103, 104, 105],
        "name": ["Rahul", "Pooja", "Amit", "Neha", "Rohan"],
        "department": ["IT", "HR", "IT", "Finance", "IT"],
        "salary": [55000, 60000, 65000, 70000, 55000],
        "experience": [2, 3, 4, 5, 2]
    })

if "employees_df" not in st.session_state:
    st.session_state.employees_df = get_data()

df = st.session_state.employees_df

# --- Header Area ---
header_col1, header_col2 = st.columns([3, 1])
with header_col1:
    st.title("💼 Workforce Intelligence & Compensation Portal")
    st.caption("An interactive data analytics platform built to evaluate organizational metrics, payroll, and departmental distributions.")

with header_col2:
    st.write("")
    st.download_button(
        label="📥 Export Dataset (CSV)",
        data=df.to_csv(index=False),
        file_name="employees_workforce_data.csv",
        mime="text/csv",
        width="stretch"
    )

st.markdown("---")

# --- Global Sidebar Filters ---
with st.sidebar:
    st.header("🎛️ Analytics Controls")
    
    # Department Filter
    all_depts = ["All Departments"] + sorted(df["department"].dropna().unique().tolist())
    selected_dept = st.selectbox("Department Scope", all_depts)
    
    # Salary Range Filter
    min_sal, max_sal = int(df["salary"].min()), int(df["salary"].max())
    selected_salary = st.slider("Salary Range (₹)", min_sal, max_sal, (min_sal, max_sal), step=5000)
    
    # Experience Filter
    min_exp, max_exp = int(df["experience"].min()), int(df["experience"].max())
    selected_exp = st.slider("Minimum Experience (Years)", min_exp, max_exp, min_exp)

# Filter logic
filtered_df = df.copy()
if selected_dept != "All Departments":
    filtered_df = filtered_df[filtered_df["department"] == selected_dept]
filtered_df = filtered_df[
    (filtered_df["salary"] >= selected_salary[0]) & 
    (filtered_df["salary"] <= selected_salary[1]) &
    (filtered_df["experience"] >= selected_exp)
]

# --- Modular Tab Architecture ---
tab_analytics, tab_directory, tab_management = st.tabs([
    "📈 Executive Dashboard", 
    "📋 Employee Directory & Search", 
    "➕ Register Employee"
])

# ----------------- TAB 1: EXECUTIVE DASHBOARD -----------------
with tab_analytics:
    # KPI Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Filtered Headcount", f"{len(filtered_df)}", delta=f"{len(filtered_df) - len(df)} from total")
    with col2:
        avg_sal = filtered_df['salary'].mean() if not filtered_df.empty else 0
        st.metric("Average Salary", f"₹{avg_sal:,.0f}")
    with col3:
        max_sal = filtered_df['salary'].max() if not filtered_df.empty else 0
        st.metric("Top Compensation", f"₹{max_sal:,.0f}")
    with col4:
        avg_exp = filtered_df['experience'].mean() if not filtered_df.empty else 0
        st.metric("Tenure Benchmark", f"{avg_exp:.1f} yrs")

    st.write("")

    if filtered_df.empty:
        st.warning("No records match the current filter criteria.")
    else:
        # Visual Analytics Row 1
        g1, g2 = st.columns(2)
        with g1:
            st.subheader("Departmental Allocation")
            dept_counts = filtered_df["department"].value_counts().reset_index()
            dept_counts.columns = ["Department", "Staff Count"]
            fig_donut = px.pie(
                dept_counts, 
                names="Department", 
                values="Staff Count", 
                hole=0.45,
                color_discrete_sequence=px.colors.qualitative.Prism
            )
            fig_donut.update_traces(textposition='inside', textinfo='percent+label')
            fig_donut.update_layout(margin=dict(t=20, b=20, l=20, r=20), showlegend=False)
            st.plotly_chart(fig_donut, width="stretch")

        with g2:
            st.subheader("Compensation Distribution")
            fig_hist = px.histogram(
                filtered_df, 
                x="salary", 
                nbins=8, 
                marginal="box",
                labels={"salary": "Salary (INR)"},
                color_discrete_sequence=["#2563eb"]
            )
            fig_hist.update_layout(bargap=0.1, margin=dict(t=20, b=20, l=20, r=20))
            st.plotly_chart(fig_hist, width="stretch")

        # Visual Analytics Row 2
        st.subheader("Tenure vs Compensation Matrix")
        fig_scatter = px.scatter(
            filtered_df,
            x="experience",
            y="salary",
            color="department",
            size="salary",
            hover_name="name",
            hover_data=["employee_id", "department"],
            labels={"experience": "Years of Experience", "salary": "Annual Salary (₹)"},
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig_scatter.update_layout(margin=dict(t=20, b=20, l=20, r=20))
        st.plotly_chart(fig_scatter, width="stretch")

# ----------------- TAB 2: DIRECTORY & SEARCH -----------------
with tab_directory:
    st.subheader("Searchable Staff Roster")
    search_query = st.text_input("🔍 Search by employee name or ID:", placeholder="e.g. Vikram or 107")
    
    display_df = filtered_df.copy()
    if search_query:
        display_df = display_df[
            display_df["name"].astype(str).str.contains(search_query, case=False, na=False) |
            display_df["employee_id"].astype(str).str.contains(search_query, case=False, na=False)
        ]

    st.dataframe(
        display_df.style.format({"salary": "₹{:,.2f}"}),
        width="stretch",
        hide_index=True
    )

# ----------------- TAB 3: DATA ENTRY / CRUD -----------------
with tab_management:
    st.subheader("Onboard New Employee Record")
    st.caption("Entries will immediately reflect across all metrics and charts in this session.")
    
    with st.form("employee_registration_form", clear_on_submit=True):
        f_col1, f_col2 = st.columns(2)
        with f_col1:
            new_id = st.number_input("Employee ID", min_value=1, value=int(df["employee_id"].max() + 1), step=1)
            new_name = st.text_input("Full Name", placeholder="e.g. Priya Sharma")
        with f_col2:
            new_dept = st.selectbox("Department", ["IT", "HR", "Finance", "Sales", "Marketing", "Operations"])
            new_salary = st.number_input("Annual Salary (₹)", min_value=15000, value=60000, step=5000)
            new_exp = st.number_input("Experience (Years)", min_value=0, max_value=40, value=2, step=1)

        submitted = st.form_submit_button("💾 Save Employee Record", width="stretch")
        if submitted:
            if not new_name.strip():
                st.error("Please enter a valid employee name.")
            elif new_id in df["employee_id"].values:
                st.error(f"Employee ID {new_id} already exists. Please choose a unique ID.")
            else:
                new_row = pd.DataFrame([{
                    "employee_id": new_id,
                    "name": new_name.strip(),
                    "department": new_dept,
                    "salary": new_salary,
                    "experience": new_exp
                }])
                st.session_state.employees_df = pd.concat([st.session_state.employees_df, new_row], ignore_index=True)
                # Persist to disk if file exists
                if os.path.exists(data_path):
                    st.session_state.employees_df.to_csv(data_path, index=False)
                st.success(f"Successfully added record for **{new_name.strip()}**! Navigate to the Dashboard or Directory to inspect.")
                st.rerun()