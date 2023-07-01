import streamlit as st
import numpy as np
import table

def Tab(In, color, fn, s1, s2, s3, h4, h5, Wood, Joist, Yoke):
    border1 = '<hr style="border-top: 5px double ' + color + '; margin-top: 0px; margin-bottom:30px; border-radius: 10px">'
    border2 = '<hr style="border-top: 1px solid '  + color + '; margin-top:30px; margin-bottom:30px; border-radius: 10px">'
    [s_h, s_t, s_weight, w_weight, w_s, w_t, w_angle, level] = [In.s_h, In.s_t, In.s_weight, In.w_weight, In.w_s, In.w_t, In.w_angle, In.level]
    # [j_s, j_b, j_h, j_d, j_t] = [In.j_s, In.j_b, In.j_h, In.j_d, In.j_t]

    st.markdown(border1, unsafe_allow_html=True)
    st.write(h4, '1. 설계하중 산정')
    st.write(s1, '1) 연직하중 (고정하중 + 작업하중)')
    t_load = table.Load(fn, s_t, s_weight, w_weight)
    st.write(s3, '*콘크리트 타설 높이가 0.5m 미만인 경우 :blue[2.5kN/m²], 0.5m 이상 1m 미만인 경우 :blue[3.5kN/m²], 1m 이상인 경우 :blue[5kN/m² 이상] 적용')

    st.markdown(border2, unsafe_allow_html=True)
    [A, I, S, E, fba, fsa] = [Wood.A, Wood.I, Wood.S, Wood.E, Wood.fba, Wood.fsa]
    st.write(h4, '2. 거푸집 합판 검토 및 장선 간격' + r'($\bm\small\color{red}L_j$)' + ' 결정')
    st.write(s1, '1) 개요')
    st.write(s2, '➣ 등분포 하중을 받는 단순보로 계산한다.')
    st.write(s1, '2) 합판이 받는 하중 (ω) [단위폭 1mm]')
    w_w = t_load/1e3*1
    st.write(s2, '➣ ω = {:.4f}'.format(t_load/1e3) + 'N/mm² x 1mm = {:.4f}'.format(w_w) + 'N/mm')
    st.write(s2, '① 휨응력에 의한 간격 검토')   #\color{red}, \textcolor{blue}{}(범위 지정), \boldsymbol [or /bm], \small, \normalize, \large, \Large
    st.write(s3, r"$\bm{M = \Large \frac{ω \textcolor{red}{L_j}^2}{8} \normalsize \leq f_{ba}\,S}$")
    Lj = np.sqrt(8*fba*S/w_w)
    st.write(s3, r"$\bm{\textcolor{red}{L_j} \leq \Large\sqrt{\frac{8\,f_{ba}\,S}{ω}} \normalsize = \:} $" + "{:.1f}".format(Lj) + ' mm')

    st.write(s2, '② 변위에 의한 간격 검토 (:red[', level, '] )')
    st.write(s3, 'a. 절대변형기준')

    st.write(s3, 'b. 상대변형기준')
      

    

