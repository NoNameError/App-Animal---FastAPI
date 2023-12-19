from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()
class Animal(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str

banco: List[Animal] = []

@app.get('/animais')
def listar_animais():
    return banco

@app.get('/animais/{animal_id}')
def obter_animal(animal_id: str):
    for animal in banco:
        if animal.id == animal_id:
            return animal
        return {'error: ' 'Animal nao encontrado'}
    
@app.delete('/animais/{animal_id}')
def remover_animal(animal_id: str):
    position =-1
    #posiciao do animal
    for index, animal in enumerate(banco):
        if animal.id == animal_id:
            position = index
            break
        if position != -1:
            banco.pop(position)
            return {'mensagem: ' 'Animal removido com sucesso'}
        else:
            return {'Animal nao localizado'}


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco.append(animal)
    return None
