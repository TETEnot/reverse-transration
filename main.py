from operator import lt
import streamlit as st
from googletrans import Translator

st.title('自動逆翻訳メーカー')

share = '''
<a href="https://twitter.com/share?ref_src=twsrc%5Etfw" class="twitter-share-button" data-size="large" data-text="自動逆翻訳メーカーを使いました！" data-url="https://tetenot-reverse-transration-main-yi8b3e.streamlitapp.com/" data-via="Tenmaru0101" data-show-count="false">Twitterでシェアする</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
'''
st.components.v1.html(share, height=50)

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

texterA = st.text_input("翻訳前 (日本語 ➡ 選択した語 ➡ 日本語)")


language = ["アフリカーンス言語", 'アルバニア語', 'アラビア語', 'アゼルバイジャン語', 'バスク語', 'ベンガル語', 'ベラルーシ語', 'ブルガリア語', "カタルーニャ語", '簡体字', '繁体字', 'クロアチア語', 'チェコ語', 'デンマーク語', 'オランダ語', '英語', "エスペラント語", 'エストニア語', 'フィリピン語', 'フィンランド語', 'フランス語', 'ガリシア語', 'グルジア語', 'ドイツ語', "ギリシャ語", 'グジャラート語', 'ハイチ語', 'ヘブライ語', 'ヒンディー語', 'ハンガリー語', 'アイスランド語', 'インドネシア語', 'アイルランド語', 'イタリア語', 'カンナダ語', '韓国語', 'ラテン語', 'ラトビア語', 'リトアニア語', 'マケドニア語', 'マレー語', 'マルタ語', 'ノルウェー語', 'ペルシア語', 'ポーランド語', 'ポルトガル語', 'ルーマニア語', 'ロシア語', 'セルビア語', 'スロバキア語', 'スロベニア語', 'スペイン語', 'スワヒリ語', 'スウェーデン語', 'タミル語', 'テルグ語', 'タイ語',  'トルコ語', 'ウクライナ語', 'ウルドゥー語', 'ベトナム語', 'ウェールズ語', 'インディッシュ語']


    
option = st.selectbox (
    "使用したい言語(1回目)",
    list(language)
)


if option == "アフリカーンス言語":
    option = "af"
    transA1 = tr.translate(texterA, dest= "af" ).text
elif option == "アルバニア語":
    option = "sq"
    transA1 = tr.translate(texterA, dest= "sq" ).text
elif option == "アラビア語":
    option = "ar"
    transA1 = tr.translate(texterA, dest= "ar" ).text
elif option == "アゼルバイジャン語":
    option = "az"
    transA1 = tr.translate(texterA, dest= "az" ).text
elif option == "バスク語":
    option = "eu"
    transA1 = tr.translate(texterA, dest= "eu" ).text
elif option == "ベンガル語":
    option = "bn"
    transA1 = tr.translate(texterA, dest= "eu" ).text
elif option == "ベラルーシ語":
    option = "be"
    transA1 = tr.translate(texterA, dest= "be" ).text
elif option == "ブルガリア語":
    option = "bg"
    transA1 = tr.translate(texterA, dest= "bg" ).text
elif option == "カタルーニャ語":
    option = "ca"
    transA1 = tr.translate(texterA, dest= "ca" ).text
elif option == "簡体字":
    option = "zh-CN"
    transA1 = tr.translate(texterA, dest= "zh-CN" ).text
elif option == "繁体字":
    option = "zh-TW"
    transA1 = tr.translate(texterA, dest= "zh-TW" ).text
elif option == "クロアチア語":
    option = "hr"
    transA1 = tr.translate(texterA, dest= "hr" ).text
elif option == "チェコ語":
    option = "cs"
    transA1 = tr.translate(texterA, dest= "cs" ).text
elif option == "デンマーク語":
    option = "da"
    transA1 = tr.translate(texterA, dest= "da" ).text
elif option == "オランダ語":
    option = "nl"
    transA1 = tr.translate(texterA, dest= "nl" ).text
elif option == "英語":
    option = "en"
    transA1 = tr.translate(texterA, dest= "en" ).text
elif option == "エスペラント語":
    option = "et"
    transA1 = tr.translate(texterA, dest= "et" ).text
elif option == "エストニア語":
    option = "eo"
    transA1 = tr.translate(texterA, dest= "eo" ).text
elif option == "フィリピン語":
    option = "tl"
    transA1 = tr.translate(texterA, dest= "tl" ).text
elif option == "フィンランド語":
    option = "fi"
    transA1 = tr.translate(texterA, dest= "fi" ).text
elif option == "フランス語":
    option = "fr"
    transA1 = tr.translate(texterA, dest= "fr" ).text
elif option == "ガリシア語":
    option = "gl"
    transA1 = tr.translate(texterA, dest= "gl" ).text
elif option == "グルジア語":
    option = "ka"
    transA1 = tr.translate(texterA, dest= "ka" ).text
elif option == "ドイツ語":
    option = "de"
    transA1 = tr.translate(texterA, dest= "de" ).text
elif option == "ギリシャ語":
    option = "el"
    transA1 = tr.translate(texterA, dest= "el").text
elif option == "グジャラート語":
    option = "gu"
    transA1 = tr.translate(texterA, dest= "gu" ).text
elif option == "ハイチ語":
    option = "ht"
    transA1 = tr.translate(texterA, dest= "ht" ).text
elif option == "ヘブライ語":
    option = "iw"
    transA1 = tr.translate(texterA, dest= "iw" ).text
