import Zstreamlit as st
import pandas as pd 

st.title("my title")
st.header("my header")
st.subheader("my sub header")
st.write("this is plain text only")
st.text("this is text same as write method")
value=st.slider("select the values",10,100)
st.write(value)
st.markdown("**This is markdown**\n*italic*")

ans=st.button("submit")
st.write(ans)
st.caption("this is caption ,here we see samll and light sentance")

df={"name":["A","B","C",'D'],
    "age":[1,2,3,4]}
st.dataframe(df)

# use to show code ,it not run
st.code("print('hello')\n" \
"print('ram')")

text=st.text_input("enter your name")
st.write(text)
num=st.number_input("enter number")
st.write(num)

result=st.text_area("Enter your introduction")
st.write(result)
