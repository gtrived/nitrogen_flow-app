import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import cbsodata


# Set the theme of the app
st.set_page_config(page_title="Nitrogen Flow", page_icon="🌱", layout="wide")

# Example Data: Nitrogen in Livestock Manure Production, Wastewater Treatment, and Emissions
manure_data = cbsodata.get_data('83981ENG')

data_nitrogen_water_treatment = cbsodata.get_data('7477eng')

df_emissions_to_air = cbsodata.get_data('85670ENG')

# Convert data into pandas DataFrames
df_manure = pd.DataFrame(manure_data)
df_wastewater = pd.DataFrame(data_nitrogen_water_treatment)
df_emissions = pd.DataFrame(df_emissions_to_air)

# Title and Introduction
st.title("🌿 Nitrogen Flow")
st.markdown(""" 
Datasets are called via CBS API

The Centraal Bureau voor de Statistiek (CBS), or the Statistics Netherlands, is the Dutch national statistical office. It plays a central role in providing reliable and timely statistical data on a wide range of topics related to the Netherlands. CBS data is widely used by policymakers, researchers, businesses, and the public to analyze trends, make decisions, and understand various aspects of life in the Netherlands.            

This interactive flowchart visualizes the **Nitrogen Flow** and allows you to explore how nitrogen moves through different sectors like **Livestock Manure Production**, **Urban Wastewater Treatment**, and **Emissions**. 
""")

import plotly.graph_objects as go
import streamlit as st

# Function to create a more refined flowchart with proper sequence and alignment
def create_flowchart():
    fig = go.Figure()

    # Define flow steps as nodes in the diagram with better alignment
    nodes = [
        {"id": "TotalExcretion_1", "label": "Total Excretion", "x": 0.1, "y": 0.8},
        {"id": "ExcretionDuringHousing_2", "label": "Excretion During Housing", "x": 0.3, "y": 0.9},
        {"id": "ExcretionDuringGrazing_3", "label": "Excretion During Grazing", "x": 0.3, "y": 0.7},
        {"id": "TotalNitrogenLossesN_4", "label": "Total Nitrogen Losses (N)", "x": 0.5, "y": 0.8},
        {"id": "AmmoniaEmissionsN_5", "label": "Ammonia Emissions (N)", "x": 0.7, "y": 0.7},
        {"id": "OtherGaseousNitrogenLossesN_6", "label": "Other Gaseous Nitrogen Losses (N)", "x": 0.7, "y": 0.9},
        {"id": "EffluentAirScrubbersN_7", "label": "Effluent Air Scrubbers (N)", "x": 0.9, "y": 0.7},
        {"id": "StoredManureAndManureDuringGrazing_8", "label": "Stored Manure & Manure During Grazing", "x": 0.1, "y": 0.5},
        {"id": "ManureRemovalFromFarms_9", "label": "Manure Removal From Farms", "x": 0.3, "y": 0.6},
        {"id": "ManureSupplyToFarms_10", "label": "Manure Supply To Farms", "x": 0.5, "y": 0.6},
        {"id": "ProcessedManureExcludingExports_11", "label": "Processed Manure (Excluding Exports)", "x": 0.7, "y": 0.6},
        {"id": "NetManureExports_12", "label": "Net Manure Exports", "x": 0.9, "y": 0.6},
        {"id": "SpreadingAreaForManure_13", "label": "Spreading Area For Manure", "x": 0.5, "y": 0.4},
        {"id": "UseOfLivestockManureInAgriculture_14", "label": "Use of Livestock Manure in Agriculture", "x": 0.7, "y": 0.4},
    ]

    # Add nodes as scatter points
    for node in nodes:
        fig.add_trace(go.Scatter(
            x=[node["x"]], y=[node["y"]],
            mode="markers+text",
            text=[node["label"]],
            textposition="bottom center",
            marker=dict(size=15, color='royalblue'),
            name=node["label"]
        ))

    # Define connections between steps as arrows
    arrows = [
        {"from": "TotalExcretion_1", "to": "ExcretionDuringHousing_2", "x1": 0.15, "y1": 0.8, "x2": 0.25, "y2": 0.9},
        {"from": "TotalExcretion_1", "to": "ExcretionDuringGrazing_3", "x1": 0.15, "y1": 0.8, "x2": 0.25, "y2": 0.7},
        {"from": "ExcretionDuringHousing_2", "to": "TotalNitrogenLossesN_4", "x1": 0.25, "y1": 0.9, "x2": 0.45, "y2": 0.8},
        {"from": "ExcretionDuringGrazing_3", "to": "TotalNitrogenLossesN_4", "x1": 0.25, "y1": 0.7, "x2": 0.45, "y2": 0.8},
        {"from": "TotalNitrogenLossesN_4", "to": "AmmoniaEmissionsN_5", "x1": 0.45, "y1": 0.8, "x2": 0.65, "y2": 0.7},
        {"from": "TotalNitrogenLossesN_4", "to": "OtherGaseousNitrogenLossesN_6", "x1": 0.45, "y1": 0.8, "x2": 0.65, "y2": 0.9},
        {"from": "AmmoniaEmissionsN_5", "to": "EffluentAirScrubbersN_7", "x1": 0.75, "y1": 0.7, "x2": 0.85, "y2": 0.7},
        {"from": "StoredManureAndManureDuringGrazing_8", "to": "ManureRemovalFromFarms_9", "x1": 0.1, "y1": 0.5, "x2": 0.25, "y2": 0.6},
        {"from": "ManureRemovalFromFarms_9", "to": "ManureSupplyToFarms_10", "x1": 0.25, "y1": 0.6, "x2": 0.45, "y2": 0.6},
        {"from": "ManureSupplyToFarms_10", "to": "ProcessedManureExcludingExports_11", "x1": 0.45, "y1": 0.6, "x2": 0.65, "y2": 0.6},
        {"from": "ProcessedManureExcludingExports_11", "to": "NetManureExports_12", "x1": 0.65, "y1": 0.6, "x2": 0.85, "y2": 0.6},
        {"from": "NetManureExports_12", "to": "SpreadingAreaForManure_13", "x1": 0.85, "y1": 0.6, "x2": 0.65, "y2": 0.4},
        {"from": "SpreadingAreaForManure_13", "to": "UseOfLivestockManureInAgriculture_14", "x1": 0.65, "y1": 0.4, "x2": 0.75, "y2": 0.4},
    ]

    # Add arrows as lines with annotations
    for arrow in arrows:
        fig.add_trace(go.Scatter(
            x=[arrow["x1"], arrow["x2"]], y=[arrow["y1"], arrow["y2"]],
            mode="lines+text",
            line=dict(color='gray', width=2),
            text=["", ""],
            showlegend=False,
            textposition="top center",
            marker=dict(size=5)
        ))

    fig.update_layout(
        title="Nitrogen Flow",
        title_x=0.5,
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False),
        yaxis=dict(showgrid=False, zeroline=False),
        plot_bgcolor='white',
        annotations=[ 
            dict(x=0.1, y=0.8, text="Total Excretion", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.3, y=0.9, text="Excretion During Housing", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.3, y=0.7, text="Excretion During Grazing", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.5, y=0.8, text="Total Nitrogen Losses", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.7, y=0.7, text="Ammonia Emissions", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.7, y=0.9, text="Other Nitrogen Losses", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.9, y=0.7, text="Effluent Air Scrubbers", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.1, y=0.5, text="Stored Manure & Grazing", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.3, y=0.6, text="Manure Removal", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.5, y=0.6, text="Manure Supply", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.7, y=0.6, text="Processed Manure", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.9, y=0.6, text="Net Manure Exports", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.5, y=0.4, text="Spreading Area", showarrow=False, font=dict(size=12, color="black")),
            dict(x=0.7, y=0.4, text="Use in Agriculture", showarrow=False, font=dict(size=12, color="black")),
        ]
    )

    st.plotly_chart(fig)

