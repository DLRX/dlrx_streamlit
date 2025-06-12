import streamlit as st
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Important pour les environnements sans interface graphique

from matplotlib_venn import venn2
import matplotlib.pyplot as plt

import os

# Crée le dossier s’il n’existe pas
os.makedirs('data', exist_ok=True)


done = False
st.session_state['done'] = done

st.markdown(
    """
    <h1 style='text-align: center;'>Step 1 : Load data that contains columns to compare</h1>
    """,
    unsafe_allow_html=True
)

file = st.file_uploader("Pick a file")

if file:
    df = pd.read_csv(file)
    st.write('Data visualisation', df)


    st.markdown(
        """
        <h1 style='text-align: center;'>Step 2 : select your columns</h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        "You should must select <i>'SeqCluster'</i> & <i>'ClusterNumber'</i> as the first & second column.<br>"
        "Then choose the column to compare",
        unsafe_allow_html=True
    )

    options = st.multiselect(
        'Select in the following case',
        df.columns.tolist() if file is not None and df is not None else []
    )

    st.write('You selected:', options)


    if options:
        df_filtered = df[options]
        st.write('Filtered Data:', df_filtered)
        output_path = "data/filtered_data.csv"
        df_filtered.to_csv(output_path, index=False)
        st.success(f"Filtered data saved to {output_path}")

        st.markdown(
                """
                <h1 style='text-align: center;'>Step 3 : Analyse the tools</h1>
                """,
                unsafe_allow_html=True
            )

        list_CK_Mc = []
        list_CK_pfam = []
        for idx, row in df_filtered.iterrows():
            
            if len(options) > 2 and pd.notna(row[options[-2]]) and row[options[-2]] != ' ':
                list_CK_Mc.append(row['SeqCluster'])
            
            if len(options) > 3 and pd.notna(row[options[-1]]) and row[options[-1]] != ' ':
                list_CK_pfam.append(row['SeqCluster'])

        
        if list_CK_Mc and list_CK_pfam:

            fig, ax = plt.subplots()
            label1 = options[-2] if len(options) >= 2 else 'Set 1'
            label2 = options[-1] if len(options) >= 2 else 'Set 2'
            v = venn2(
                [set(list_CK_Mc), set(list_CK_pfam)],
                set_labels=(label1, label2),
                set_colors=('#1f77b4', '#ff7f0e'),
                ax=ax
            )
            st.pyplot(fig)

        

        st.markdown(
            """
            <style>
            .full-width-button .stButton>button {
                width: 100%;
                height: 3em;
                font-size: 1.2em;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        
        st.session_state['done'] = True

        col = st.container()
        with col:
            btn = st.button("Go to Tools_Intersection", key="tools_intersection", help="Navigate to Tools_Intersection", type="primary")
            st.markdown('<div class="full-width-button"></div>', unsafe_allow_html=True)

        if btn:
            st.switch_page("./pages/Tool_Intersection.py")