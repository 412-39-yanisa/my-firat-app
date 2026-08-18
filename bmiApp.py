import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# :red[💪 คำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่าน้ำหนัก และ ส่วนสูง
weight = st.number_input("กรอกนํ้าหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกส่วนวสูงของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)

if st.button("คำนวณค่า BMI"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  st.write("---")
  st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

  if bmi < 18.5:
      st.warning("คุณมีนํ้าหนักน้อยกว่าเกณฑ์ (ผอม)")
  elif 18.5 <= bmi < 23.0:
      st.success("คุณมีนํ้่าหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
  elif 23.0 <= bmi < 25.0:
      st.info("คุณเริ่มมีนํ้าหนักเกินเกณฑ์ (ท้วม)")
  else:
      st.error("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นางสาวญานิศา นิตยารส เลขที่39 ม.4/12")
                        
