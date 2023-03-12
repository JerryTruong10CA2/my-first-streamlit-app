import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
  if a == 0:
    if b == 0:
        st.write("Phương trình vô số nghiệm")
    else:
        st.write("Phương trình vô nghiệm")
  else:
    x = -b / a
    st.write("Nghiệm của phương trình là: x = ", x)