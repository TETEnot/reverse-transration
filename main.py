
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

st.components.v1.html(Twitter, width=500, height=1000)