elif option == "ヒンディー語":
    option = "hi"
    transA1 = tr.translate(texterA, dest= "hi" ).text
elif option == "ハンガリー語":
    option = "hu"
    transA1 = tr.translate(texterA, dest= "hu" ).text
elif option == "アイスランド語":
    option = "is"
    transA1 = tr.translate(texterA, dest= "is" ).text
elif option == "インドネシア語":
    option = "id"
    transA1 = tr.translate(texterA, dest= "id" ).text
elif option == "アイルランド語":
    option = "ga"
    transA1 = tr.translate(texterA, dest= "ga" ).text
elif option == "イタリア語":
    option = "it"
    transA1 = tr.translate(texterA, dest= "it" ).text
elif option == "カンナダ語":
    option = "kn"
    transA1 = tr.translate(texterA, dest= "kn" ).text
elif option == "韓国語":
    option = "ko"
    transA1 = tr.translate(texterA, dest= "ko" ).text
elif option == "ラテン語":
    option = "la"
    transA1 = tr.translate(texterA, dest= "la" ).text
elif option == "ラトビア語":
    option = "lv"
    transA1 = tr.translate(texterA, dest= "lv" ).text
elif option == "リトアニア語":
    option = "lt"
    transA1 = tr.translate(texterA, dest= "lt" ).text
elif option == "マケドニア語":
    option = "mk"
    transA1 = tr.translate(texterA, dest= "mk" ).text
elif option == "マレー語":
    option = "ms"
    transA1 = tr.translate(texterA, dest= "ms" ).text
elif option == "マルタ語":
    option = "mt"
    transA1 = tr.translate(texterA, dest= "mt" ).text
elif option == "ノルウェー語":
    option = "no"
    transA1 = tr.translate(texterA, dest= "no" ).text
elif option == "ペルシア語":
    option = "fa"
    transA1 = tr.translate(texterA, dest= "fa" ).text
elif option == "ポーランド語":
    option = "pl"
    transA1 = tr.translate(texterA, dest= "pl" ).text
elif option == "ポルトガル語":
    option = "pt"
    transA1 = tr.translate(texterA, dest= "pt" ).text
elif option == "ルーマニア語":
    option = "ro"
    transA1 = tr.translate(texterA, dest= "ro" ).text
elif option == "ロシア語":
    option = "ru"
    transA1 = tr.translate(texterA, dest= "ru" ).text
elif option == "セルビア語":
    option = "sr"
    transA1 = tr.translate(texterA, dest= "sr" ).text
elif option == "スロバキア語":
    option = "sk"
    transA1 = tr.translate(texterA, dest= "sk" ).text
elif option == "スロベニア語":
    option = "sl"
    transA1 = tr.translate(texterA, dest= "sl" ).text
elif option == "スペイン語":
    option = "es"
    transA1 = tr.translate(texterA, dest= "es" ).text
elif option == "スワヒリ語":
    option = "sw"
    transA1 = tr.translate(texterA, dest= "sw" ).text
elif option == "スウェーデン語":
    option = "sv"
    transA1 = tr.translate(texterA, dest= "sv" ).text
elif option == "タミル語":
    option = "ta"
    transA1 = tr.translate(texterA, dest= "ta" ).text
elif option == "テルグ語":
    option = "te"
    transA1 = tr.translate(texterA, dest= "te" ).text
elif option == "タイ語":
    option = "th"
    transA1 = tr.translate(texterA, dest= "th" ).text
elif option == "トルコ語":
    option = "tr"
    transA1 = tr.translate(texterA, dest= "tr" ).text
elif option == "ウクライナ語":
    option = "uk"
    transA1 = tr.translate(texterA, dest= "uk" ).text
elif option == "ウルドゥー語":
    option = "ur"
    transA1 = tr.translate(texterA, dest= "ur" ).text
elif option == "ベトナム語":
    option = "vi"
    transA1 = tr.translate(texterA, dest= "vi" ).text
elif option == "ウェールズ語":
    option = "cy"
    transA1 = tr.translate(texterA, dest= "cy" ).text
elif option == "イディッシュ語":
    option = "yi"
    transA1 = tr.translate(texterA, dest= "yi" ).text
else:
    option = "en"
    transA1 = tr.translate(texterA, dest= "en" ).text

transA2 = tr.translate(transA1, dest="ja").text

"翻訳された文：", transA2



option1 = st.selectbox (
    "使用したい言語(2回目)",
    list(language)
)




if option1 == "アフリカーンス言語":
    option1 = "af"
    transB1 = tr.translate(transA2, dest= "af" ).text
elif option1 == "アルバニア語":
    option1 = "sq"
    transB1 = tr.translate(transA2, dest= "sq" ).text
elif option1 == "アラビア語":
    option1 = "ar"
    transB1 = tr.translate(transA2, dest= "ar" ).text
elif option1 == "アゼルバイジャン語":
    option1 = "az"
    transB1 = tr.translate(transA2, dest= "az" ).text
elif option1 == "バスク語":
    option1 = "eu"
    transB1 = tr.translate(transA2, dest= "eu" ).text
elif option1 == "ベンガル語":
    option1 = "bn"
    transB1 = tr.translate(transA2, dest= "eu" ).text
elif option1 == "ベラルーシ語":
    option1 = "be"
    transB1 = tr.translate(transA2, dest= "be" ).text
elif option1 == "ブルガリア語":
    option1 = "bg"
    transB1 = tr.translate(transA2, dest= "bg" ).text
