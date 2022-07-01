import streamlit as st
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
import pandas as pd

st.title("TMU Orchestra Certificate Generator")
st.write("Developed by 王彥成")
st.write("Python version: 3.9.1")

#check membership
id = st.selectbox("請選擇您所擔任工作人員的場次",("20211227期末音樂會", "20220315國家音樂廳年度音樂會"))

#input name
text_input = st.text_input("Please enter your name")

#font
fontpath = "GenRyuMin-SB.ttc"
font = ImageFont.truetype(fontpath, 270)

#check eligibility
concert_one = pd.read_csv("20211227.csv")
concert_two = pd.read_csv("20220315.csv")


#embed image
def generate_cert(filename):
    if text_input:
        #st.write("%s - Attendance %s, Requirement: %s" %(text_input)) #display personal info  / fulfilled or not
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        if len(text_input)==2:
            draw.text((1130, 850),text_input[0], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1600, 850),text_input[1], font = font,fill = "#ffffff", stroke_width = 1 )
            st.image(img)
        elif len(text_input)==3:
            draw.text((1010, 850),text_input[0], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1360, 850),text_input[1], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1710, 850),text_input[2], font = font,fill = "#ffffff", stroke_width = 1 )
            st.image(img)
        elif len(text_input)==4:
            draw.text((830, 850),text_input[0], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1180, 850),text_input[1], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1530, 850),text_input[2], font = font,fill = "#ffffff", stroke_width = 1 )
            draw.text((1880, 850),text_input[3], font = font,fill = "#ffffff", stroke_width = 1 )
            st.image(img)
            
            
        #Transform PIL to byte
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_img = buf.getvalue()
        
        st.download_button(label = "Download Certificate", 
                        data = byte_img,
                        file_name = text_input + ".png")
    else:
        st.write("Enter to check if you're eligible")

if id == "20211227期末音樂會":
    if text_input in concert_one.values:
        generate_cert(filename = '20211227.png')
    elif text_input:
        st.write("%s您好，"%(text_input))
        st.write("您並未參與本場音樂會擔任志工")
        st.write("若有問題歡迎來信tmuorchestra1979@gmail.com")
elif id == "20220315國家音樂廳年度音樂會":
    if text_input in concert_two.values:
        generate_cert(filename = "20220315.png")
    elif text_input:
        st.write("%s您好，"%(text_input))
        st.write("您並未參與本場音樂會擔任志工")
        st.write("若有問題歡迎來信tmuorchestra1979@gmail.com")