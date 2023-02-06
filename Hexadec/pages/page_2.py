import streamlit as st

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')
    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    # セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子供', '大人')
    )
    # ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子供', '大人')
    )
    # 複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'ドライブ', '料理', '旅行', '投資', 'プログラム', 'ブログ')
    )
    # チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')
    # スライダー
    height = st.slider('身長', min_value=110, max_value=210)
  
    # カラーびっかー
    color = st.color_picker('テーマカラー', '#00f900')

    if submit_btn:
        st.text(f'ようこそ！{name}さん！！{address}に書籍を送りました')
        st.text(f'年齢層：{age_category}')
        st.text(f'趣味：{",".join(hobby)}')