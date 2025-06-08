from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud.users as users_crud, crud.jobs as jobs_crud, crud.applications as applications_crud, crud.resumes as resumes_crud
import schemas
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/")
def read_root():
    return {"message": "API está funcionando correctamente"}

# Rutas para usuarios
@app.post("/usuarios/", response_model=schemas.UsuarioOut)
def crear_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return users_crud.crear_usuario(db=db, usuario=usuario)

@app.get("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return users_crud.obtener_usuario(db=db, usuario_id=usuario_id)

@app.put("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def actualizar_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return users_crud.actualizar_usuario(db=db, usuario_id=usuario_id, usuario=usuario)

@app.delete("/usuarios/{usuario_id}", response_model=schemas.UsuarioOut)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return users_crud.eliminar_usuario(db=db, usuario_id=usuario_id)

# Rutas para vacantes
@app.post("/vacantes/", response_model=schemas.VacanteOut)
def crear_vacante(vacante: schemas.VacanteCreate, db: Session = Depends(get_db)):
    return jobs_crud.crear_vacante(db=db, vacante=vacante)

@app.get("/vacantes/{vacante_id}", response_model=schemas.VacanteOut)
def obtener_vacante(vacante_id: int, db: Session = Depends(get_db)):
    return jobs_crud.obtener_vacante(db=db, vacante_id=vacante_id)

@app.put("/vacantes/{vacante_id}", response_model=schemas.VacanteOut)
def actualizar_vacante(vacante_id: int, vacante: schemas.VacanteCreate, db: Session = Depends(get_db)):
    return jobs_crud.actualizar_vacante(db=db, vacante_id=vacante_id, vacante=vacante)

@app.delete("/vacantes/{vacante_id}", response_model=schemas.VacanteOut)
def eliminar_vacante(vacante_id: int, db: Session = Depends(get_db)):
    return jobs_crud.eliminar_vacante(db=db, vacante_id=vacante_id)

# Rutas para postulaciones
@app.post("/postulaciones/", response_model=schemas.PostulacionCreate)
def crear_postulacion(postulacion: schemas.PostulacionCreate, db: Session = Depends(get_db)):
    return applications_crud.crear_postulacion(db=db, postulacion=postulacion)

@app.put("/postulaciones/{postulacion_id}", response_model=schemas.PostulacionCreate)
def actualizar_postulacion(postulacion_id: int, postulacion: schemas.PostulacionCreate, db: Session = Depends(get_db)):
    return applications_crud.actualizar_postulacion(db=db, postulacion_id=postulacion_id, postulacion=postulacion)

@app.delete("/postulaciones/{postulacion_id}", response_model=schemas.PostulacionCreate)
def eliminar_postulacion(postulacion_id: int, db: Session = Depends(get_db)):
    return applications_crud.eliminar_postulacion(db=db, postulacion_id=postulacion_id)

# Rutas para hojas de vida
@app.post("/hojas_de_vida/", response_model=schemas.HojaDeVidaCreate)
def crear_hoja_de_vida(hoja_de_vida: schemas.HojaDeVidaCreate, db: Session = Depends(get_db)):
    return resumes_crud.crear_hoja_de_vida(db=db, hoja_de_vida=hoja_de_vida)

@app.put("/hojas_de_vida/{usuario_id}", response_model=schemas.HojaDeVidaCreate)
def actualizar_hoja_de_vida(usuario_id: int, hoja_de_vida: schemas.HojaDeVidaCreate, db: Session = Depends(get_db)):
    return resumes_crud.actualizar_hoja_de_vida(db=db, usuario_id=usuario_id, hoja_de_vida=hoja_de_vida)

@app.delete("/hojas_de_vida/{usuario_id}", response_model=schemas.HojaDeVidaCreate)
def eliminar_hoja_de_vida(usuario_id: int, db: Session = Depends(get_db)):
    return resumes_crud.eliminar_hoja_de_vida(db=db, usuario_id=usuario_id)