elif option1 == "カタルーニャ語":
    option1 = "ca"
    transB1 = tr.translate(transA2, dest= "ca" ).text
elif option1 == "簡体字":
    option1 = "zh-CN"
    transB1 = tr.translate(transA2, dest= "zh-CN" ).text
elif option1 == "繁体字":
    option1 = "zh-TW"
    transB1 = tr.translate(transA2, dest= "zh-TW" ).text
elif option1 == "クロアチア語":
    option1 = "hr"
    transB1 = tr.translate(transA2, dest= "hr" ).text
elif option1 == "チェコ語":
    option1 = "cs"
    transB1 = tr.translate(transA2, dest= "cs" ).text
elif option1 == "デンマーク語":
    option1 = "da"
    transB1 = tr.translate(transA2, dest= "da" ).text
elif option1 == "オランダ語":
    option1 = "nl"
    transB1 = tr.translate(transA2, dest= "nl" ).text
elif option1 == "英語":
    option1 = "en"
    transB1 = tr.translate(transA2, dest= "en" ).text
elif option1 == "エスペラント語":
    option1 = "et"
    transB1 = tr.translate(transA2, dest= "et" ).text
elif option1 == "エストニア語":
    option1 = "eo"
    transB1 = tr.translate(transA2, dest= "eo" ).text
elif option1 == "フィリピン語":
    option1 = "tl"
    transB1 = tr.translate(transA2, dest= "tl" ).text
elif option1 == "フィンランド語":
    option1 = "fi"
    transB1 = tr.translate(transA2, dest= "fi" ).text
elif option1 == "フランス語":
    option1 = "fr"
    transB1 = tr.translate(transA2, dest= "fr" ).text
elif option1 == "ガリシア語":
    option1 = "gl"
    transB1 = tr.translate(transA2, dest= "gl" ).text
elif option1 == "グルジア語":
    option1 = "ka"
    transB1 = tr.translate(transA2, dest= "ka" ).text
elif option1 == "ドイツ語":
    option1 = "de"
    transB1 = tr.translate(transA2, dest= "de" ).text
elif option1 == "ギリシャ語":
    option1 = "el"
    transB1 = tr.translate(transA2, dest= "el").text
elif option1 == "グジャラート語":
    option1 = "gu"
    transB1 = tr.translate(transA2, dest= "gu" ).text
elif option1 == "ハイチ語":
    option1 = "ht"
    transB1 = tr.translate(transA2, dest= "ht" ).text
elif option1 == "ヘブライ語":
    option1 = "iw"
    transB1 = tr.translate(transA2, dest= "iw" ).text
elif option1 == "ヒンディー語":
    option1 = "hi"
    transB1 = tr.translate(transA2, dest= "hi" ).text
elif option1 == "ハンガリー語":
    option1 = "hu"
    transB1 = tr.translate(transA2, dest= "hu" ).text
elif option1 == "アイスランド語":
    option1 = "is"
    transB1 = tr.translate(transA2, dest= "is" ).text
elif option1 == "インドネシア語":
    option1 = "id"
    transB1 = tr.translate(transA2, dest= "id" ).text
elif option1 == "アイルランド語":
    option1 = "ga"
    transB1 = tr.translate(transA2, dest= "ga" ).text
elif option1 == "イタリア語":
    option1 = "it"
    transB1 = tr.translate(transA2, dest= "it" ).text
elif option1 == "カンナダ語":
    option1 = "kn"
    transB1 = tr.translate(transA2, dest= "kn" ).text
elif option1 == "韓国語":
    option1 = "ko"
    transB1 = tr.translate(transA2, dest= "ko" ).text
elif option1 == "ラテン語":
    option1 = "la"
    transB1 = tr.translate(transA2, dest= "la" ).text
elif option1 == "ラトビア語":
    option1 = "lv"
    transB1 = tr.translate(transA2, dest= "lv" ).text
elif option1 == "リトアニア語":
    option1 = "lt"
    transB1 = tr.translate(transA2, dest= "lt" ).text
elif option1 == "マケドニア語":
    option1 = "mk"
    transB1 = tr.translate(transA2, dest= "mk" ).text
elif option1 == "マレー語":
    option1 = "ms"
    transB1 = tr.translate(transA2, dest= "ms" ).text
elif option1 == "マルタ語":
    option1 = "mt"
    transB1 = tr.translate(transA2, dest= "mt" ).text
elif option1 == "ノルウェー語":
    option1 = "no"
    transB1 = tr.translate(transA2, dest= "no" ).text
elif option1 == "ペルシア語":
    option1 = "fa"
    transB1 = tr.translate(transA2, dest= "fa" ).text
elif option1 == "ポーランド語":
    option1 = "pl"
    transB1 = tr.translate(transA2, dest= "pl" ).text
elif option1 == "ポルトガル語":
    option1 = "pt"
    transB1 = tr.translate(transA2, dest= "pt" ).text
elif option1 == "ルーマニア語":
    option1 = "ro"
    transB1 = tr.translate(transA2, dest= "ro" ).text
elif option1 == "ロシア語":
    option1 = "ru"
    transB1 = tr.translate(transA2, dest= "ru" ).text
elif option1 == "セルビア語":
    option1 = "sr"
    transB1 = tr.translate(transA2, dest= "sr" ).text
elif option1 == "スロバキア語":
    option1 = "sk"
    transB1 = tr.translate(transA2, dest= "sk" ).text
elif option1 == "スロベニア語":
    option1 = "sl"
    transB1 = tr.translate(transA2, dest= "sl" ).text
