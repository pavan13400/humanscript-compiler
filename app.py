import streamlit as st
from parser import parser, commands
from codegen import generate_code
import io
from normalizer import normalize
import sys
st.title("HumanScript Compiler")

text = st.text_area("Enter Instructions")

if st.button("Compile"):

    commands.clear()

    lines = text.split("\n")

    for line in lines:
        normalized = normalize(line)
        try:
            parser.parse(normalized)
        except:
            pass

    code = generate_code(commands)

    st.subheader("Generated Python Code")
    st.code(code)

    st.subheader("Output")

    # Capture output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()

    try:
        exec(code)
        output = buffer.getvalue()
    except Exception as e:
        output = str(e)

    sys.stdout = old_stdout

    st.success(output)