# Display the flowchart
create_flowchart()


# Provide detailed insights for each node

# Show detailed descriptions based on the selected data
st.markdown("### Detailed Data and Insights")

st.write("""
#### Nitrogen Compounds in Livestock Manure
The nitrogen compounds in livestock manure include various forms of nitrogen released from livestock during different stages such as housing, grazing, and manure treatment processes. Here are the main categories:

These categories help track the nitrogen footprint of the livestock sector and its impact on the environment, including emissions and agricultural nutrient management.
""")


# Filter and clean the manure data
df_manure_filtered = df_manure[['ID', 'ManureAndNutrients', 'Periods', 'TotalExcretion_1', 'ExcretionDuringHousing_2', 'ExcretionDuringGrazing_3', 
                                'TotalNitrogenLossesN_4', 'AmmoniaEmissionsN_5', 'OtherGaseousNitrogenLossesN_6', 'EffluentAirScrubbersN_7', 
                                'StoredManureAndManureDuringGrazing_8', 'ManureRemovalFromFarms_9', 'ManureSupplyToFarms_10', 
                                'ProcessedManureExcludingExports_11', 'NetManureExports_12', 'SpreadingAreaForManure_13', 
                                'UseOfLivestockManureInAgriculture_14']]

# Create columns layout to display filters and charts side by side
col1, col2 = st.columns([1, 2])

# Dropdown to select ManureAndNutrients
with col1:
    st.subheader("Filter Manure and Nutrients Data")

    # Dropdown for ManureAndNutrients
    manure_selector = st.selectbox(
        "Select Manure and Nutrients:",
        options=df_manure_filtered['ManureAndNutrients'].unique(),
        index=0  # Default index
    )

# Filter the DataFrame based on the selected "ManureAndNutrients"
filtered_manure = df_manure_filtered[df_manure_filtered['ManureAndNutrients'] == manure_selector]

