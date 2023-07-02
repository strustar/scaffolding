# import openpyxl as ox
# import xlwings as xw
import streamlit as st 
import sidebar, tab0, tab1

### * -- Set page config
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# https://zzsza.github.io/mlops/2021/02/07/python-streamlit-dashboard/  유용한 사이트
st.set_page_config(page_title = "System support 구조검토", page_icon = "🌈", layout = "wide",    # centered, wide
                    initial_sidebar_state="expanded",
                    # runOnSave = True,
                    menu_items = {        #   initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
                        # 'Get Help': 'https://www.extremelycoolapp.com/help',
                        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
                        # 'About': "# This is a header. This is an *extremely* cool app!"
                    })
### * -- Set page config

# 줄바꿈 처리
st.markdown("""
    <style>
        .element-container {
            white-space: nowrap;
            overflow-x: visible;
        }
    </style>
    """, unsafe_allow_html=True)


# Adding custom style with font
fn1 = 'Nanum Gothic';  fn2 = 'Gungsuhche';  fn3 = 'Lora';  fn4 = 'Noto Sans KR'
font_style = """
    <style>
        /* CSS to set font for everything except code blocks */
        body, h1, h2, h3, h4, h5, h6, p, blockquote {font-family: 'Nanum Gothic', sans-serif !important;}
        /* CSS to set font for code blocks */
        .highlight pre, .highlight tt, pre, tt {font-family: 'Courier New', Courier, monospace;}

        /* Font size for titles (h1 to h6) */
        h1 {font-size: 32px;}
        h2 {font-size: 28px;}
        h3 {font-size: 24px;}
        h4 {font-size: 20px;}
        h5 {font-size: 16px;}
        h6 {font-size: 12px;}
        /* Font size for body text */
        body {font-size: 16px;}
    </style>
"""
st.markdown(font_style, unsafe_allow_html=True)

h2 = '## ';  h3 = '### ';  h4 = '#### ';  h5 = '##### ';  h6 = '###### '
s1 = h5+'$\quad$';  s2 = h5+'$\qquad$';  s3 = h5+'$\quad \qquad$'  #s12 = '$\enspace$'  공백 : \,\:\;  # ⁰¹²³⁴⁵⁶⁷⁸⁹  ₀₁₂₃₄₅₆₇₈₉

In = sidebar.Sidebar(h2, h4)
##### tab ===========================================================================================================
tab = st.tabs([ h4+':green[Ⅰ. 설계조건 📝✍️]', h4+':blue[Ⅱ. 단면제원 검토 💻⭕]', h4+':orange[Ⅲ. 시스템 서포터 검토 🏛️🏗️]', h4+':green[Ⅳ. 구조검토 결과 🎯✅ ]' ])
with tab[1]:
    [Wood, Joist, Yoke] = tab0.Tab(In, 'green', fn1, s1, s2, s3, h4, h5)    

with tab[0]:
    [Lj, Ly, Ls] = tab1.Tab(In, 'blue', fn1, s1, s2, s3, h4, h5, Wood, Joist, Yoke)
    st.write(h4, '5. 서포트 검토 (수직재)')
    st.write(s1, '1) 1본당 작용하중 (P)')
    st.write(s2, '➣ P = 설계 하중 x 멍에 간격 x 서포트 간격')
    # st.write(s2, '➣ $\pmb{{{}}}$ = {:.4f}'.format(w_str, t_load) + ' N/mm² x '+str(round(L))+' mm = {:.4f}'.format(w) + ' N/mm')





# # import re
# # pattern = r"\d+\.?\d*" #정수 : r'\d+'
# # jj = re.findall(pattern, jw)
# import streamlit as st

# # 변수 설정
# red_variable = r"\textcolor{blue}{L_k}"
# Ljm = 10  # 값을 대신 입력하세요.

# # 포맷을 사용하여 문자열에 변수 삽입
# formatted_string = r"$\bm{{\quad\textcolor{{red}}{{{}}}\leq \Large\sqrt{{\frac{{8\,f_{{ba}}\,S}}{{ω}}}} \normalsize = \:}} $".format(red_variable) + '{:.1f}'.format(Ljm) + ' mm'

# st.write(s3, r"$\bm{{\quad\textcolor{{red}}{{{}}}\leq \Large\sqrt{{\frac{{8\,f_{{ba}}\,S}}{{ω}}}} \normalsize = \:}} $".format(red_variable) + '{:.1f}'.format(Ljm) + ' mm')

# name = "Alice"
# age = 25
# string = f"My name is {name} and I'm {age} years old."
# string
# string = "He said, \"Hello, World!\""
# string

