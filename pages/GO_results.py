import streamlit as st
import cafaeval
from cafaeval.evaluation import cafa_eval
import numpy as np 
from tqdm import tqdm
import os



obo_file = st.text_input("Entrez le chemin d'accès du fichier (.obo & without \"\")")

if obo_file:
    st.write("path is : ", obo_file)
    pred_dir = st.text_input("Entrez le chemin d'accès du dossier de prédictions (without \"\")")
    if pred_dir:
        gt_file = st.text_input("Entrez le chemin d'accès du fichier ground_truth (without \"\")")

if obo_file and pred_dir and gt_file:
    obo_file = os.path.abspath(obo_file)
    pred_dir = os.path.abspath(pred_dir)
    gt_file = os.path.abspath(gt_file)


    obo_file = r"C:\Users\dodol\Documents\LBM\Stage\data\NetGO_results\cafa_evaluation_data\test\abre.obo"
    pred_dir = r"C:\Users\dodol\Documents\LBM\Stage\data\NetGO_results\cafa_evaluation_data\test\predictions"
    gt_file = r"C:\Users\dodol\Documents\LBM\Stage\data\NetGO_results\cafa_evaluation_data\test\g_t.tsv"
    
    df, df_b = cafa_eval(obo_file, pred_dir, gt_file)
    st.write(df_b['f'])