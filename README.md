# 🕹️ gamehub - レトロ風漢字タイピングゲーム

## 🎮 概要

**gamehub** は、昭和レトロな雰囲気の画面で楽しめる漢字タイピングゲームです。  
ユーザー自身が問題を自由に作成できるため、学習用・娯楽用どちらにも活用できます。

## ✨ 特徴

- レトロ風のUIで懐かしさと遊び心を演出  
- 自作問題を登録して、オリジナルのタイピングチャレンジが可能  
- Djangoベースで構築された拡張性の高い設計  
- 問題は日本語テキストで簡単に追加可能  
- スコア表示やタイム計測など、ゲーム性も充実

## 🛠️ セットアップ方法

```bash
# 仮想環境の作成と起動（任意）
python -m venv venv
source venv/bin/activate  # Windows の場合は venv\Scripts\activate

# 必要パッケージのインストール
pip install -r requirements.txt

# サーバー起動
python manage.py runserver

## 📦 インストール方法

```bash
git clone https://github.com/takeru0528/kanji-typing.git
cd kanji-typing-game
python manage.py runserver
