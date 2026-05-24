# Writing Slide Phase Reference

## Purpose

Transform your written proposal document into a highly visual, persuasive 10-minute Google Slides presentation. This phase ensures that the written narrative is perfectly adapted for speaking and visual scanning.

## Task

| # | Task | Output File(s) | Description |
|---|---|---|---|
| 1 | Draft 10-Minute Google Slides | `writing-slide/10min-slideData.json`<br>`writing-slide/10min-gas_presentation.js` | 10-minute presentation data JSON file and script |

**CRITICAL: You must produce both files above to complete this phase.**

## Inputs
**CRITICAL (STRICT INPUT RULE):** You MUST use the output of Phase 8: Writing Text (specifically `writing-text/10min-text.md`) as the primary and mandatory input for this phase. You are prohibited from generating slides based on earlier phases without first aligning them with the finalized narrative text from Phase 8. This ensures that the verbal pitch and visual slides are perfectly synchronized.
- **Phase 8 (writing-text/10min-text.md)**

---

## 10-Minute Slide Generation Rules

To draft the 10-Minute Google Slides (`writing-slide/10min-slideData.json` & `writing-slide/10min-gas_presentation.js`), you must rigidly adhere to these universal rules for the presentation structure.

### 1. File & Schema Constraints
- **Map to `slideData` Schema:** Strictly follow the detailed instructions in the reference `gem.prompt.md` to map the proposal to the exact JSON/JS schema required.
- **Speaker Notes Total Volume Constraint (STRICT RULE):** You must strictly control the total sum of all `notes` texts across all slides to precisely match the target length of **3,000 – 3,500 characters** (JP) / 1,200 – 1,300 words (EN). Count only characters inside the `"notes"` fields (ignore spaces/JSON syntax). **CRITICAL:** Do NOT artificially bloat or repeat text on the last slide to meet this requirement. The notes must represent a natural, evenly distributed speech flow across all slides.
- **Conversational Spoken Tone (STRICT RULE):** All speaker `notes` MUST be written in natural spoken language that the speaker will actually say. Do NOT use noun-ending phrases (体言止め) like "〜のご提案". Instead, explicitly write out polite, fluent spoken sentences (e.g., "〜のご提案について、お話しさせていただきます。" or "〜についてご説明します。"). Furthermore, actively avoid unnatural "translated phrasing" such as "この" + adjective (e.g., avoid "この素晴らしい仕組み", "この強力ツール"). Use natural Japanese phrasing like "本提案の仕組み" or "本ツール" instead. Additionally, avoid exaggerated, emotional, or overly dramatic adjectives (e.g., avoid "驚異的な", "素晴らしい", "劇的に", "非常にスピーディーで明確な"). Keep the tone professional, objective, and natural for a Japanese B2B business pitch. Additionally, because the notes are read by Google Text To Speech, you must account for mispronunciations: never write "数倍" (which is read incorrectly), always explicitly write "すう倍" in the notes.
- **Emphasizing Key Words:** You MUST use `[[]]` (double square brackets) to emphasize key words in the slide text (e.g., `[[日米]]で[[粉体一筋]]27年`). The Google Apps Script uses this syntax to emphasize the words in blue color. You MUST NOT use markdown for emphasis in slides.

### 2. Required Slide Sequence (STRICT RULE)
The slides must be generated in this EXACT order:

1. **Video Link Slide:** The very first slide must ALWAYS be a title slide pointing to a video link:
   ```json
   {
      "type": "title",
      "title": "説明動画をクリック",
      "hyperlinkText": "[URL of tinyurl]",
      "date": " ",
      "notes": "説明動画へのリンクをクリックして下さい。"
   },
   ```
2. **Title Slide:** Include one slide for the presentation title.
**CRITICAL INSTRUCTION:** Think about the title of the proposal and the notes of the proposal based on the output of `writing-text/10min-text.md`. The format of JSON object is as follows:
   ```json
   {
      "type": "title",
      "title": "[[Title of the proposal]]",
      "date": " ",
      "notes": "[Title]について、お話しさせていただきます。"
   },
   ```
