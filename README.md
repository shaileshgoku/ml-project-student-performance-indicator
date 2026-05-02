## Student Performance Indicator

This repository includes a Streamlit app entrypoint at `streamlit_app.py` and the trained model artifacts inside `artifacts/`.

## Run locally

```bash
streamlit run streamlit_app.py
```

## Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. In Streamlit Cloud, create a new app from the repo.
3. Set the main file path to `streamlit_app.py`.
4. Keep the Python version on a supported release such as Python 3.10, 3.11, or 3.12.
5. Deploy. Streamlit Cloud will install packages from `requirements.txt`.

## Notes

- The app depends on `artifacts/model.pkl` and `artifacts/preprocessor.pkl`, so those files must stay in the repo.
- `packages.txt` includes `libgomp1`, which helps binary ML dependencies like `xgboost` and `catboost` run on Streamlit Cloud.
