rem activate venv
if exist .venv\ (
   .venv\Scripts\activate
) else (
  virtualenv .venv
  .venv\Scripts\activate
  pip install -r requirements.txt
)
