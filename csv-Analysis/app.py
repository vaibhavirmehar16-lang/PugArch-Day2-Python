import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
    page_title="Employee Analytics Dashboard | PugArch Day 2",
    page_icon="📊",
    layout="wide"
)

st.title("📊 PugArch Day 2: Employee Data Intelligence & Analytics")
st.markdown("An interactive data analytics platform built to evaluate organizational metrics, payroll, and departmental distributions.")

# Data loading
data_path = os.path.join(os.path.dirname(__file__), "data", "employees.csv")

@st.cache_data
def load_data(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

df = load_data(data_path)

if df is None:
    uploaded_file = st.sidebar.file_uploader("Upload employees.csv", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

if df is not None:
    # Sidebar Filters
    st.sidebar.header("Filter Criteria")
    dept_options = ["All"] + sorted(df["department"].dropna().unique().tolist())
    selected_dept = st.sidebar.selectbox("Filter by Department", dept_options)

    filtered_df = df.copy()
    if selected_dept != "All":
        filtered_df = filtered_df[filtered_df["department"] == selected_dept]

    # Executive Metric Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Employees", len(filtered_df))
    with col2:
        st.metric("Average Salary", f"₹{filtered_df['salary'].mean():,.2f}")
    with col3:
        st.metric("Highest Salary", f"₹{filtered_df['salary'].max():,.2f}")
    with col4:
        st.metric("Avg Experience", f"{filtered_df['experience'].mean():.1f} yrs")

    st.markdown("---")

    # Visualizations
    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.subheader("Department Headcount Breakdown")
        dept_counts = filtered_df["department"].value_counts().reset_index()
        dept_counts.columns = ["Department", "Headcount"]
        fig_bar = px.bar(
            dept_counts, 
            x="Department", 
            y="Headcount", 
            color="Headcount",
            color_continuous_scale="Tealgrn", 
            text_auto=True
        )
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, width="stretch")

    with chart_col2:
        st.subheader("Salary Distribution")
        fig_hist = px.histogram(
            filtered_df, 
            x="salary", 
            nbins=10, 
            marginal="box", 
            color_discrete_sequence=["#1f77b4"]
        )
        st.plotly_chart(fig_hist, width="stretch")

    # Experience vs Salary Scatter
    st.subheader("Experience vs Compensation Correlation")
    fig_scatter = px.scatter(
        filtered_df,
        x="experience",
        y="salary",
        color="department",
        size="salary",
        hover_data=["name", "employee_id"],
        labels={"experience": "Years of Experience", "salary": "Salary (INR)"}
    )
    st.plotly_chart(fig_scatter, width="stretch")

    # Detailed Interactive Data Table
    st.subheader("Employee Records")
    st.dataframe(filtered_df, width="stretch")
else:
    st.warning("Please verify that `data/employees.csv` exists or upload a dataset using the sidebar.")