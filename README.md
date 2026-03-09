# Système de recommandations pour l’agriculture

Structure 

```
Systeme_de_recommandations_pour_agriculture
│
├── .git/
├── .github/                  # CI/CD Github Actions
├── api/                      # API (FastAPI ou Flask)
│   └── tests
├── data/                     # datasets
│   ├── raw/
│   └── processed/
├── model/                    # model retenu
│   └── model_rf_tt.pkl
├── notebook/                 # notebooks d'analyse
│   ├── notebook.ipynb
│   └── mlflow.db
├── streamlit_app/            # interface utilisateur
│   └── app.py
├── github/                   # scripts liés au repo ou CI
├── main.py                   # script principal ML / pipeline
├── dockerfile                # container Docker
├── requirements.txt
├── pyproject.toml
├── poetry.lock
├── README.md
├── mlflow.PNG                # capture interface MLflow
├── .gitignore
└── .gitattributes
```


1. Créer un environnement virtuel :

bash

poetry install

poetry shell  

python -m ipykernel install --user --name systeme-reco-agri --display-name "Poetry - Système Reco Agriculture"

Redémarrer VS Code 

Sélectioner le bon Kernel ("Poetry - Système Reco Agriculture")

L'environnement poetry est prêt à être utilisé


2. Lancer l’API sur Docker
Build
docker build -t crop-api .

Run
docker run -p 8003:8000 crop-api

Documentation auto FastAPI

👉 http://localhost:8002/docs

3. Lancer l'api en local

se déplacer à la source

 fastapi dev main.py
 ou
 uvicorn main:app --reload

4. Lancer streamlit

streamlit run app.py


## Pour lancer l'ensemble et voir comment l'app fonctionne 

- ouvrir un terminal lancer d'abord fastapi : fastapi dev main.py
- ensuite ouvrir un second terminal et lancer l'app : streamlit run app.py


5. Lancer MLflow en local :

bash
 
 notebook 
 
 mlflow ui

Ensuite lancer 

http://127.0.0.1:5000