3. **Self-Introduction Slide:** Include one slide for self-introduction and company introduction immediately after the title slide.
**CRITICAL INSTRUCTION:** Think about the self-introduction and company introduction based on the output of writing-text/10min-text.md. 

4. **Effort Summary Slide:** Include one slide explaining the process used to create the proposal (e.g., using `processList`).
   ```json
  {
    "type": "processList",
    "title": "本提案のために実施した作業",
    "subhead": " ",
    "steps": [
      "調査",
      "課題の定義",
      "解決策の定義",
      "タスク計画",
      "コスト見積",
      "投資対効果"
    ],
    "notes": "この提案を作成するために、調査、課題の定義、解決策の定義、実施計画、コスト見積り、投資対効果の計算の順に作業を行いました。"
  },
   ```

5. **Problem/Solution Pairs:** 
   - **EXACT MAPPING TO SOLUTION DESIGN:** The slides MUST perfectly and exhaustively mirror ALL problems and solutions listed in `solution-design.md`. Omissions are prohibited.
   - **One Slide = ONE Atomic Problem (STRICT SPLIT RULE):** You MUST NOT put different problems into one slide. For example, "用語の違いによる検索機会の損失" and "3Dデータ提供の不足" are two entirely different problems. They MUST be separated into two distinct problem slides (and their corresponding solutions must be separated into two distinct solution slides). Each problem slide MUST contain exactly 1 problem (single root cause). Remove any "また" or "さらに" that introduces a second problem. Use `"type": "headerCards"` for both.
   - **Problem Content Requirements:** Problem slides using `headerCards` MUST contain an `"items"` array (NOT `"cards"`). The `items` must include a `"title": "現状"` and `"title": "機会損失"` item. The `"機会損失"` (Opportunity Cost) `desc` **MUST** include both a quantitative metric and a qualitative narrative.
   - **Speaker Notes Narrative:** The `notes` for problem slides MUST follow the empathetic narrative framework:
     - **Persona:** "I am [Specific Role]..."
     - **Outcome:** "I am trying to [Achieve Outcome]..."
     - **Barriers & Emotion:** "But [Barrier], which makes me feel [Emotion]..."
     - **Root Cause:** "Because [Root Cause]..."
   - **One Slide = ONE Solution (STRICT SPLIT RULE):** Each solution slide MUST contain exactly 1 solution (single root cause, no "また" or "さらに" connecting different issues). You MUST NOT put two different solutions in one slide. For example, "実機常設展示" and "診断ツール" are different solutions and must be separated into distinct slides. Likewise, "30-second AI avatar videos for engagement" and "2-minute technical explanation videos" are different solutions and must be separated. It must be followed IMMEDIATELY by exactly one slide for its single corresponding solution (Problem A -> Solution A -> Problem B -> Solution B). Use `"type": "headerCards"` for both.
   - **CLEAR EXPLANATION IN NATIVE LANGUAGE:** The `title` MUST be translated and expanded into a simple, straightforward explanation in the native language (e.g. Japanese). Use the `subhead` to provide a one-line, jargon-free explanation that requires no prior knowledge. You MUST NOT use raw English labels, jargon, or acronyms directly if they are not instantly understandable.
   - **Solution Content Requirements:** Solution slides using `headerCards` MUST contain an `"items"` array (NOT `"cards"`). The `items` must include a `"title": "特徴"` and `"title": "利点"` item. The `"利点"` (Benefits) `desc` **MUST** include both a quantitative metric and a qualitative narrative.
   - Make sure each notes section expands deeply on the nuances, mechanics, and financial impacts of every single solution.
   - Example for the problem slide
   ```json
   {
      "type": "headerCards",
      "title": "課題1",
      "subhead": "海外展示会での[[声掛け]]が困難",
      "columns": 2,
      "items": [
         {
               "title": "現状",
               "desc": "ネイティブスピーカーではない人は[[躊躇]]\n\n[[一瞬]]の勝負"
         },
         {
               "title": "機会損失",
               "desc": "接触数: \n\n日本ならば1日[[300人]]\nアメリカならば1日[[50人]]"
         }
      ],
      "notes": "展示会の課題は、来場者に話しかけづらいことです。ネイティブスピーカーではない人は、話しかけるのをどうしても躊躇してしまいます。話しかけても、来場者の足を止めるのは、一瞬の勝負です。日本の展示会なら1日に300人ほどに声掛けできますが、海外の展示会だと50人程度にとどまってしまうこともあります。"
   },
   ```
   - Example for the solution slide
   ```json
   {
      "type": "headerCards",
      "title": "解決策1",
      "subhead": "話しかけ用の[[AI動画]]",
      "columns": 2,
      "items": [
         {
               "title": "特徴",
               "desc": "[[30秒]]\n\n[[iPad]]\n\n[[AIクローン]]\n\n"
         },
         {
               "title": "ベネフィット",
               "desc": "[[誰でも]]: ネイティブスピーカーでなくても\n\n[[簡単]]: 画面を見せるだけで\n\nブース来訪者数: [[数倍]]に"
         }
      ],
      "notes": "そこで、解決策としてご提案するのが、話しかけ用のショート動画の作成です。30秒の動画をiPadで見せる形です。ご本人の声をモノマネするAIクローンも作れます。ネイティブスピーカーでなくても誰でもiPadの画面を見せるだけで、来場者の足を止め、ブース来訪者の数がすう倍になります。"
   },
   ```

