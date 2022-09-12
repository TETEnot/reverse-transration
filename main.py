
import streamlit as st
from googletrans import Translator

st.title('自動逆翻訳メーカー')
st.header("翻訳したい文 (英語限定)",)

texter = st.text_input("翻訳前 (日本語 ➡ 英語 ➡ 日本語)")

tr = Translator(service_urls=['tramslate.googleapis.com'])
trans1 = tr.translate(texter, dest="en").text
trans2 = tr.translate(trans1, dest="ja").text
"翻訳された文：", trans2

"""

###

"""


st.header("翻訳したい文 (選択可)",)

language = ["アフリカーンス言語", 'アルバニア語', 'アラビア語', 'アゼルバイジャン語', 'バスク語', 'ベンガル語', 'ベラルーシ語', 'ブルガリア語', "カタルーニャ語", '簡体字', '繁体字', 'クロアチア語', 'チェコ語', 'デンマーク語', 'オランダ語', '英語', "エスペラント語", 'エストニア語', 'フィリピン語', 'フィンランド語', 'フランス語', 'ガリシア語', 'グルジア語', 'ドイツ語', "ギリシャ語", 'グジャラート語', 'ハイチ語', 'ヘブライ語', 'ヒンディー語', 'ハンガリー語', 'アイスランド語', 'インドネシア語', 'アイルランド語', 'イタリア語', 'カンナダ語', '韓国語', 'ラテン語', 'ラトビア語', 'リトアニア語', 'マケドニア語', 'マレー語', 'マルタ語', 'ノルウェー語', 'ペルシア語', 'ポーランド語', 'ポルトガル語', 'ルーマニア語', 'ロシア語', 'セルビア語', 'スロバキア語', 'スロベニア語', 'スペイン語', 'スワヒリ語', 'スウェーデン語', 'タミル語', 'テルグ語', 'タイ語',  'トルコ語', 'ウクライナ語', 'ウルドゥー語', 'ベトナム語', 'ウェールズ語', 'インディッシュ語']


    
option = st.selectbox (
    "使用したい言語",
    list(language)
)


if option == "アフリカーンス言語":
    option = "af"
elif option == "アルバニア語":
    option = "sq"
elif option == "アラビア語":
    option = "ar"
elif option == "アゼルバイジャン語":
    option = "az"
elif option == "バスク語":
    option = "eu"
elif option == "ベンガル語":
    option = "bn"
elif option == "ベラルーシ語":
    option = "be"
elif option == "ブルガリア語":
    option = "bg"
elif option == "カタルーニャ語":
    option = "ca"
elif option == "簡体字":
    option = "zh-CN"
elif option == "繁体字":
    option = "zh-TW"
elif option == "クロアチア語":
    option = "hr"
elif option == "チェコ語":
    option = "cs"
elif option == "デンマーク語":
    option = "da"
elif option == "オランダ語":
    option = "nl"
elif option == "英語":
    option = "en"
elif option == "エスペラント語":
    option = "et"
elif option == "エストニア語":
    option = "eo"
elif option == "フィリピン語":
    option = "tl"
elif option == "フィンランド語":
    option = "fi"
elif option == "フランス語":
    option = "fr"
elif option == "ガリシア語":
    option = "gl"
elif option == "グルジア語":
    option = "ka"
elif option == "ドイツ語":
    option = "de"
elif option == "ギリシャ語":
    option = "el"
elif option == "グジャラート語":
    option = "gu"
elif option == "ハイチ語":
    option = "ht"
elif option == "ヘブライ語":
    option = "iw"
elif option == "ヒンディー語":
    option = "hi"
elif option == "ハンガリー語":
    option = "hu"
elif option == "アイスランド語":
    option = "is"
elif option == "インドネシア語":
    option = "id"
elif option == "アイルランド語":
    option = "ga"
elif option == "イタリア語":
    option = "it"
elif option == "カンナダ語":
    option = "kn"
elif option == "韓国語":
    option = "ko"
elif option == "ラテン語":
    option = "la"
elif option == "ラトビア語":
    option = "lv"
elif option == "リトアニア語":
    option = "lt"
elif option == "マケドニア語":
    option = "mk"
elif option == "マレー語":
    option = "ms"
elif option == "マルタ語":
    option = "mt"
elif option == "ノルウェー語":
    option = "no"
elif option == "ペルシア語":
    option = "fa"
elif option == "ポーランド語":
    option = "pl"
elif option == "ポルトガル語":
    option = "pt"
elif option == "ルーマニア語":
    option = "ro"
elif option == "ロシア語":
    option = "ru"
elif option == "セルビア語":
    option = "sr"
elif option == "スロバキア語":
    option = "sk"
elif option == "スロベニア語":
    option = "sl"
elif option == "スペイン語":
    option = "es"
elif option == "スワヒリ語":
    option = "sw"
elif option == "スウェーデン語":
    option = "sv"
elif option == "タミル語":
    option = "ta"
elif option == "テルグ語":
    option = "te"
elif option == "タイ語":
    option = "th"
elif option == "トルコ語":
    option = "tr"
elif option == "ウクライナ語":
    option = "uk"
elif option == "ウルドゥー語":
    option = "ur"
elif option == "ベトナム語":
    option = "vi"
elif option == "ウェールズ語":
    option = "cy"
elif option == "イディッシュ語":
    option = "yi"
else:
    option = "en"

texterA = st.text_input("翻訳前 (日本語 ➡ 選択した語 ➡ 日本語)")

transA1 = tr.translate(texterA, dest="en").text
transA2 = tr.translate(transA1, dest="ja").text
"翻訳された文：", transA2

"""

###

"""

"""

###

"""

"""

###

"""

st.header("主のTwitter")
Twitter = '''
<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">Twitterの検索コマンドを作るコマンドジェネレーターを作りました！<br><br>検索したいワード、ツイート元のユーザーID、いつからいつまでのツイートか、動画か画像か、除外ワードまで入力して作成できます！<br><br>エゴサやおかず探しにお使いください！！<br><br>👇👇👇URL👇👇👇<a href="https://t.co/B04OeIjAQG">https://t.co/B04OeIjAQG</a> <a href="https://t.co/gpZ86zDE0Q">pic.twitter.com/gpZ86zDE0Q</a></p>&mdash; 点丸/Tenmaru (@Tenmaru0101) <a href="https://twitter.com/Tenmaru0101/status/1430320437032980480?ref_src=twsrc%5Etfw">August 25, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
'''

st.components.v1.html(Twitter, width=350, height=1000)

