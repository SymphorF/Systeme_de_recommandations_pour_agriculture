# Système de recommandations pour l’agriculture


3. Créer un environnement virtuel :

bash

poetry install

poetry shell  

python -m ipykernel install --user --name systeme-reco-agri --display-name "Poetry - Système Reco Agriculture"

Redémarrer VS Code 

Sélectioner le bon Kernel ("Poetry - Système Reco Agriculture")

L'environnement poetry est prêt à être utilisé


▶️ 4️⃣ Lancer l’API sur Docker
Build
docker build -t crop-api .

Run
docker run -p 8002:8000 crop-api

Documentation auto FastAPI

👉 http://localhost:8002/docs

**Lancer l'api en local**

se déplacer à la source

 fastapi dev main.py
 ou
 uvicorn main:app --reload

**Lancer streamlit**

streamlit run app.py


## Pour lancer l'ensemble et voir comment l'app fonctionne 

- lancer d'abord fastapi : fastapi dev main.py
- ensuite lancer l'app : streamlit run app.py
