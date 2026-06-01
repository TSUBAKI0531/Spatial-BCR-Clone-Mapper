import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Spatial BCR Clone Mapper")
st.write("連携: Tissue-Spatial-Analysis, RNA-seq DEG解析アプリ")

st.info("プロトタイプ: ランダムな空間座標データにクローンAをマッピングします")
if st.button("マップ生成"):
    df = pd.DataFrame({
        "x": np.random.rand(100) * 10,
        "y": np.random.rand(100) * 10,
        "clone_A_count": np.random.poisson(2, 100)
    })
    
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['x'], df['y'], c=df['clone_A_count'], cmap="Reds", s=100)
    plt.colorbar(scatter, label="Clone A frequency")
    ax.set_title("Spatial Distribution of BCR Clone A")
    st.pyplot(fig)
