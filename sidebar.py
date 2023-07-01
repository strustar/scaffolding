import streamlit as st
import numpy as np

##### sidebar =======================================================================================================
def Sidebar(h2, h4):
    st.sidebar.write(h2, ':blue[슬래브]')
    [col1, col2, col3] = st.sidebar.columns([1, 1, 1.5])
    with col1:
        s_h = st.number_input(h4+':green[층고 [mm]]', min_value = 100., value = 2000., step = 100., format = '%f')
    with col2:
        s_t = st.number_input(h4+':green[두께 [mm]]', min_value = 50., value = 350., step = 10., format = '%f')
    with col3:
        Ln = st.number_input(h4+':green[동바리 순간격 [mm] (Ln) ]', min_value = 50., value = 1500., step = 100., format = '%f')

    st.sidebar.write(h2, ':blue[자중]')
    [col1, col2] = st.sidebar.columns(2)
    with col1:
        s_weight = st.number_input(h4+':green[콘크리트 단위중량 [kN/m³]]', min_value = 10., value = 24., step = 1., format = '%f')
    with col2:
        w_weight = st.number_input(h4+':green[거푸집 단위중량 [kN/m²]]', min_value = 0.1, value = 0.4, step = 0.1, format = '%f')

    st.sidebar.write(h2, ':blue[거푸집 널의 변형기준]')
    [col1, col2] = st.sidebar.columns(2)
    with col1:
        level = st.radio(h4+':green[표면의 등급]', ('A급', 'B급', 'C급'), horizontal=True)
        if 'A' in level:  d1 = 360;  d2 = '3mm'
        if 'B' in level:  d1 = 270;  d2 = '6mm'
        if 'C' in level:  d1 = 180;  d2 = '13mm'
        d1 = r'$\,\bm{\Large\frac{L_n}{'+str(d1)+'}}$'
        
    with col2:        
        st.write(h4+'➣ 상대변형 :', d1)
        st.write(h4+'➣ 절대변형 :', d2)
    # with col1:

    st.sidebar.write(h2, ':blue[거푸집용 합판]')
    w_s = '합판'
    [col1, col2] = st.sidebar.columns([1,1], gap = "small")
    with col1:
        w_t = st.radio(h4+':green[합판 두께 [mm]]', (12., 15., 18.), horizontal=True)
    with col2:
        w_angle = st.radio(h4+':green[하중 방향 [각도]]', (0, 90), horizontal=True)

    j_s = ['',''];  j_b = np.zeros(2);  j_h = np.zeros(2);  j_d = np.zeros(2);  j_t = np.zeros(2)
    for i in [0,1]:
        if i == 0:  typ = '장선'
        if i == 1:  typ = '멍에'
        st.sidebar.write(h2, ':blue['+typ+']')
        
        j_s[i] = st.sidebar.radio(h4+':green['+typ+' 종류]', ('목재', '각형강관', '원형강관'), horizontal=True, index=1)
        [col1, col2, col3] = st.sidebar.columns(3)
        a = {'step':5., 'format':'%f'}
        # a['step'] = 10.
        # st.write(a['step'])
        with col1:
            if '목재' in j_s[i]:
                j_b[i] = st.number_input(h4+':green[폭 [mm]]', min_value = 10.+i, value = 30., **a)
            if '각형' in j_s[i]:
                j_b[i] = st.number_input(h4+':green[폭 [mm]]', min_value = 10.+i, value = 50.+25*i, step = 5., format = '%f')
        with col2:
            if '목재' in j_s[i]:
                j_h[i] = st.number_input(h4+':green[높이 [mm]]', min_value = 10.+i, value = 50., step = 5., format = '%f')
            if '각형' in j_s[i]:
                j_h[i] = st.number_input(h4+':green[높이 [mm]]', min_value = 10.+i, value = 50.+75*i, step = 5., format = '%f')
            if '원형' in j_s[i]:
                j_d[i] = st.number_input(h4+':green[직경 [mm]]', min_value = 10.+i, value = 42.7+17.2*i, step = 5., format = '%.1f')
        with col3:
            if '각형' in j_s[i]:
                j_t[i] = st.number_input(h4+':green[두께 [mm]]', min_value = 1.+i/10, value = 2.3+0.9*i-0., step = 0.1, format = '%.1f')
            if '원형' in j_s[i]:
                j_t[i] = st.number_input(h4+':green[두께 [mm]]', min_value = 1.+i/10, value = 2.2+0.1*i, step = 0.1, format = '%.1f')

    class In:
        pass
    [In.s_h, In.s_t, In.s_weight, In.w_weight, In.w_s, In.w_t, In.w_angle, In.level, In.d1, In.d2, In.Ln] = [s_h, s_t, s_weight, w_weight, w_s, w_t, w_angle, level, d1, d2, Ln]
    [In.j_s, In.j_b, In.j_h, In.j_d, In.j_t] = [j_s, j_b, j_h, j_d, j_t]    
    return In