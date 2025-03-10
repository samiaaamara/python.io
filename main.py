from typing import Union,List
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pour autoriser toutes les origines (localhost, 127.0.0.1...)
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, DELETE...
    allow_headers=["*"],  # Tous les headers
)

etudiants = [
    {"id": 1,
    "nom": "Sami",
    "age": 21,
    "departement": "Informatique",},
    {"id": 2,
    "nom": "Ali",
    "age": 22,
    "departement": "Informatique",},
    {"id": 3,
    "nom": "Ahmed",
    "age": 23,
    "departement": "Informatique",},
]

@app.get("/etudiants")
def getetudiant():
    return etudiants

@app.get("/etudiants/{id}")
def getetudiant(id: int):
    for etudiant in etudiants:
        if etudiant["id"] == id:
            return etudiant
    return "etudiant not found"

@app.post("/etudiants")
def createetudiant(etudiant: dict):
    etudiants.append(etudiant)
    return etudiant

@app.put("/etudiants/{id}")
def updateetudiant(id: int, etudiant: dict):
    for i in range(len(etudiants)):
        if etudiants[i]["id"] == id:
            etudiants[i] = etudiant
            return etudiant
    return "etudiant not found"

@app.delete("/etudiants/{id}")
def deleteetudiant(id: int):
    for i in range(len(etudiants)):
        if etudiants[i]["id"] == id:
            etudiants.pop(i)
            return "etudiant deleted"
    return "etudiant not found"