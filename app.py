import datetime

import matplotlib.pyplot as plt
import pandas as pd
import  seaborn as sns
import streamlit as st
from PIL import Image
#ImageのIは大文字

# df = sns.load_dataset('iris')
# df.info()
# df.head(5)

st.title('Hexadec')
st.caption('Streamlitで作成した動画用のテストアプリです')

col1, col2 = st.columns(2)

with col1:
    st.subheader('自己紹介')
    st.text('今後便利ソフトをアップロードする予定です')
    code = '''
        import streamlit as st
        st.title('Hexadec')
    '''
    st.code(code, language='python')
    #画像
    image = Image.open('images.png')
    st.image(image, width=200)
    #動画
    # video_file = open('movie.mov', 'rb')
    # video_byte= video_file.read()
    # st.video(video_byte)

    with st.form(key='profile_form'):
        # テキストボックス
        name = st.text_input('名前')
        address = st.text_input('住所')
        # ボタン
        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')

        #セレクトボックス
        age_category = st.selectbox(
            '年齢層',
            ('子供','大人')
        )
        # ラジオボタン
        age_category = st.radio(
            '年齢層',
            ('子供', '大人')
        )
        #複数選択
        hobby = st.multiselect(
            '趣味',
            ('スポーツ','読書','ドライブ','料理','旅行','投資','プログラム','ブログ')
        )
        #チェックボックス
        mail_subscribe = st.checkbox('メールマガジンを購読する')
        #スライダー
        height = st.slider('身長',min_value=110,max_value=210)
        #日付
        start_date = st.date_input(
            '開始日',
            datetime.date(2023, 2, 5)
        )
        #カラーびっかー
        color = st.color_picker('テーマカラー','#00f900')

        if submit_btn:
            st.text(f'ようこそ！{name}さん！！{address}に書籍を送りました')
            st.text(f'年齢層：{age_category}')
            st.text(f'趣味：{",".join(hobby)}')

#ボタン
    # submit_btn = st.button('送信')
    # cancel_btn = st.button('キャンセル')
# print(f'submit_btn:{submit_btn}')
# print(f'cancel_btn:{cancel_btn}')

with col2:
    # データ分析関係
    df = pd.read_csv('testdata.csv', index_col='月')
    st.dataframe(df)
    # st.table(df)
    st.line_chart(df)
    st.bar_chart(df['2021年'])

    # matplotlib
    fig, ax = plt.subplots()
    ax.plot(df.index, df['2021年'])
    ax.set_title('matplotlib graph')
    st.pyplot(fig)


