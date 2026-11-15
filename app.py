
Untitled2.ipynb
Untitled2.ipynb_

[1]
9 s
!pip install streamlit
Collecting streamlit
  Downloading streamlit-1.67.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: altair!=5.4.0,!=5.4.1,<7,>=5.0.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: numpy<3,>=1.25.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (2.4.6)
Requirement already satisfied: packaging>=20 in /usr/local/lib/python3.13/dist-packages (from streamlit) (26.3)
Requirement already satisfied: pandas<4,>=1.5.3 in /usr/local/lib/python3.13/dist-packages (from streamlit) (2.2.3)
Requirement already satisfied: pillow<14,>=9.2.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (11.3.0)
Collecting pydeck<1,>=0.8.0b4 (from streamlit)
  Downloading pydeck-0.9.3-py2.py3-none-any.whl.metadata (4.2 kB)
Requirement already satisfied: protobuf<8,>=5.26.1 in /usr/local/lib/python3.13/dist-packages (from streamlit) (6.33.6)
Requirement already satisfied: pyarrow!=25.0.0,<27,>=12.0.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (23.0.1)
Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.13/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: typing-extensions<5,>=4.10.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (4.16.0)
Requirement already satisfied: starlette<2,>=0.46.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (1.10.0)
Requirement already satisfied: uvicorn<1,>=0.30.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (0.54.0)
Requirement already satisfied: anyio<5,>=4.0.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (4.16.0)
Requirement already satisfied: python-multipart<1,>=0.0.10 in /usr/local/lib/python3.13/dist-packages (from streamlit) (0.0.33)
Requirement already satisfied: websockets<18,>=12.0.0 in /usr/local/lib/python3.13/dist-packages (from streamlit) (15.0.1)
Requirement already satisfied: itsdangerous<3,>=2.1.2 in /usr/local/lib/python3.13/dist-packages (from streamlit) (2.2.0)
Requirement already satisfied: watchdog<8,>=2.1.5 in /usr/local/lib/python3.13/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.13/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.13/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (4.26.0)
Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.13/dist-packages (from altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (2.28.0)
Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.13/dist-packages (from anyio<5,>=4.0.0->streamlit) (3.20)
Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.13/dist-packages (from pandas<4,>=1.5.3->streamlit) (2.9.0.post0)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.13/dist-packages (from pandas<4,>=1.5.3->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.13/dist-packages (from pandas<4,>=1.5.3->streamlit) (2026.6)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.13/dist-packages (from requests<3,>=2.27->streamlit) (3.4.9)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.13/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.13/dist-packages (from requests<3,>=2.27->streamlit) (2026.10.23)
Requirement already satisfied: h11>=0.8 in /usr/local/lib/python3.13/dist-packages (from uvicorn<1,>=0.30.0->streamlit) (0.16.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.13/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (3.0.4)
Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.13/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (26.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.13/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.13/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in /usr/local/lib/python3.13/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<7,>=5.0.0->streamlit) (2026.9.1)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.13/dist-packages (from python-dateutil>=2.8.2->pandas<4,>=1.5.3->streamlit) (1.17.0)
Downloading streamlit-1.67.0-py3-none-any.whl (11.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.2/11.2 MB 33.5 MB/s  0:00:00
Downloading pydeck-0.9.3-py2.py3-none-any.whl (11.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.4/11.4 MB 33.1 MB/s  0:00:00
Installing collected packages: pydeck, streamlit
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2/2 [streamlit]
Successfully installed pydeck-0.9.3 streamlit-1.67.0

[2]
2 s
import streamlit as st

st.title("💡 موقعي الأول بـ Python")
st.write("مرحباً بك في موقعي المصنوع بيدي!")

# آلة حاسبة بسيطة للتوفير
saving_month = st.number_input(
    "قداه تحب تخبّي كل شهر (بالدينار)؟", min_value=0, value=50
)
total_year = saving_month * 12

if st.button("احسب قداه تجمّع في العام"):
    st.success(f"في عام كامل باش تجمع تقريباً: {total_year} دينار! 🚀")
2026-11-15 19:51:07.994 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.292 
  Warning: to view this Streamlit app on a browser, run it with the following
  command:

    streamlit run /usr/local/lib/python3.13/dist-packages/colab_kernel_launcher.py [ARGUMENTS]
2026-11-15 19:51:08.293 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.299 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.302 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.306 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.309 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.312 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.321 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.326 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.331 Session state does not function when running a script without `streamlit run`
2026-11-15 19:51:08.337 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.340 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.345 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.349 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.352 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.361 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2026-11-15 19:51:08.364 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
Produits payants Colab
-
Résilier les contrats ici
