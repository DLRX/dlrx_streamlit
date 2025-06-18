import streamlit as st
import cafaeval
from cafaeval.evaluation import cafa_eval
import numpy as np 
from tqdm import tqdm



obo_file = fr"{st.text_input("Entrez le chemin d'accès du fichier (.obo & without "")")}
pred_dir = fr"{st.text_input("Entrez le chemin d'accès du dossier de prédictions (without "")")}
gt_file = fr"{st.text_input("Entrez le chemin d'accès du fichier ground_truth (without "")")}


if obo_file and pred_dir and gt_file:
    df, df_b = cafa_eval(obo_file, pred_dir, gt_file)


    st.write(df_b['f'])