6. **Video Demo Slide:** Only if a image file that fits the solution exists in input directory,insert a demo slide immediately after the each solution slide.
   - Example
   ```json
   {
      "type": "demoImage",
      "title": "[[Product Name]]",
      "image": "URL of image",
      "points": [
         "[[Point 1]]",
         "[[Point 2]]",
         "[[Point 3]]"
      ],
      "notes": "[[Product Name]]のイメージです。"
   }
   ```

7. **Investment Breakdown Slide:** Include exactly one slide dedicated to the Investment. Never combine this with the ROI slide.
   - Example
   ```json
   {
      "type": "table",
      "title": "投資額",
      "subhead": " ",
      "headers": [
         "コンポーネント",
         "金額",
         "内容"
      ],
      "rows": [
         [
         "初期セットアップ費（一回限り）",
         "$15,000",
         "30秒動画、2分動画、AIメールエージェント、CADポータル、展示設置"
         ],
         [
         "月額リテイナー",
         "$6,000/月",
         "シカゴ展示スペース、Google広告、AI運用、Ph.D.技術営業、月次レポート"
         ],
         [
         "成功報酬",
         "北米売上の12%",
         "AAA Machine経由で成立した売上のみ"
         ]
      ],
      "notes": "投資額の詳細です。初期セットアップ費は一回限りの$15,000で、AIアバター制作、メールエージェント設定、CADポータル構築、コンプライアンスハブ、シカゴ展示設置を含みます。月額リテイナーは$6,000で、シカゴ展示スペース、Google広告管理、AI運用、Ph.D.レベルの技術営業、月次リートレポートを含みます。成功報酬は御社に新規売上が発生した場合のみ12%です。Year 1合計は$87,000。DIY米国子会社の$25万〜40万と比較すると、3分の1以下のコストです。"
   },
    ```

