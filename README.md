# Spatial BCR Clone Mapper

**テーマ**: RNA-seq×抗体技術

## 概要

がん微小環境に浸潤するB細胞のBCR配列から、腫瘍局所での空間的共局在スコアおよびターゲット浸潤度インデックスを予測するプロトタイプツールです。BioPythonによる物理化学的特性解析を基盤としたシミュレーションにより、免疫ホット／コールド領域の探索を支援します。結果はPass/Alert 2段階で判定します。

> **注意**: 現行実装はアミノ酸配列ベースのシミュレーションです。空間トランスクリプトミクスデータ（Visium等）およびBCRレパートリーCSVアップロードへの対応は今後の拡張候補です。

## 入力

- アミノ酸配列（VH/VL または CDR3）
- 形式: FASTAまたはプレーンテキスト

## 出力

| スコア | 説明 |
|--------|------|
| Spatial colocalization score | 空間的共局在スコア |
| Target infiltration index | ターゲット浸潤度インデックス |

判定: **Pass / Alert** 2段階（アラート閾値はサイドバーで調整可能）

## 使用技術

- Python
- Streamlit
- BioPython（ProteinAnalysis: MW / pI / Aromaticity / GRAVY 算出）

## ローカル起動方法

```bash
pip install -r requirements.txt
streamlit run app.py
```