elif option1 == "スペイン語":
    option1 = "es"
    transB1 = tr.translate(transA2, dest= "es" ).text
elif option1 == "スワヒリ語":
    option1 = "sw"
    transB1 = tr.translate(transA2, dest= "sw" ).text
elif option1 == "スウェーデン語":
    option1 = "sv"
    transB1 = tr.translate(transA2, dest= "sv" ).text
elif option1 == "タミル語":
    option1 = "ta"
    transB1 = tr.translate(transA2, dest= "ta" ).text
elif option1 == "テルグ語":
    option1 = "te"
    transB1 = tr.translate(transA2, dest= "te" ).text
elif option1 == "タイ語":
    option1 = "th"
    transB1 = tr.translate(transA2, dest= "th" ).text
elif option1 == "トルコ語":
    option1 = "tr"
    transB1 = tr.translate(transA2, dest= "tr" ).text
elif option1 == "ウクライナ語":
    option1 = "uk"
    transB1 = tr.translate(transA2, dest= "uk" ).text
elif option1 == "ウルドゥー語":
    option1 = "ur"
    transB1 = tr.translate(transA2, dest= "ur" ).text
elif option1 == "ベトナム語":
    option1 = "vi"
    transB1 = tr.translate(transA2, dest= "vi" ).text
elif option1 == "ウェールズ語":
    option1 = "cy"
    transB1 = tr.translate(transA2, dest= "cy" ).text
elif option1 == "イディッシュ語":
    option1 = "yi"
    transB1 = tr.translate(transA2, dest= "yi" ).text
else:
    option1 = "en"
    transB1 = tr.translate(transA2, dest= "en" ).text


transB2 = tr.translate(transB1, dest="ja").text

"翻訳された文：", transB2




option2 = st.selectbox (
    "使用したい言語(3回目)",
    list(language)
)




if option2 == "アフリカーンス言語":
    option2 = "af"
    transC1 = tr.translate(transB2, dest= "af" ).text
elif option2 == "アルバニア語":
    option2 = "sq"
    transC1 = tr.translate(transB2, dest= "sq" ).text
elif option2 == "アラビア語":
    option2 = "ar"
    transC1 = tr.translate(transB2, dest= "ar" ).text
elif option2 == "アゼルバイジャン語":
    option2 = "az"
    transC1 = tr.translate(transB2, dest= "az" ).text
elif option2 == "バスク語":
    option2 = "eu"
    transC1 = tr.translate(transB2, dest= "eu" ).text
elif option2 == "ベンガル語":
    option2 = "bn"
    transC1 = tr.translate(transB2, dest= "eu" ).text
elif option2 == "ベラルーシ語":
    option2 = "be"
    transC1 = tr.translate(transB2, dest= "be" ).text
elif option2 == "ブルガリア語":
    option2 = "bg"
    transC1 = tr.translate(transB2, dest= "bg" ).text
elif option2 == "カタルーニャ語":
    option2 = "ca"
    transC1 = tr.translate(transB2, dest= "ca" ).text
elif option2 == "簡体字":
    option2 = "zh-CN"
    transC1 = tr.translate(transB2, dest= "zh-CN" ).text
elif option2 == "繁体字":
    option2 = "zh-TW"
    transC1 = tr.translate(transB2, dest= "zh-TW" ).text
elif option2 == "クロアチア語":
    option2 = "hr"
    transC1 = tr.translate(transB2, dest= "hr" ).text
elif option2 == "チェコ語":
    option2 = "cs"
    transC1 = tr.translate(transB2, dest= "cs" ).text
elif option2 == "デンマーク語":
    option2 = "da"
    transC1 = tr.translate(transB2, dest= "da" ).text
elif option2 == "オランダ語":
    option2 = "nl"
    transC1 = tr.translate(transB2, dest= "nl" ).text
elif option2 == "英語":
    option2 = "en"
    transC1 = tr.translate(transB2, dest= "en" ).text
elif option2 == "エスペラント語":
    option2 = "et"
    transC1 = tr.translate(transB2, dest= "et" ).text
elif option2 == "エストニア語":
    option2 = "eo"
    transC1 = tr.translate(transB2, dest= "eo" ).text
elif option2 == "フィリピン語":
    option2 = "tl"
    transC1 = tr.translate(transB2, dest= "tl" ).text
elif option2 == "フィンランド語":
    option2 = "fi"
    transC1 = tr.translate(transB2, dest= "fi" ).text
elif option2 == "フランス語":
    option2 = "fr"
    transC1 = tr.translate(transB2, dest= "fr" ).text
elif option2 == "ガリシア語":
    option2 = "gl"
    transC1 = tr.translate(transB2, dest= "gl" ).text
elif option2 == "グルジア語":
    option2 = "ka"
    transC1 = tr.translate(transB2, dest= "ka" ).text
elif option2 == "ドイツ語":
    option2 = "de"
    transC1 = tr.translate(transB2, dest= "de" ).text
elif option2 == "ギリシャ語":
    option2 = "el"
    transC1 = tr.translate(transB2, dest= "el").text
elif option2 == "グジャラート語":
    option2 = "gu"
    transC1 = tr.translate(transB2, dest= "gu" ).text
elif option2 == "ハイチ語":
    option2 = "ht"
    transC1 = tr.translate(transB2, dest= "ht" ).text
elif option2 == "ヘブライ語":
    option2 = "iw"
    transC1 = tr.translate(transB2, dest= "iw" ).text