8. **Total Return On Investment (ROI) Slide:** Immediately following the Investment slide, extract the exact calculated metrics (NPV, Return Multiple, Payback Period) into a dedicated ROI Slide (e.g., `kpi`schema).
   - Example
   ```json
   {
      "type": "kpi",
      "title": "投資対効果（ROI）",
      "subhead": "36ヶ月シミュレーション（割引率10%）",
      "items": [
         {
               "title": "必要資金",
               "value": "[[$25,000]]",
               "unit": " "
         },
         {
               "title": "損益分岐",
               "value": "[[$3.0ヶ月]]",
               "unit": " "
         },
         {
               "title": "回収期間",
               "value": "[[13.0ヶ月]]",
               "unit": " "
         },
         {
               "title": "NPV（正味現在価値）",
               "value": "[[$1,718,872]]",
               "unit": "36ヶ月・10%割引率"
         },
         {
               "title": "リターン倍率",
               "value": "[[3.30×]]",
               "unit": "総投資額$25,000に対し$82,500の経済価値"
         },
         {
               "title": "内部収益率",
               "value": "[[151.45%]]",
               "unit": "36ヶ月"
         },
      ],
      "notes": "投資対効果をご説明します。最初の月額ランニングコストが先行しますが、米国EPCエンジニアによる仕様への組み込み（スペックイン）というサイクルの長い成果が第4ヶ月目から出始めます。その結果、累積キャッシュフローが最も低下した底の金額（皆様が用意すべき必要資金）は、開始から第3ヶ月目時点で -$25,000となります。つまり、$25,000の内部留保資金さえ確保していただければ、この米国進出プロジェクトは完全に軌道に乗り自走します。シカゴでオフィスを借りるためだけに発生する莫大な初期費用と比べ、その10分の1以下の資金で実行可能ということです。損益分岐の観点では、回収期間はわずか13.0 ヶ月です。AIアバターによる展示会の圧倒的リード獲得と、3D CADダウンロードからのインバウンド引き合いが機能し始めることで、1年強で初期の$10,000と月々の継続費用を含む全ての総キャッシュアウトフロー（$25,000）は全てカバーされ、それ以後はすべてが純利益として御社に還元されます。投資倍率は 3.30倍 にのぼります。また、10%の保守的な割引率を適用する前提で、このプロジェクトの正味現在価値は $45,820.27です。年換算の内部収益率は 151.45% という高い収益性を確保できます。"
   },
   ```

9. **Next Steps Slide:** Include exactly one dedicated slide for the Next Steps. (e.g., using `timeline`)
- Example for the Next Steps slide
   ```json
   {
      "type": "timeline",
      "title": "次のステップ",
      "subhead": " ",
      "milestones": [
         { "date": "2月29日", "label": "社内承認" },
         { "date": "3月15日", "label": "発注" },
         { "date": "4月1日", "label": "キックオフ" }
      ],
      "notes": "スケジュールについては、2月29日に社内承認、そして3月15日までに発注をお願いいたします。4月1日にはキックオフミーティングを行い、作業を本格的にスタートします。"
   },
   ```

10. **Final Contact Slide:** Include the final slide for contact information.
   - Example:
   ```json
   {
      "type": "bulletCards",
      "title": "連絡先",
      "subhead": " ",
      "items": [
            {
               "title": "○○株式会社 代表取締役 △△ △△",
               "desc": "[[[EMAIL_ADDRESS]]]\n+ 81 - 90 - 1234 - 5678(Japan)\n+ 1 - 123 - 456 - 7890(US)"
            }
      ],
      "notes": "お時間をいただき、ありがとうございました。\n連絡先は、○○までよろしくお願いします。"
   }
   ```

---

## Generate Presentation Output (THE "TOTAL FILE" RULE)

1. **Automated Generation:** You MUST NOT manually generate or update the 9,000+ line JavaScript files yourself.
2. Run the provided Python script `scripts/merge_gas_presentation.py` using `run_command` tool to automatically merge your JSON outputs into the GAS boilerplates.
   ```bash
   python /Users/yasutakairino/international-sales/.agent/skills/proposal-writing/scripts/merge_gas_presentation.py \
     --proposal-dir [PATH_TO_PROPOSAL_DIR] \
     --sample-path /Users/yasutakairino/international-sales/.agent/skills/proposal-writing/assets/gas_presentation_sample.js
   ```

---

## Phase Validation: Final Completeness Check

Before marking the Writing Slide Phase as complete, you MUST verify the existence of these 2 files:
1. [ ] `writing-slide/10min-slideData.json`
2. [ ] `writing-slide/10min-gas_presentation.js`

If any are missing, generate them immediately.

## Phase Validation Checklist

- [ ] Google Slides `slideData` generated AND merged into the full boilerplate (9,000+ lines).
- [ ] **Speaker notes character count explicitly verified** — run a character count on all `notes` fields combined and confirm it falls within the calibrated range.
- [ ] Phase deliverables stored in `writing-slide/` folder
