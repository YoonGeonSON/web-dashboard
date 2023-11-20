import streamlit as st

# 이미지 / 동영상을 화면에 보여주기

from PIL import Image

def main () :
    img = Image.open('./data\data/image_03.jpg')

    print(img)

    st.image(img)

    st.image( img, use_column_width=True)
    
    img_url = 'https://health.chosun.com/site/data/img_dir/2023/06/20/2023062002262_0.jpg'
    st.image(img_url) 

    # 동영상

    video_file = open('./data\data/video1.mp4', 'rb')
    st.video(video_file)

if __name__ == '__main__' :
    main()