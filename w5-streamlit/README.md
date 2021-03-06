# Week 5 - streamlit, fastapi \& quarto

## Streamlit

Examples of how to create applications in streamlit through:

- [Hello world application](hello_world)
- [Small report with plots and dataframes in streamlit](small_report/main.py)
- [Monte Carlo simulation](mc_simulation/main.py)
- [Favorite dish application](dishes/favorite_dish.py)
- [Test checker application](checker/main.py)

Run, e.g., with:

```
streamlit run main.py
```

## FastAPI

Small example of creating REST API through FastAPI:

- [Boston model price predictor](simple_api/boston_api.py)
- [Image color predictor](simple_api/image_api.py)

Run, e.g., with:

```
uvicorn boston_api:app
```

## Quarto 

How to create [a simple report in Quarto](quarto_demo/README.md)

- [Report with code, data and plots](quarto_demo/raport.ipynb)
- [With html output](quarto_demo/raport.html)
- [And pdf](quarto_demo/raport.pdf)
