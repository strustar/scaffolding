import streamlit as st 
import plotly.graph_objects as go
import pandas as pd
# import numpy as np

def Load(fn, s_t, s_weight, w_weight):
    headers = [
        "<b>구분",
        "<b>하중 [N/mm²]",
        "<b>하중 [kN/m²]",
        "<b>하중 산정 [KDS 21 50 00 :2022]",
    ]
    w_load = w_weight;  s_load = s_weight*s_t/1e3;  live_load = 2.5   # kN/m²
    if s_t/1e3 >= 0.5: live_load = 3.5
    if s_t/1e3 >= 1.0: live_load = 5.0
    t_load = s_load + w_load + live_load

    data = [
    ['<b>콘크리트 자중', '<b>{:.4f}'.format(s_load/1e3), '<b>{:.2f}'.format(s_load), '<b>{:.1f}'.format(s_weight) + 'kN/m³ × ' + '{:.3f}'.format(s_t/1e3) + 'm = {:.2f}'.format(s_load) + 'kN/m²'],
    ['<b>거푸집 자중', '<b>{:.4f}'.format(w_load/1e3), '<b>{:.2f}'.format(w_load), '<b>최소 0.4kN/m² (1.6.2 연직하중)'],
    ['<b>작업하중 (활하중)', '<b>{:.4f}'.format(live_load/1e3), '<b>{:.2f}'.format(live_load), '<b>*최소 2.5kN/m² (1.6.2 연직하중)'],
    ['<b>∑ (합계)', '<b>{:.4f}'.format(t_load/1e3), '<b>{:.2f}'.format(t_load), '<b>최소 5.0kN/m² (1.6.2 연직하중)'],
    ]

    data_dict = {header: values for header, values in zip(headers, zip(*data))}  # 행이 여러개(2개 이상) 일때
    df = pd.DataFrame(data_dict)

    fs = 16;  lw = 2
    fig = go.Figure(data=[go.Table(
        # columnorder=[1,2,3],
        columnwidth=[2, 1., 1., 3],
        header=dict(
            values=list(df.columns),
            align=['center'],
            height=10,
            font=dict(size=fs, color='black', family=fn),  # 글꼴 변경
            fill_color=['silver'],  #'darkgray'
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            align=['center'],
            # align=['center', 'center', 'right', 'left'],
            height=25,
            prefix=None,
            suffix=None,
            font=dict(size=fs, color='black', family=fn),  # 글꼴 변경
            fill=dict(color=['silver', 'white']),  # 셀 배경색 변경
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
            format=[None, None]  # '나이' 열의 데이터를 실수 형태로 변환하여 출력  '.2f'
        ),
    )],
    )    
    fig.update_layout(width=1000, height=190, margin=dict(l=40, r=0, t=1, b=0))  # 테이블 여백 제거  # 표의 크기 지정
    st.plotly_chart(fig)
    return t_load


def Info(fn, shape, section, A, I, S, E, fba, fsa):
    headers = [
        "<b>재료<br>형상",
        "<b>두께 / 하중방향<br>      [mm / °]",
        "<b> 단면적<br>A [mm²]",
        "<b>단면2차모멘트<br>    I [mm⁴]",
        "<b>단면계수<br>S [mm³]",
        "<b>탄성계수<br> E [GPa]",
        "<b>허용휨응력<br>  <i>f<sub>ba</sub></i> [MPa]",
        "<b>허용전단응력<br>   <i>f<sub>sa</sub></i> [MPa]",
        ]
    if '합판' not in shape:
        headers[1] = "<b> 단면<br>[mm]"
    data = [
        '<b>'+shape,
        '<b>'+section,
        '<b>'+str(round(A,1)),
        '<b>'+str(round(I,1)),
        '<b>'+str(round(S,1)),
        '<b>'+str(round(E/1e3)),
        '<b>'+'<b>'+"{:.1f}".format(fba),
        '<b>'+"{:.2f}".format(fsa),
        ]
    if '합판' not in shape:
        data[3] = '<b>'+str(round(I/1e3,1))+'×10³'
        data[4] = '<b>'+str(round(S/1e3,1))+'×10³'
        data[7] = '<b>'+"{:.1f}".format(fsa)
    data_dict = {header: [value] for header, value in zip(headers, data)}  # 행이 한개 일때    
    df = pd.DataFrame(data_dict)

    fs = 16;  lw = 2
    fig = go.Figure(data=[go.Table(
        # columnorder=[1,2,3],
        # columnwidth=[1, 1, 1, 1, 1.3, 1, 1, 1.3],
        header=dict(
            values=list(df.columns),
            align=['center'],
            height=10,
            font=dict(size=fs, color='black', family=fn),  # 글꼴 변경
            fill_color=['silver'],  #'darkgray'
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            align=['center']*1,
            height=25,
            prefix=None,
            suffix=None,
            font=dict(size=fs, color='black', family=fn),  # 글꼴 변경
            fill=dict(color=['silver', 'white']),  # 셀 배경색 변경
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
            format=[None, None]  # '나이' 열의 데이터를 실수 형태로 변환하여 출력  '.2f'
        ),
    )],
    )    
    fig.update_layout(width=1000, height=100, margin=dict(l=40, r=0, t=1, b=0))  # 테이블 여백 제거  # 표의 크기 지정
    st.plotly_chart(fig)

def Interval(fn, d, d1, d2):
    headers = [
        "<b>휨응력 검토",
        "<b>상대변형 검토",
        "<b>절대변형 검토",
        ]
    data = [
        '<b>'+"{:.1f}".format(d)+' mm',
        '<b>'+"{:.1f}".format(d1)+' mm',
        '<b>'+"{:.1f}".format(d2)+' mm',
        ]
    data_dict = {header: [value] for header, value in zip(headers, data)}  # 행이 한개 일때    
    df = pd.DataFrame(data_dict)

    color = ['black','black','black']
    n = [d, d1, d2];  min_index = n.index(min(n));  color[min_index] = 'blue'
    fs = 16;  lw = 2
    fig = go.Figure(data=[go.Table(
        # columnorder=[1,2,3],
        # columnwidth=[1, 1, 1, 1, 1.3, 1, 1, 1.3],
        header=dict(
            values=list(df.columns),
            align=['center'],
            height=10,
            font=dict(size=fs, color=color, family=fn),  # 글꼴 변경
            fill_color=['silver'],  #'darkgray'
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
        ),
        cells=dict(
            values=[df[col] for col in df.columns],
            align=['center']*1,
            height=25,
            prefix=None,
            suffix=None,
            font=dict(size=fs, color=color, family=fn),  # 글꼴 변경
            fill=dict(color=['white']),  # 셀 배경색 변경
            line=dict(color='black', width=lw),   # 셀 경계색, 두께
            format=[None, None]  # '나이' 열의 데이터를 실수 형태로 변환하여 출력  '.2f'
        ),
    )],
    )    
    fig.update_layout(width=600, height=80, margin=dict(l=60, r=0, t=1, b=0))  # 테이블 여백 제거  # 표의 크기 지정
    st.plotly_chart(fig)