elif option2 == "ヒンディー語":
    option2 = "hi"
    transC1 = tr.translate(transB2, dest= "hi" ).text
elif option2 == "ハンガリー語":
    option2 = "hu"
    transC1 = tr.translate(transB2, dest= "hu" ).text
elif option2 == "アイスランド語":
    option2 = "is"
    transC1 = tr.translate(transB2, dest= "is" ).text
elif option2 == "インドネシア語":
    option2 = "id"
    transC1 = tr.translate(transB2, dest= "id" ).text
elif option2 == "アイルランド語":
    option2 = "ga"
    transC1 = tr.translate(transB2, dest= "ga" ).text
elif option2 == "イタリア語":
    option2 = "it"
    transC1 = tr.translate(transB2, dest= "it" ).text
elif option2 == "カンナダ語":
    option2 = "kn"
    transC1 = tr.translate(transB2, dest= "kn" ).text
elif option2 == "韓国語":
    option2 = "ko"
    transC1 = tr.translate(transB2, dest= "ko" ).text
elif option2 == "ラテン語":
    option2 = "la"
    transC1 = tr.translate(transB2, dest= "la" ).text
elif option2 == "ラトビア語":
    option2 = "lv"
    transC1 = tr.translate(transB2, dest= "lv" ).text
elif option2 == "リトアニア語":
    option2 = "lt"
    transC1 = tr.translate(transB2, dest= "lt" ).text
elif option2 == "マケドニア語":
    option2 = "mk"
    transC1 = tr.translate(transB2, dest= "mk" ).text
elif option2 == "マレー語":
    option2 = "ms"
    transC1 = tr.translate(transB2, dest= "ms" ).text
elif option2 == "マルタ語":
    option2 = "mt"
    transC1 = tr.translate(transB2, dest= "mt" ).text
elif option2 == "ノルウェー語":
    option2 = "no"
    transC1 = tr.translate(transB2, dest= "no" ).text
elif option2 == "ペルシア語":
    option2 = "fa"
    transC1 = tr.translate(transB2, dest= "fa" ).text
elif option2 == "ポーランド語":
    option2 = "pl"
    transC1 = tr.translate(transB2, dest= "pl" ).text
elif option2 == "ポルトガル語":
    option2 = "pt"
    transC1 = tr.translate(transB2, dest= "pt" ).text
elif option2 == "ルーマニア語":
    option2 = "ro"
    transC1 = tr.translate(transB2, dest= "ro" ).text
elif option2 == "ロシア語":
    option2 = "ru"
    transC1 = tr.translate(transB2, dest= "ru" ).text
elif option2 == "セルビア語":
    option2 = "sr"
    transC1 = tr.translate(transB2, dest= "sr" ).text
elif option2 == "スロバキア語":
    option2 = "sk"
    transC1 = tr.translate(transB2, dest= "sk" ).text
elif option2 == "スロベニア語":
    option2 = "sl"
    transC1 = tr.translate(transB2, dest= "sl" ).text
elif option2 == "スペイン語":
    option2 = "es"
    transC1 = tr.translate(transB2, dest= "es" ).text
elif option2 == "スワヒリ語":
    option2 = "sw"
    transC1 = tr.translate(transB2, dest= "sw" ).text
elif option2 == "スウェーデン語":
    option2 = "sv"
    transC1 = tr.translate(transB2, dest= "sv" ).text
elif option2 == "タミル語":
    option2 = "ta"
    transC1 = tr.translate(transB2, dest= "ta" ).text
elif option2 == "テルグ語":
    option2 = "te"
    transC1 = tr.translate(transB2, dest= "te" ).text
elif option2 == "タイ語":
    option2 = "th"
    transC1 = tr.translate(transB2, dest= "th" ).text
elif option2 == "トルコ語":
    option2 = "tr"
    transC1 = tr.translate(transB2, dest= "tr" ).text
elif option2 == "ウクライナ語":
    option2 = "uk"
    transC1 = tr.translate(transB2, dest= "uk" ).text
elif option2 == "ウルドゥー語":
    option2 = "ur"
    transC1 = tr.translate(transB2, dest= "ur" ).text
elif option2 == "ベトナム語":
    option2 = "vi"
    transC1 = tr.translate(transB2, dest= "vi" ).text
elif option2 == "ウェールズ語":
    option2 = "cy"
    transC1 = tr.translate(transB2, dest= "cy" ).text
elif option2 == "イディッシュ語":
    option2 = "yi"
    transC1 = tr.translate(transB2, dest= "yi" ).text
else:
    option2 = "en"
    transC1 = tr.translate(transB2, dest= "en" ).text


transC2 = tr.translate(transC1, dest="ja").text

"翻訳された文：", transC2



option3 = st.selectbox (
    "使用したい言語(4回目)",
    list(language)
)




if option3 == "アフリカーンス言語":
    option3 = "af"
    transD1 = tr.translate(transC2, dest= "af" ).text
elif option3 == "アルバニア語":
    option3 = "sq"
    transD1 = tr.translate(transC2, dest= "sq" ).text
elif option3 == "アラビア語":
    option3 = "ar"
    transD1 = tr.translate(transC2, dest= "ar" ).text
elif option3 == "アゼルバイジャン語":
    option3 = "az"
    transD1 = tr.translate(transC2, dest= "az" ).text
elif option3 == "バスク語":
    option3 = "eu"
    transD1 = tr.translate(transC2, dest= "eu" ).text
