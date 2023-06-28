import streamlit as st
import numpy as np
import table

def Tab(In, color, fn, s1, s2, s3, h4, h5):
    border1 = '<hr style="border-top: 5px double ' + color + '; margin-top: 0px; margin-bottom:30px; border-radius: 10px">'
    border2 = '<hr style="border-top: 1px solid '  + color + '; margin-top:30px; margin-bottom:30px; border-radius: 10px">'
    [s_h, s_t, s_weight, w_weight, w_s, w_t, w_angle] = [In.s_h, In.s_t, In.s_weight, In.w_weight, In.w_s, In.w_t, In.w_angle]
    # [j_s, j_b, j_h, j_d, j_t] = [In.j_s, In.j_b, In.j_h, In.j_d, In.j_t]

    st.markdown(border1, unsafe_allow_html=True)
    st.write(h4, '1. 설계하중 산정')
    st.write(s1, '1) 연직하중 (고정하중 + 작업하중)')
    table.T2(fn, s_t, s_weight, w_weight)
    st.write(s3, '*콘크리트 타설 높이가 0.5m 미만인 경우 :blue[2.5kN/m²], 0.5m 이상 1m 미만인 경우 :blue[3.5kN/m²], 1m 이상인 경우 :blue[5kN/m² 이상] 적용')

    st.markdown(border2, unsafe_allow_html=True)
    st.write(h4, '2. 거푸집 합판 검토 및 장선 간격 결정')
    st.write(s1, '1) 도해')
    
