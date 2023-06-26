# import openpyxl as ox
# import xlwings as xw
import os
import streamlit as st 
import plotly.graph_objects as go
import pandas as pd
import numpy as np

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

# Adding custom style with font
f1 = 'Nanum Gothic';  f2 = 'Gungsuhche';  f3 = 'Lora';  f4 = 'Noto Sans KR'
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
border = '<hr style="border-top: 5px double green; margin-top:0px; margin-bottom:30px; border-radius: 10px">'
border1= '<hr style="border-top: 1px solid green; margin-top:30px; margin-bottom:30px; border-radius: 10px">'
h2 = '## ';  h3 = '### ';  h4 = '#### ';  h5 = '##### ';  h6 = '###### '
s1 = h5+'$\quad$';  s2 = h5+'$\qquad$';  s3 = h5+'$\quad \qquad$'  #s12 = '$\enspace$'

##### sidebar =======================================================================================================
st.sidebar.write(h2, ':blue[거푸집용 합판]')
[col1, col2] = st.sidebar.columns([1,1], gap = "small")
with col1:
    wt = st.radio(h4+':green[합판 두께 [mm]]', (12, 15, 18), horizontal=True)
with col2:
    wangle = st.radio(h4+':green[하중 방향 [각도]]', (0, 90), horizontal=True)

st.sidebar.write(h2, ':blue[장선]')
js = st.sidebar.radio(h4+':green[장선 종류]', ('목재', '각형강관', '원형강관'), horizontal=True)
[col1, col2, col3] = st.sidebar.columns(3)
with col1:
    if '목재' in js:
        jw = st.number_input(h4+':green[폭 [mm]]', min_value = 10., value = 30., step = 5., format = '%f')
    if '각형' in js:
        jw = st.number_input(h4+':green[폭 [mm]]', min_value = 10., value = 50., step = 5., format = '%f')
with col2:
    if '목재' in js:
        jh = st.number_input(h4+':green[높이 [mm]]', min_value = 10., value = 50., step = 5., format = '%f')
    if '각형' in js:
        jh = st.number_input(h4+':green[높이 [mm]]', min_value = 10., value = 50., step = 5., format = '%f')
    if '원형' in js:
        jd = st.number_input(h4+':green[직경 [mm]]', min_value = 10., value = 42.7, step = 5., format = '%f')
with col3:
    if '각형' in js:
        jt = st.number_input(h4+':green[두께 [mm]]', min_value = 1., value = 2.3, step = 0.1)
    if '원형' in js:
        jt = st.number_input(h4+':green[두께 [mm]]', min_value = 1., value = 2.2, step = 0.1)
##### sidebar =======================================================================================================