elif option3 == "ベンガル語":
    option3 = "bn"
    transD1 = tr.translate(transC2, dest= "eu" ).text
elif option3 == "ベラルーシ語":
    option3 = "be"
    transD1 = tr.translate(transC2, dest= "be" ).text
elif option3 == "ブルガリア語":
    option3 = "bg"
    transD1 = tr.translate(transC2, dest= "bg" ).text
elif option3 == "カタルーニャ語":
    option3 = "ca"
    transD1 = tr.translate(transC2, dest= "ca" ).text
elif option3 == "簡体字":
    option3 = "zh-CN"
    transD1 = tr.translate(transC2, dest= "zh-CN" ).text
elif option3 == "繁体字":
    option3 = "zh-TW"
    transD1 = tr.translate(transC2, dest= "zh-TW" ).text
elif option3 == "クロアチア語":
    option3 = "hr"
    transD1 = tr.translate(transC2, dest= "hr" ).text
elif option3 == "チェコ語":
    option3 = "cs"
    transD1 = tr.translate(transC2, dest= "cs" ).text
elif option3 == "デンマーク語":
    option3 = "da"
    transD1 = tr.translate(transC2, dest= "da" ).text
elif option3 == "オランダ語":
    option3 = "nl"
    transD1 = tr.translate(transC2, dest= "nl" ).text
elif option3 == "英語":
    option3 = "en"
    transD1 = tr.translate(transC2, dest= "en" ).text
elif option3 == "エスペラント語":
    option3 = "et"
    transD1 = tr.translate(transC2, dest= "et" ).text
elif option3 == "エストニア語":
    option3 = "eo"
    transD1 = tr.translate(transC2, dest= "eo" ).text
elif option3 == "フィリピン語":
    option3 = "tl"
    transD1 = tr.translate(transC2, dest= "tl" ).text
elif option3 == "フィンランド語":
    option3 = "fi"
    transD1 = tr.translate(transC2, dest= "fi" ).text
elif option3 == "フランス語":
    option3 = "fr"
    transD1 = tr.translate(transC2, dest= "fr" ).text
elif option3 == "ガリシア語":
    option3 = "gl"
    transD1 = tr.translate(transC2, dest= "gl" ).text
elif option3 == "グルジア語":
    option3 = "ka"
    transD1 = tr.translate(transC2, dest= "ka" ).text
elif option3 == "ドイツ語":
    option3 = "de"
    transD1 = tr.translate(transC2, dest= "de" ).text
elif option3 == "ギリシャ語":
    option3 = "el"
    transD1 = tr.translate(transC2, dest= "el").text
elif option3 == "グジャラート語":
    option3 = "gu"
    transD1 = tr.translate(transC2, dest= "gu" ).text
elif option3 == "ハイチ語":
    option3 = "ht"
    transD1 = tr.translate(transC2, dest= "ht" ).text
elif option3 == "ヘブライ語":
    option3 = "iw"
    transD1 = tr.translate(transC2, dest= "iw" ).text
elif option3 == "ヒンディー語":
    option3 = "hi"
    transD1 = tr.translate(transC2, dest= "hi" ).text
elif option3 == "ハンガリー語":
    option3 = "hu"
    transD1 = tr.translate(transC2, dest= "hu" ).text
elif option3 == "アイスランド語":
    option3 = "is"
    transD1 = tr.translate(transC2, dest= "is" ).text
elif option3 == "インドネシア語":
    option3 = "id"
    transD1 = tr.translate(transC2, dest= "id" ).text
elif option3 == "アイルランド語":
    option3 = "ga"
    transD1 = tr.translate(transC2, dest= "ga" ).text
elif option3 == "イタリア語":
    option3 = "it"
    transD1 = tr.translate(transC2, dest= "it" ).text
elif option3 == "カンナダ語":
    option3 = "kn"
    transD1 = tr.translate(transC2, dest= "kn" ).text
elif option3 == "韓国語":
    option3 = "ko"
    transD1 = tr.translate(transC2, dest= "ko" ).text
elif option3 == "ラテン語":
    option3 = "la"
    transD1 = tr.translate(transC2, dest= "la" ).text
elif option3 == "ラトビア語":
    option3 = "lv"
    transD1 = tr.translate(transC2, dest= "lv" ).text
elif option3 == "リトアニア語":
    option3 = "lt"
    transD1 = tr.translate(transC2, dest= "lt" ).text
elif option3 == "マケドニア語":
    option3 = "mk"
    transD1 = tr.translate(transC2, dest= "mk" ).text
elif option3 == "マレー語":
    option3 = "ms"
    transD1 = tr.translate(transC2, dest= "ms" ).text
elif option3 == "マルタ語":
    option3 = "mt"
    transD1 = tr.translate(transC2, dest= "mt" ).text
elif option3 == "ノルウェー語":
    option3 = "no"
    transD1 = tr.translate(transC2, dest= "no" ).text
elif option3 == "ペルシア語":
    option3 = "fa"
    transD1 = tr.translate(transC2, dest= "fa" ).text
elif option3 == "ポーランド語":
    option3 = "pl"
    transD1 = tr.translate(transC2, dest= "pl" ).text
elif option3 == "ポルトガル語":
    option3 = "pt"
    transD1 = tr.translate(transC2, dest= "pt" ).text
elif option3 == "ルーマニア語":
    option3 = "ro"
    transD1 = tr.translate(transC2, dest= "ro" ).text
elif option3 == "ロシア語":
    option3 = "ru"
    transD1 = tr.translate(transC2, dest= "ru" ).text
