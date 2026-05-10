import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Header
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

st.markdown("### Developed By")
st.write("**MUHAMMAD SOBAN**")
st.write("**Roll No: 25-ME-143**")

st.markdown("---")

# =========================
# UNIT CONVERTER SECTION
# =========================

st.header("🔄 Mechanical Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    [
        "Length (m to cm)",
        "Force (N to kN)",
        "Pressure (Pa to kPa)",
        "Temperature (C to F)"
    ]
)

value = st.number_input("Enter Value", value=0.0)

if conversion_type == "Length (m to cm)":
    result = value * 100
    st.success(f"{value} m = {result} cm")

elif conversion_type == "Force (N to kN)":
    result = value / 1000
    st.success(f"{value} N = {result} kN")

elif conversion_type == "Pressure (Pa to kPa)":
    result = value / 1000
    st.success(f"{value} Pa = {result} kPa")

elif conversion_type == "Temperature (C to F)":
    result = (value * 9/5) + 32
    st.success(f"{value} °C = {result} °F")

st.markdown("---")

# =========================
# MATERIAL DENSITY CHECKER
# =========================

st.header("🧱 Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200
}

selected_material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[selected_material]

st.info(f"Density of {selected_material} = {density} kg/m³")

st.markdown("---")

st.caption("Mechanical Engineering Web App using Streamlit")
