import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة
st.set_page_config(page_title="سباق شركات الاتصالات", layout="wide")

# قراءة ملف الـ HTML الخارجي بأمان تام
try:
    with open("game.html", "r", encoding="utf-8") as f:
        game_html = f.read()
    # عرض اللعبة
    components.html(game_html, height=750, scrolling=True)
except FileNotFoundError:
    st.error("⚠️ ملف game.html غير موجود! تأكد من وجوده في نفس المجلد مع app.py.")