elif option3 == "セルビア語":
    option3 = "sr"
    transD1 = tr.translate(transC2, dest= "sr" ).text
elif option3 == "スロバキア語":
    option3 = "sk"
    transD1 = tr.translate(transC2, dest= "sk" ).text
elif option3 == "スロベニア語":
    option3 = "sl"
    transD1 = tr.translate(transC2, dest= "sl" ).text
elif option3 == "スペイン語":
    option3 = "es"
    transD1 = tr.translate(transC2, dest= "es" ).text
elif option3 == "スワヒリ語":
    option3 = "sw"
    transD1 = tr.translate(transC2, dest= "sw" ).text
elif option3 == "スウェーデン語":
    option3 = "sv"
    transD1 = tr.translate(transC2, dest= "sv" ).text
elif option3 == "タミル語":
    option3 = "ta"
    transD1 = tr.translate(transC2, dest= "ta" ).text
elif option3 == "テルグ語":
    option3 = "te"
    transD1 = tr.translate(transC2, dest= "te" ).text
elif option3 == "タイ語":
    option3 = "th"
    transD1 = tr.translate(transC2, dest= "th" ).text
elif option3 == "トルコ語":
    option3 = "tr"
    transD1 = tr.translate(transC2, dest= "tr" ).text
elif option3 == "ウクライナ語":
    option3 = "uk"
    transD1 = tr.translate(transC2, dest= "uk" ).text
elif option3 == "ウルドゥー語":
    option3 = "ur"
    transD1 = tr.translate(transC2, dest= "ur" ).text
elif option3 == "ベトナム語":
    option3 = "vi"
    transD1 = tr.translate(transC2, dest= "vi" ).text
elif option3 == "ウェールズ語":
    option3 = "cy"
    transD1 = tr.translate(transC2, dest= "cy" ).text
elif option3 == "イディッシュ語":
    option3 = "yi"
    transD1 = tr.translate(transC2, dest= "yi" ).text
else:
    option3 = "en"
    transD1 = tr.translate(transC2, dest= "en" ).text


transD2 = tr.translate(transD1, dest="ja").text

"翻訳された文：", transD2



option4 = st.selectbox (
    "使用したい言語(5回目)",
    list(language)
)




if option4 == "アフリカーンス言語":
    option4 = "af"
    transE1 = tr.translate(transD2, dest= "af" ).text
elif option4 == "アルバニア語":
    option4 = "sq"
    transE1 = tr.translate(transD2, dest= "sq" ).text
elif option4 == "アラビア語":
    option4 = "ar"
    transE1 = tr.translate(transD2, dest= "ar" ).text
elif option4 == "アゼルバイジャン語":
    option4 = "az"
    transE1 = tr.translate(transD2, dest= "az" ).text
elif option4 == "バスク語":
    option4 = "eu"
    transE1 = tr.translate(transD2, dest= "eu" ).text
elif option4 == "ベンガル語":
    option4 = "bn"
    transE1 = tr.translate(transD2, dest= "eu" ).text
elif option4 == "ベラルーシ語":
    option4 = "be"
    transE1 = tr.translate(transD2, dest= "be" ).text
elif option4 == "ブルガリア語":
    option4 = "bg"
    transE1 = tr.translate(transD2, dest= "bg" ).text
elif option4 == "カタルーニャ語":
    option4 = "ca"
    transE1 = tr.translate(transD2, dest= "ca" ).text
elif option4 == "簡体字":
    option4 = "zh-CN"
    transE1 = tr.translate(transD2, dest= "zh-CN" ).text
elif option4 == "繁体字":
    option4 = "zh-TW"
    transE1 = tr.translate(transD2, dest= "zh-TW" ).text
elif option4 == "クロアチア語":
    option4 = "hr"
    transE1 = tr.translate(transD2, dest= "hr" ).text
elif option4 == "チェコ語":
    option4 = "cs"
    transE1 = tr.translate(transD2, dest= "cs" ).text
elif option4 == "デンマーク語":
    option4 = "da"
    transE1 = tr.translate(transD2, dest= "da" ).text
elif option4 == "オランダ語":
    option4 = "nl"
    transE1 = tr.translate(transD2, dest= "nl" ).text
elif option4 == "英語":
    option4 = "en"
    transE1 = tr.translate(transD2, dest= "en" ).text
elif option4 == "エスペラント語":
    option4 = "et"
    transE1 = tr.translate(transD2, dest= "et" ).text
elif option4 == "エストニア語":
    option4 = "eo"
    transE1 = tr.translate(transD2, dest= "eo" ).text
elif option4 == "フィリピン語":
    option4 = "tl"
    transE1 = tr.translate(transD2, dest= "tl" ).text
elif option4 == "フィンランド語":
    option4 = "fi"
    transE1 = tr.translate(transD2, dest= "fi" ).text
elif option4 == "フランス語":
    option4 = "fr"
    transE1 = tr.translate(transD2, dest= "fr" ).text
elif option4 == "ガリシア語":
    option4 = "gl"
    transE1 = tr.translate(transD2, dest= "gl" ).text
elif option4 == "グルジア語":
    option4 = "ka"
    transE1 = tr.translate(transD2, dest= "ka" ).text
elif option4 == "ドイツ語":
    option4 = "de"
    transE1 = tr.translate(transD2, dest= "de" ).text
elif option4 == "ギリシャ語":
    option4 = "el"
    transE1 = tr.translate(transD2, dest= "el").text
