import logging

import matplotlib.figure
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

_N_SPOTS = 100
_SPATIAL_RANGE = 10.0
_CLONE_LAMBDA = 2


def generate_mock_spatial_data(
    n_spots: int = _N_SPOTS,
    spatial_range: float = _SPATIAL_RANGE,
    clone_lambda: int = _CLONE_LAMBDA,
) -> pd.DataFrame:
    """ランダムな空間トランスクリプトミクス模擬データを生成する。

    実データ統合前のプロトタイプ用モック。各スポットはVisiumビーズに相当する。

    Args:
        n_spots: 生成するスポット数。
        spatial_range: XY座標の最大値（単位: 任意スケール）。
        clone_lambda: クローンA頻度のポアソン分布パラメータ（lambda）。

    Returns:
        "x", "y", "clone_A_count" の3列を持つDataFrame。
        x, y は [0, spatial_range) の一様乱数、
        clone_A_count はポアソン分布に従うカウント値。
    """
    rng = np.random.default_rng()
    df = pd.DataFrame(
        {
            "x": rng.random(n_spots) * spatial_range,
            "y": rng.random(n_spots) * spatial_range,
            "clone_A_count": rng.poisson(clone_lambda, n_spots),
        }
    )
    logger.info(
        "モックデータ生成完了: %d スポット, clone_A_count 合計=%d",
        n_spots,
        int(df["clone_A_count"].sum()),
    )
    return df


def plot_spatial_distribution(df: pd.DataFrame) -> matplotlib.figure.Figure:
    """BCRクローンAの空間的分布を散布図として描画する。

    スポットの色はクローンA頻度に対応したカラーマップ (Reds) で表現する。

    Args:
        df: "x", "y", "clone_A_count" 列を持つDataFrame。
            generate_mock_spatial_data() の出力を想定。

    Returns:
        描画済みのmatplotlib Figureオブジェクト。

    Raises:
        KeyError: 必要な列が存在しない場合。
    """
    required_cols = {"x", "y", "clone_A_count"}
    missing = required_cols - set(df.columns)
    if missing:
        raise KeyError(f"DataFrameに必要な列がありません: {missing}")

    fig, ax = plt.subplots(figsize=(7, 6))
    scatter = ax.scatter(
        df["x"],
        df["y"],
        c=df["clone_A_count"],
        cmap="Reds",
        s=100,
        edgecolors="grey",
        linewidths=0.3,
    )
    plt.colorbar(scatter, ax=ax, label="Clone A frequency")
    ax.set_title("Spatial Distribution of BCR Clone A")
    ax.set_xlabel("X coordinate")
    ax.set_ylabel("Y coordinate")
    logger.info("空間分布グラフ描画完了")
    return fig


def main() -> None:
    """Spatial BCR Clone MapperのStreamlitアプリエントリポイント。"""
    st.title("Spatial BCR Clone Mapper")
    st.write("連携: Tissue-Spatial-Analysis, RNA-seq DEG解析アプリ")

    st.info(
        "プロトタイプ: ランダムな空間座標データにクローンAをマッピングします。\n"
        "実データ利用時は空間座標CSVとクローンIDCSVのアップロード機能に置き換えてください。"
    )

    if st.button("マップ生成"):
        logger.info("マップ生成ボタンが押されました")

        try:
            df = generate_mock_spatial_data()
        except Exception as e:
            st.error(f"データ生成中にエラーが発生しました: {e}")
            logger.error("データ生成エラー: %s", e)
            return

        st.subheader("生成データ（先頭10行）")
        st.dataframe(df.head(10))

        try:
            fig = plot_spatial_distribution(df)
        except KeyError as e:
            st.error(str(e))
            logger.error("グラフ描画エラー: %s", e)
            return

        st.subheader("空間分布マップ")
        st.pyplot(fig)

        st.caption(
            f"スポット数: {len(df)} / "
            f"クローンA検出スポット数: {(df['clone_A_count'] > 0).sum()}"
        )


main()
