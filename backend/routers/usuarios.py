from fastapi import APIRouter, HTTPException
from typing import List
from database import db
from schemas import UsuarioCreate, UsuarioResponse, UsuarioLogin
import bcrypt

router = APIRouter()

@router.post("/", response_model=UsuarioResponse, status_code=201)
async def criar_usuario(usuario: UsuarioCreate):
    """Cria um novo usuário"""
    try:
        # Hash seguro da senha usando bcrypt
        senha_hash = bcrypt.hashpw(usuario.senha.encode(), bcrypt.gensalt())

        query = """
            INSERT INTO usuario (nome, senha, tipo_usuario)
            VALUES (%s, %s, %s)
            RETURNING id_usuario, nome, tipo_usuario
        """
        result = db.execute_query(query, (
            usuario.nome, senha_hash, usuario.tipo_usuario
        ))
        if result:
            return UsuarioResponse(**result[0])
        raise HTTPException(status_code=500, detail="Erro ao criar usuário")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar usuário: {str(e)}")

@router.get("/", response_model=List[UsuarioResponse])
async def listar_usuarios():
    """Lista todos os usuários"""
    try:
        query = "SELECT id_usuario, nome, tipo_usuario FROM usuario"
        result = db.execute_query(query)
        return [UsuarioResponse(**row) for row in result]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar usuários: {str(e)}")

@router.get("/{id_usuario}", response_model=UsuarioResponse)
async def obter_usuario(id_usuario: int):
    """Obtém um usuário por ID"""
    try:
        query = "SELECT id_usuario, nome, tipo_usuario FROM usuario WHERE id_usuario = %s"
        result = db.execute_query(query, (id_usuario,))
        if not result:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return UsuarioResponse(**result[0])
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter usuário: {str(e)}")

@router.put("/{id_usuario}", response_model=UsuarioResponse)
async def atualizar_usuario(id_usuario: int, usuario: UsuarioCreate):
    """Atualiza um usuário"""
    try:
        # Verifica se existe
        query_check = "SELECT * FROM usuario WHERE id_usuario = %s"
        existing = db.execute_query(query_check, (id_usuario,))
        if not existing:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        senha_hash = bcrypt.hashpw(usuario.senha.encode(), bcrypt.gensalt())
        
        query = """
            UPDATE usuario 
            SET nome = %s, senha = %s, tipo_usuario = %s
            WHERE id_usuario = %s
            RETURNING id_usuario, nome, tipo_usuario
        """
        result = db.execute_query(query, (
            usuario.nome, senha_hash, usuario.tipo_usuario, id_usuario
        ))
        
        if result:
            return UsuarioResponse(**result[0])
        raise HTTPException(status_code=500, detail="Erro ao atualizar usuário")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar usuário: {str(e)}")

@router.delete("/{id_usuario}", status_code=204)
async def deletar_usuario(id_usuario: int):
    """Deleta um usuário"""
    try:
        query_check = "SELECT * FROM usuario WHERE id_usuario = %s"
        existing = db.execute_query(query_check, (id_usuario,))
        if not existing:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        
        query = "DELETE FROM usuario WHERE id_usuario = %s"
        db.execute_query(query, (id_usuario,), fetch=False)
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao deletar usuário: {str(e)}")

@router.post("/login")
async def login(credentials: UsuarioLogin):
    """Autentica um usuário"""
    try:
        # Busca usuário pelo ID
        query = "SELECT id_usuario, nome, tipo_usuario, senha FROM usuario WHERE id_usuario = %s"
        result = db.execute_query(query, (credentials.id_usuario,))
        if not result:
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
        usuario_db = result[0]
        # Verifica senha usando bcrypt
        if not bcrypt.checkpw(credentials.senha.encode(), usuario_db['senha']):
            raise HTTPException(status_code=401, detail="Credenciais inválidas")
        return {"message": "Login bem-sucedido", "usuario": UsuarioResponse(**usuario_db)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao fazer login: {str(e)}")
