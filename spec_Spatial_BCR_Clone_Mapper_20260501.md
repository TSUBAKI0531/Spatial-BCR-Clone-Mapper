# 仕様書: Spatial BCR Clone Mapper

## 1. 概要
空間トランスクリプトミクス（Visium等）のデータと、in situ VDJシーケンスデータを統合し、特定のBCRクローンの空間的分布をプロットする。

## 2. 主要機能
- 空間座標データとクローンIDデータのアップロード
- スポットごとの特定クローンの存在量をヒートマップ/バブルチャート化
- TLS（三次リンパ組織）マーカーとの共局在評価

## 3. 技術スタック
- Python, Streamlit, pandas, matplotlib/seaborn