##### tab ===========================================================================================================
tab = st.tabs(['📄 📝🏠 :blue[설계조건]', '⭕ 🧮 :red[22] 단면제원 검토','ℹ️ 📊 :green[시스템 서포터 검토]', '📘 ✅ 구조검토 결과'])
with tab[0]:
    st.markdown(border, unsafe_allow_html=True)
    st.write(h4, '1. 적용기준')
    st.write(s1, '1) 거푸집 및 동바리 설계기준 (국토교통부, :blue[KDS 21 50 00 : 2022])')
    # st.write('_ㅇㅇ_ **1. $\sqrt{x^2}$ 적용기준**')
    st.write(s1, '2) 거푸집 및 동바리 안전작업지침 등 (한국산업안전보건공단)')
    st.write(s1, '3) 콘크리트 표준시방서 (한국콘크리트학회, 2016)')        
    
    st.markdown(border1, unsafe_allow_html=True)
    st.write(h4, '2. 설계하중')  # \enspace : 1/2 em space, \quad : 1 em space, \qquad : 2 em space
    st.write(h5, ':orange[<근거 : 1.6 설계하중 (KDS 21 50 00 :2022)>]')
    st.write(s1, '1) 연직하중 (고정하중 + 작업하중)')

    st.write(s2, '① 고정하중')
    st.write(s3, '➣ 보통 콘크리트 자중 : :blue[24kN/㎥ 이상] 적용')    
    st.write(s3, '➣ 거푸집 자중 : :blue[0.4kN/㎡ 이상] 적용')

    st.write(s2, '② 작업하중 (작업원, 경량의 장비하중, 충격하중, 기타 콘크리트 타설에 필요한 자재 및 공구 등)')
    # st.write(s3, '➣ :blue[2.5kN/㎡ 이상] 적용, 전동식 카트장비 사용시 :blue[3.8kN/㎡ 이상] 적용')  # 바뀐 설계기준에는 없음??
    st.write(s3, '➣ 콘크리트 타설 높이가 0.5m 미만인 경우 :blue[2.5kN/㎡], 0.5m 이상 1m 미만인 경우 :blue[3.5kN/㎡], 1m 이상인 경우 :blue[5kN/㎡ 이상] 적용')

    st.write(s2, '③ 최소 연직하중')
    st.write(s3, '➣ 콘크리트 타설 높이와 관계없이 최소 :blue[5kN/㎡ 이상] 적용, ??바뀐 설계기준에는 없음?? 전동식카트 사용시 최소 :blue[6.3kN/㎡ 이상] 적용')

    st.write(s1, '2) 수평하중 **[:blue[아래 두값 중 큰 값 적용]]**')
    st.write(s2, '① 동바리 상단에 고정하중의 :blue[2% 이상]')
    st.write(s2, '② 동바리 상단에 수평방향으로 단위길이당 :blue[1.5kN/m 이상]')
    
    st.markdown(border1, unsafe_allow_html=True)
    st.write(h4, '3. 사용재료')
    st.write(h5, ':orange[<근거 : 2.2 거푸집 널 & 2.3 장선 및 멍에 (KDS 21 50 00 :2022)>]')
    st.write(s1, '1) 거푸집 널')

    st.write(s1, '2) 장선')

# import re
# pattern = r"\d+\.?\d*" #정수 : r'\d+'
# jj = re.findall(pattern, jw)
if '목재' in js:
    joist = [js, str(round(jw))+'Ⅹ'+str(round(jh)), jw*jh]

joist

df = pd.DataFrame({
    "<br><b>형상": ['<b>'+joist[0]],
    "<br><b>단면": '<b>'+joist[1],
    "<b> 단면적<br>A [mm²]": '<b>'+str(joist[2]),
    "<b>단면계수<br>S [mm³]": '<b>'+str(11),
    "<b>단면2차모멘트<br>    I [mm⁴]": '<b>',
    "<b>탄성계수<br> E [MPa]": '<b>',
    "<b>허용휨응력<br>  <i>f<sub>b</sub></i> [MPa]": '<b>',
    "<b>허용전단응력<br>   <i>f<sub>s</sub></i> [MPa]": '<b>',
})

fig = go.Figure(data=[go.Table(
    # columnorder=[1,2,3],
    # columnwidth=[1, 1, 1],    
    header=dict(
        values=list(df.columns),
        align=['center'],
        height=10,
        font=dict(size=16, color='black', family=f1),  # 글꼴 변경
        fill_color=['silver'],  #'darkgray'
        line=dict(color='black', width=[1]),   # 셀 경계색, 두께
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        align=['center']*1,
        height=25,
        prefix=None,
        suffix=None,
        font=dict(size=16, color='black', family=f1),  # 글꼴 변경
        fill=dict(color=['white', 'white']),  # 셀 배경색 변경
        line=dict(color='black', width=[1]),   # 셀 경계색, 두께
        format=[None, None]  # '나이' 열의 데이터를 실수 형태로 변환하여 출력  '.2f'
    ),
)],
)

fig.update_layout(width=800, height=400, margin=dict(l=40, r=0, t=0, b=0), showlegend=True)  # 테이블 여백 제거  # 표의 크기 지정
st.plotly_chart(fig)


import plotly.graph_objects as go

header_values = ["이름", "매출액 (원)"]
cell_data = [
    ["철수", 43500000],
    ["영희", 2300000],
    ["영호", 6000000]
]

# 천 단위 콤마 처리
formatted_data = [
    [cell_data[i][0], format(cell_data[i][1], ',')] for i in range(len(cell_data))
]

fig = go.Figure(data=[go.Table(
    header=dict(values=header_values,
                font=dict(size=16),
                align='center'),
    cells=dict(values=list(map(list, zip(*formatted_data))),
                font=dict(size=14),
                align='center'))
])
st.plotly_chart(fig)


