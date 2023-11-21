import streamlit as st
import pandas as pd

def main() :
    
    df = pd.read_csv('./data\data/iris.csv')
    # print(type(df))
    if st.button('데이터프레임 보기') : # button() 클릭 시 True
        st.dataframe(df)

    name = 'Mike' 

    if st.button('대문자') :
        st.subheader( name.upper() )

    if st.button('소문자') :
        st.subheader ( name.lower() )

    # 라디오버튼을 만드는 방법
    selected = st.radio('정렬을 선택하세요' ,['오름차순 정렬', '내림차순 정렬'])
    # print(selected)
    # df의 petal_lenth 컬럼을 정렬하도록 한다.
    if selected == '오름차순 정렬' :
       st.dataframe(df.sort_values('petal_length'))

    elif selected == '내림차순 정렬' :
       st.dataframe (df.sort_values('petal_length', ascending=False))

    # 체크박스를 나타내는 방법
    if st.checkbox('체크박스') :
        st.dataframe( df )
    else :
        st.write('')

    # 셀렉트박스 : 여러개중에 한개를 선택 할 때
    language = ['Python', 'Java', 'C', 'PHP', 'GO']

    my_choice = st.selectbox('좋아하는 언어를 선택하세요', language) 
    st.text('저는 {}언어를 좋아합니다.'.format( my_choice ))
    # st.text(f"저는 {my_choice}언어를 좋아합니다.")

    if my_choice == language[0] or my_choice == [3] or my_choice == language[-1] :
        st.text('배우기 쉽습니다.')
    elif my_choice == language[1] or my_choice == language[2] :
        st.text('배우기 어렵습니다.')

     # 멀티셀렉트 : 여러개를 동시에 선택 가능
    
    selected_list = st.multiselect('여러개 선택 가능', df.columns)

    print(selected_list)
    
    if len(selected_list) != 0 :
        st.dataframe(df[selected_list])
    else :
        st.text('')

    # 슬라이더 (이름, 최소값, 최대값 , value=(초기값) , step=(간격))
    age = st.slider('나이', 0 , 100)

    st.text ('제 나이는 ' + str(age) + '세 입니다.')    

    st.slider('데이터', 50, 200, step= 10 )  

    st.slider('나이', 0 , 100, value= 33)

    st.slider('데이터', -0.5,2.7, step = 0.1 )

    with st.expander('상세내용보기') :
        st.text('상세 내용 입니다~~')
        
     
     



if __name__ == '__main__' :
    main()