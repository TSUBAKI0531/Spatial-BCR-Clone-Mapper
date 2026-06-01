# 研究ツール案: RNA-seq×抗体技術 (2026-05-01)

## 提案ツール案（3選）
### 1. Spatial BCR Clone Mapper (空間BCRクローンマッピングツール) 【最有力】
- **解決課題**: 組織切片上のどの位置（TLSなど）に特定のB細胞クローンが存在するかを可視化し、クローン拡大をトラッキングする。
- **実装コスト**: 中
- **ポートフォリオ連携**: `Tissue-Spatial-Analysis` モジュールとして統合。発現変動解析に `RNA-seq DEG解析アプリ` を活用。

### 2. TLS B-cell Exhaustion Scorer
- **ポートフォリオ連携**: `RNA-seq DEG解析アプリ` に疲弊マーカー計算機能を追加。

### 3. Tumor-Infiltrating Antibody Discovery Pipeline
- **ポートフォリオ連携**: `Intrabody-Design-Platform` への新規抗体配列供給。
