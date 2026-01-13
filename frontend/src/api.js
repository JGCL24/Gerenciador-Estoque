const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// PRODUTOS
export async function fetchProducts() {
  const res = await fetch(`${API_BASE}/produtos/`);
  if (!res.ok) throw new Error('Erro ao buscar produtos');
  return res.json();
}

export async function createProduct(payload) {
  // O backend espera: nome, preco, validade, quant_min_estoque, id_admin_cadastrou
  // O frontend precisa pedir o id do admin logado (ajuste conforme login futuramente)
  const body = {
    nome: payload.name,
    preco: payload.price,
    validade: payload.validade || null,
    quant_min_estoque: payload.min_quantity,
    id_admin_cadastrou: 1 // <-- ajuste para o id do admin logado
  };
  const res = await fetch(`${API_BASE}/produtos/`, {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify(body)
  });
  if (!res.ok) throw new Error('Erro ao criar produto');
  return res.json();
}

export async function updateProduct(id, payload) {
  // Não implementado no backend, mas pode ser adaptado se necessário
  throw new Error('Atualização de produto não implementada na API');
}

export async function deleteProduct(id) {
  // Não implementado no backend, mas pode ser adaptado se necessário
  throw new Error('Exclusão de produto não implementada na API');
}

// ESTOQUE
export async function fetchStock() {
  const res = await fetch(`${API_BASE}/estoque/`);
  if (!res.ok) throw new Error('Erro ao buscar estoque');
  return res.json();
}

// MOVIMENTAÇÕES
export async function fetchMovements() {
  const res = await fetch(`${API_BASE}/estoque/movimentacoes`);
  if (!res.ok) throw new Error('Erro ao buscar movimentações');
  return res.json();
}

export async function createMovement(payload) {
  // O backend espera: id_estoque, tipo, quantidade, data
  // O frontend precisa buscar o id_estoque do produto antes de criar a movimentação
  // Aqui é necessário um ajuste para buscar o estoque do produto
  const estoqueRes = await fetch(`${API_BASE}/estoque/produto/${payload.product_id}`);
  if (!estoqueRes.ok) throw new Error('Produto não possui estoque cadastrado');
  const estoque = await estoqueRes.json();
  const body = {
    id_estoque: estoque.id_estoque,
    tipo: payload.type,
    quantidade: payload.quantity,
    data: new Date().toISOString().split('T')[0] // data de hoje
  };
  const res = await fetch(`${API_BASE}/estoque/movimentacoes`, {
    method: 'POST', headers: {'Content-Type':'application/json'},
    body: JSON.stringify(body)
  });
  const data = await res.json();
  if (!res.ok) throw new Error(data.detail || data.message || 'Erro ao criar movimentação');
  return data;
}
