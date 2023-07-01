import streamlit as st
import numpy as np
import table

def Tab(In, color, fn, s1, s2, s3, h4, h5, Wood, Joist, Yoke):
    border1 = '<hr style="border-top: 5px double ' + color + '; margin-top: 0px; margin-bottom:30px; border-radius: 10px">'
    border2 = '<hr style="border-top: 1px solid '  + color + '; margin-top:30px; margin-bottom:30px; border-radius: 10px">'
    [s_h, s_t, s_weight, w_weight, w_s, w_t, w_angle, level, d1, d2, Ln] = [In.s_h, In.s_t, In.s_weight, In.w_weight, In.w_s, In.w_t, In.w_angle, In.level, In.d1, In.d2, In.Ln]
    # [j_s, j_b, j_h, j_d, j_t] = [In.j_s, In.j_b, In.j_h, In.j_d, In.j_t]

    st.markdown(border1, unsafe_allow_html=True)
    st.write(h4, '1. 설계하중 산정')
    st.write(s1, '1) 연직하중 (고정하중 + 작업하중)')
    t_load = table.Load(fn, s_t, s_weight, w_weight)
    st.write(s3, '*콘크리트 타설 높이가 0.5m 미만인 경우 :blue[2.5kN/m²], 0.5m 이상 1m 미만인 경우 :blue[3.5kN/m²], 1m 이상인 경우 :blue[5kN/m² 이상] 적용')

    st.markdown(border2, unsafe_allow_html=True)
    [A, I, S, E, fba, fsa, Ib_Q] = [Wood.A, Wood.I, Wood.S, Wood.E, Wood.fba, Wood.fsa, Wood.Ib_Q]
    st.write(h4, '2. 거푸집 합판 검토 및 장선 간격' + r'($\bm\small\color{red}L_j$)' + ' 결정')
    st.write(s1, '1) 개요')
    st.write(s2, '➣ 등분포 하중을 받는 단순보로 계산한다.')
    st.write(s1, '2) 합판이 받는 하중 (ω) [단위폭 1mm]')
    w_w = t_load/1e3*1
    Ljm = (8*fba*S/w_w)**(1/2)

    import re
    pattern = r'\d+'
    j1 = re.findall(pattern, d1);  j1 = float(j1[0])
    j2 = re.findall(pattern, d2);  j2 = float(j2[0])    

    Lj1 = (384*E*I*Ln/(5*w_w*j1))**(1/4)
    Lj2 = (384*E*I*j2/(5*w_w))**(1/4)
    st.write(s2, '➣ ω = {:.4f}'.format(t_load/1e3) + 'N/mm² x 1mm = {:.4f}'.format(w_w) + 'N/mm')
    st.write(s2, '① 휨응력에 의한 간격 검토')  #\color{red}, \textcolor{blue}{}(범위 지정), \boldsymbol [or \bm], \small, \normalize, \large, \Large
    st.write(s3, r"$\bm{\quad M = \Large \frac{ω \textcolor{red}{L_j}^2}{8} \normalsize \leq f_{ba}\,S}$")    
    st.write(s3, r"$\bm{\quad\textcolor{red}{L_j} \leq \Large\sqrt{\frac{8\,f_{ba}\,S}{ω}} \normalsize = \:} $" + "{:.1f}".format(Ljm) + ' mm')

    st.write(s2, '② 변위에 의한 간격 검토 (:red[', level, '] )')
    st.write(s3, 'a. 상대변형 기준')
    st.write(s3, r"$\bm{\quad\delta = \Large \frac{5\,ω \textcolor{red}{L_j}^4}{384\,E\,I} \normalsize \leq}$", d1)
    st.write(s3, r"$\bm{\quad\textcolor{red}{L_j} \leq \Large\sqrt[4]{\frac{384\,E\,I\,L_n}{5\,ω\,360}} \normalsize = \:} $" + "{:.1f}".format(Lj1) + ' mm')

    st.write(s3, 'b. 절대변형 기준')
    st.write(s3, r"$\bm{\quad\delta = \Large \frac{5\,ω \textcolor{red}{L_j}^4}{384\,E\,I} \normalsize \leq}$", d2)
    st.write(s3, r"$\bm{\quad\textcolor{red}{L_j} \leq \Large\sqrt[4]{\frac{384\,E\,I\,L_n}{5\,ω\,360}} \normalsize = \:} $" + "{:.1f}".format(Lj2) + ' mm')

    st.write(s2, '③ 장선 간격 검토결과')
    table.Interval(fn, Ljm, Lj1, Lj2)
    Lj = round(min(Ljm, Lj1, Lj2)*0.9, -1)
    st.write(s3, '➣ 검토 항목 중 최솟값 이하 간격으로 설치한다.')
    st.write(s3, '➣ 장선 간격을', r"$\bm{\small \: \color{blue}{" + str(int(Lj)) + '}}$', ':blue[mm] 간격으로 설치한다. (기본값 : 최솟값의 90% 정도로 설정)')
    
    st.write(s2, '③ 전단 검토')
    Vmax = w_w*max(Ljm, Lj1, Lj2)/2
    fs = Vmax/Ib_Q
    st.write(s3, r"$\bm{\quad V_{max} = \Large \frac{ω\,L_{max}}{2} \normalsize =}$", "{:.2f}".format(Vmax) + ' N')
    if fs <= fsa:
        st.write(s3, r"$\bm{\quad f_s = \Large \frac{V_{max}}{Ib/Q} \normalsize =}$", "{:.2f}".format(fs) + ' MPa', r'$\bm \leq$', "{:.2f}".format(fsa) + ' MPa', r'$\bm {( = f_{sa})} \qquad$', ':blue[OK]')
    else:
        st.write(s3, r"$\bm{\quad f_s = \Large \frac{V_{max}}{Ib/Q} \normalsize =}$", "{:.2f}".format(fs) + ' MPa', r'$\bm \gt$', "{:.2f}".format(fsa) + ' MPa', r'$\bm {( = f_{sa})} \qquad$', ':red[NG]')

    