# Optional: Display a chart based on filtered data inside col2
with col2:
    st.write(f"Filtered Nitrogen Data for {manure_selector}")

    fig_manure_filtered = px.line(
        filtered_manure, 
        x='Periods', 
        y=['TotalExcretion_1', 'ExcretionDuringHousing_2', 'ExcretionDuringGrazing_3', 'TotalNitrogenLossesN_4', 
           'AmmoniaEmissionsN_5', 'OtherGaseousNitrogenLossesN_6', 'EffluentAirScrubbersN_7', 'StoredManureAndManureDuringGrazing_8',
           'ManureRemovalFromFarms_9', 'ManureSupplyToFarms_10', 'ProcessedManureExcludingExports_11', 'NetManureExports_12', 
           'SpreadingAreaForManure_13', 'UseOfLivestockManureInAgriculture_14'],
        title=f"Nitrogen Compounds in Livestock Manure for {manure_selector}",
        markers=True
    )
    fig_manure_filtered.update_layout(
        xaxis_title="Period", 
        yaxis_title="Nitrogen Compounds (kg)", 
        template="plotly_dark"
    )
    st.plotly_chart(fig_manure_filtered)


# Filter and clean the wastewater treatment data
df_wastewater_filtered = df_wastewater[['Regions', 'Periods', 'NitrogenCompoundsAsNTotal_47']]

# Create columns layout to display filters and charts side by side
col1, col2 = st.columns([1, 2])

# Dropdown to select Region
with col1:
    st.subheader("Waste water treatment")

    # Dropdown for Regions
    region_selector = st.selectbox(
        "Select Region:",
        options=df_wastewater_filtered['Regions'].unique(),
        index=0  # Default index
    )

# Filter the DataFrame based on the selected region (no period selection)
filtered_wastewater = df_wastewater_filtered[df_wastewater_filtered['Regions'] == region_selector]

# Optional: Display a chart based on filtered data inside col2
with col2:
    st.write(f"Filtered Nitrogen Data for {region_selector}")

    fig_wastewater_filtered = px.line(
        filtered_wastewater, 
        x='Periods', 
        y=['NitrogenCompoundsAsNTotal_47'],
        title=f"Nitrogen Compounds in Wastewater Treatment for {region_selector}",
        markers=True
    )
    fig_wastewater_filtered.update_layout(
        xaxis_title="Period", 
        yaxis_title="Nitrogen Compounds (kg)", 
        template="plotly_dark"
    )
    st.plotly_chart(fig_wastewater_filtered)

st.write(""" 
#### Emissions of air polluting substances
The table contains annual figures on the emissions of a number of air pollutants in the Netherlands as calculated according to the European NEC guidelines.
In 2001, the European Parliament and the Council of Europe drew up a directive on national emission ceilings for cross-border air pollution. The directive is simply called the NEC directive. NEC stands for 'National Emission Ceilings'. Until 2020, the directive determined for each Member State the maximum amount of a number of air pollutants that could be emitted annually. As of 2020, the system of national emission ceilings has been replaced by one of national emission reduction obligations.
The guidelines relate to sulphur dioxide (SO2), nitrogen oxides (NOx), ammonia (NH3), volatile organic compounds excluding methane (NMVOC) and particulate matter PM2.5 (particles with a diameter of less than 2.5 micrometres).
The emissions, expressed in kilograms, are broken down by NEC sectors: Energy, Transport, Industry, Agriculture, Waste and Other stationary and mobile sources.

         """)

# Create columns layout to display filters and charts side by side
col1, col2 = st.columns([1, 2])

# Filter and clean the data
df_emissions_filtered = df_emissions[['NECSectors', 'EmissionsToAir', 'Periods', 'EmissionToAir_1']]

# Ensure the Period column is in a suitable format
df_emissions_filtered['Periods'] = df_emissions_filtered['Periods'].astype(str)

# Dropdowns to select NECSectors, EmissionsToAir, and Periods inside col1
with col1:
    st.subheader("Filter Emissions Data")

    # Dropdown for NECSectors
    necs_selector = st.selectbox(
        "Select NECSector:",
        options=df_emissions_filtered['NECSectors'].unique(),
        index=0  # Default index
    )

    # Dropdown for EmissionsToAir
    emissions_selector = st.selectbox(
        "Select Emission Type:",
        options=df_emissions_filtered['EmissionsToAir'].unique(),
        index=0  # Default index
    )

    # Dropdown for Periods
    periods_selector = df_emissions_filtered['Periods'].unique()

# Filter the DataFrame based on the selected dropdown values
filtered_emissions = df_emissions_filtered[
    (df_emissions_filtered['NECSectors'] == necs_selector) & 
    (df_emissions_filtered['EmissionsToAir'] == emissions_selector)
]

# Optional: Display a chart based on filtered data inside col2
with col2:
    st.write(f"Filtered Emissions Data for {necs_selector} - {emissions_selector}")

    fig_emissions_filtered = px.line(filtered_emissions, x='Periods', y='EmissionToAir_1',
                                      title=f"Filtered Emissions Trends for {necs_selector} - {emissions_selector}",
                                      markers=True)
    fig_emissions_filtered.update_layout(xaxis_title="Period", yaxis_title="Emissions (kg)", template="plotly_dark")
    st.plotly_chart(fig_emissions_filtered)
