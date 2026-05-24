# HTML履歴書テンプレートガイド

HTML履歴書テンプレートの構造に関する完全なリファレンスです。

## ドキュメント構造

```html
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>[氏名] - [職種名]</title>
    <style>/* 以下のCSSを参照 */</style>
</head>
<body>
    <div class="resume">
        <div class="header">       <!-- 氏名、ターゲット、連絡先 -->
        <div class="section edu">  <!-- 学歴（簡潔に、上部に配置） -->
        <div class="section">      <!-- 3つのコアアドバンテージ（グリッド） -->
        <div class="section">      <!-- 主要プロジェクト -->
        <div class="section">      <!-- 職務経歴 -->
        <div class="section">      <!-- 主要コンピテンシー（グリッド） -->
        <div class="section">      <!-- スキルタグ -->
        <div class="section">      <!-- AIツール（該当する場合） -->
        <div class="section">      <!-- 資格 -->
    </div>
</body>
</html>
```

## CSS 変数

```css
:root {
    --accent: #6b4c9a;
    --accent-light: #f8f5fc;
    --accent-tag: #ede6f5;
    --text: #333;
    --text-secondary: #555;
    --text-muted: #888;
    --bg: #fff;
}
```

## CSS ルール

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

@page { size: A4; margin: 0; }

body {
    font-family: "Hiragino Sans", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif;
    font-size: 11px;
    line-height: 1.5;
    color: #333;
    background: #fff;
}

.resume {
    width: 210mm;
    min-height: 297mm;
    margin: 0 auto;
    padding: 12mm 18mm;
}

/* ヘッダー */
.header {
    border-bottom: 2px solid var(--accent);
    padding-bottom: 8px;
    margin-bottom: 12px;
}
.name { font-size: 26px; font-weight: 600; color: var(--accent); margin-bottom: 4px; }
.target { font-size: 14px; color: var(--accent); font-weight: 500; margin-bottom: 6px; }
.contact { font-size: 10px; color: #666; display: flex; flex-wrap: wrap; gap: 12px; }
.contact span { display: flex; align-items: center; gap: 4px; }

/* セクション */
.section { margin-bottom: 10px; }
.section-title {
    font-size: 13px; font-weight: 600; color: var(--accent);
    margin-bottom: 6px; display: flex; align-items: center; gap: 6px;
}
.section-title::before {
    content: ""; width: 4px; height: 14px;
    background: var(--accent); border-radius: 2px;
}

/* ハイライト（3カラムグリッド） */
.highlights { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 10px; }
.highlight-item {
    background: var(--accent-light); padding: 8px 10px;
    border-radius: 4px; border-left: 3px solid var(--accent);
}
.highlight-title { font-size: 11px; font-weight: 600; color: var(--accent); margin-bottom: 3px; }
.highlight-desc { font-size: 9px; color: #555; line-height: 1.35; }

/* 職務経歴 */
.work-item { margin-bottom: 8px; }
.work-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 3px; }
.work-company { font-size: 11px; font-weight: 600; color: var(--accent); }
.work-time { font-size: 9px; color: #888; }
.work-role { font-size: 10px; color: #333; margin-bottom: 3px; }
.work-role span { color: #666; }
.work-project { font-size: 9px; color: #666; margin-bottom: 4px; }
.work-desc { font-size: 9px; color: #555; line-height: 1.4; padding-left: 12px; }
.work-desc li { margin-bottom: 1px; }

/* プロジェクト詳細カード */
.project-detail {
    background: #faf8fc; padding: 10px 12px;
    border-radius: 4px; margin-bottom: 10px;
    border-left: 3px solid var(--accent);
}
.project-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px; }
.project-name { font-size: 11px; font-weight: 600; color: var(--accent); }
.project-tag { font-size: 9px; color: var(--accent); background: var(--accent-tag); padding: 2px 6px; border-radius: 3px; }
.project-desc { font-size: 9px; color: #555; line-height: 1.5; }
.project-desc li { margin-bottom: 2px; }

/* スキルグリッド */
.skills-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px; }
.skill-item { display: flex; align-items: flex-start; gap: 6px; }
.skill-label { font-size: 10px; font-weight: 500; color: var(--accent); min-width: 70px; }
.skill-value { font-size: 9px; color: #555; flex: 1; line-height: 1.35; }

/* タグ */
.tag-group { display: flex; flex-wrap: wrap; gap: 5px; }
.tag { font-size: 9px; color: var(--accent); background: var(--accent-tag); padding: 2px 7px; border-radius: 3px; }
.tag-highlight { font-size: 9px; color: #fff; background: var(--accent); padding: 2px 7px; border-radius: 3px; }

/* 学歴 */
.edu-item { display: flex; justify-content: space-between; align-items: baseline; }
.edu-school { font-size: 11px; font-weight: 600; color: var(--accent); }
.edu-time { font-size: 9px; color: #888; }
.edu-detail { font-size: 10px; color: #555; margin-top: 2px; }

/* リストの箇条書き */
ul { list-style: none; }
ul li::before { content: "•"; color: var(--accent); margin-right: 6px; }

/* 印刷設定 */
@media print {
    body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .resume { margin: 0; box-shadow: none; }
}
```

## セクション別の最適化ルール

### コアアドバンテージ（3つのハイライト）
- 各項目をJDの最優先要件（上位2-3個）に対応させる
- タイトル：2〜5文字のスキルラベル
- 説明：具体的な根拠を伴う1〜2文
- 順序：JDに最も関連性の高いものを最初に配置

### 職務経歴
- **関連性の高いロール（JDにマッチ）**: 完全な説明、4〜5項目の箇条書き、実績の数値化
- **隣接するロール（部分的なマッチ）**: 2〜3項目の箇条書き、転用可能なスキルに焦点を当てる
- **関連性の低いロール**: 最大1〜2項目の箇条書き、または簡潔な記述にまとめる
- 重要な用語や数値は**太字**にする
- 職歴の浅い新卒者の場合：代わりにプロジェクトセクションを充実させる

### プロジェクト
- JDに関連するプロジェクト、または主要スキルを実証できるもののみを含める
- 各プロジェクト：名称 ＋ タグ（タイプ/状況）＋ 3〜4項目の箇条書き
- 可能であれば、最も印象的な指標を最初に持ってくる

### スキル ＆ タグ
- **tag-highlight** (塗りつぶし): JDで明示的に要求されているスキル
- **tag** (枠線のみ): 補足的なスキル
- 順序：JD要求スキルを優先し、その後に補足スキルを並べる

## ローカライズ

**日本語履歴書:**
- 連絡先に生年月日を含める
- 写真のプレースホルダーは任意
- 学位の形式：学士/修士/博士

**英語履歴書:**
- 生年月日、写真は含めない
- 学位：BS/MS/PhD
- フォント: `"Inter", "Helvetica Neue", sans-serif`
- 英語の日付形式を使用: Jan 2020 - Mar 2021
