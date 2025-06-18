import streamlit as st
import cafaeval
from cafaeval.evaluation import cafa_eval
import numpy as np 
from tqdm import tqdm

obo_file = st.text_input("Entrez le chemin d'accès du fichier (.obo & without "")")
pred_dir = st.text_input("Entrez le chemin d'accès du dossier de prédictions (without "")")
gt_file = st.text_input("Entrez le chemin d'accès du fichier ground_truth (without "")")



df, df_b = cafa_eval(obo_file, pred_dir, gt_file)


st.write(df_b['f'])