elif option4 == "グジャラート語":
    option4 = "gu"
    transE1 = tr.translate(transD2, dest= "gu" ).text
elif option4 == "ハイチ語":
    option4 = "ht"
    transE1 = tr.translate(transD2, dest= "ht" ).text
elif option4 == "ヘブライ語":
    option4 = "iw"
    transE1 = tr.translate(transD2, dest= "iw" ).text
elif option4 == "ヒンディー語":
    option4 = "hi"
    transE1 = tr.translate(transD2, dest= "hi" ).text
elif option4 == "ハンガリー語":
    option4 = "hu"
    transE1 = tr.translate(transD2, dest= "hu" ).text
elif option4 == "アイスランド語":
    option4 = "is"
    transE1 = tr.translate(transD2, dest= "is" ).text
elif option4 == "インドネシア語":
    option4 = "id"
    transE1 = tr.translate(transD2, dest= "id" ).text
elif option4 == "アイルランド語":
    option4 = "ga"
    transE1 = tr.translate(transD2, dest= "ga" ).text
elif option4 == "イタリア語":
    option4 = "it"
    transE1 = tr.translate(transD2, dest= "it" ).text
elif option4 == "カンナダ語":
    option4 = "kn"
    transE1 = tr.translate(transD2, dest= "kn" ).text
elif option4 == "韓国語":
    option4 = "ko"
    transE1 = tr.translate(transD2, dest= "ko" ).text
elif option4 == "ラテン語":
    option4 = "la"
    transE1 = tr.translate(transD2, dest= "la" ).text
elif option4 == "ラトビア語":
    option4 = "lv"
    transE1 = tr.translate(transD2, dest= "lv" ).text
elif option4 == "リトアニア語":
    option4 = "lt"
    transE1 = tr.translate(transD2, dest= "lt" ).text
elif option4 == "マケドニア語":
    option4 = "mk"
    transE1 = tr.translate(transD2, dest= "mk" ).text
elif option4 == "マレー語":
    option4 = "ms"
    transE1 = tr.translate(transD2, dest= "ms" ).text
elif option4 == "マルタ語":
    option4 = "mt"
    transE1 = tr.translate(transD2, dest= "mt" ).text
elif option4 == "ノルウェー語":
    option4 = "no"
    transE1 = tr.translate(transD2, dest= "no" ).text
elif option4 == "ペルシア語":
    option4 = "fa"
    transE1 = tr.translate(transD2, dest= "fa" ).text
elif option4 == "ポーランド語":
    option4 = "pl"
    transE1 = tr.translate(transD2, dest= "pl" ).text
elif option4 == "ポルトガル語":
    option4 = "pt"
    transE1 = tr.translate(transD2, dest= "pt" ).text
elif option4 == "ルーマニア語":
    option4 = "ro"
    transE1 = tr.translate(transD2, dest= "ro" ).text
elif option4 == "ロシア語":
    option4 = "ru"
    transE1 = tr.translate(transD2, dest= "ru" ).text
elif option4 == "セルビア語":
    option4 = "sr"
    transE1 = tr.translate(transD2, dest= "sr" ).text
elif option4 == "スロバキア語":
    option4 = "sk"
    transE1 = tr.translate(transD2, dest= "sk" ).text
elif option4 == "スロベニア語":
    option4 = "sl"
    transE1 = tr.translate(transD2, dest= "sl" ).text
elif option4 == "スペイン語":
    option4 = "es"
    transE1 = tr.translate(transD2, dest= "es" ).text
elif option4 == "スワヒリ語":
    option4 = "sw"
    transE1 = tr.translate(transD2, dest= "sw" ).text
elif option4 == "スウェーデン語":
    option4 = "sv"
    transE1 = tr.translate(transD2, dest= "sv" ).text
elif option4 == "タミル語":
    option4 = "ta"
    transE1 = tr.translate(transD2, dest= "ta" ).text
elif option4 == "テルグ語":
    option4 = "te"
    transE1 = tr.translate(transD2, dest= "te" ).text
elif option4 == "タイ語":
    option4 = "th"
    transE1 = tr.translate(transD2, dest= "th" ).text
elif option4 == "トルコ語":
    option4 = "tr"
    transE1 = tr.translate(transD2, dest= "tr" ).text
elif option4 == "ウクライナ語":
    option4 = "uk"
    transE1 = tr.translate(transD2, dest= "uk" ).text
elif option4 == "ウルドゥー語":
    option4 = "ur"
    transE1 = tr.translate(transD2, dest= "ur" ).text
elif option4 == "ベトナム語":
    option4 = "vi"
    transE1 = tr.translate(transD2, dest= "vi" ).text
elif option4 == "ウェールズ語":
    option4 = "cy"
    transE1 = tr.translate(transD2, dest= "cy" ).text
elif option4 == "イディッシュ語":
    option4 = "yi"
    transE1 = tr.translate(transD2, dest= "yi" ).text
else:
    option4 = "en"
    transE1 = tr.translate(transD2, dest= "en" ).text


transE2 = tr.translate(transE1, dest="ja").text

"翻訳された文：", transE2

"""
###
"""

"""
###
"""

"""
###
"""

##st.header("Twitterで共有する")


st.header("主のTwitter")
Twitter = '''
<a class="twitter-timeline" data-width="500" data-height="750" href="https://twitter.com/Tenmaru0101?ref_src=twsrc%5Etfw">Tweets by Tenmaru0101</a> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
'''

st.components.v1.html(Twitter, width=340, height=1000)
