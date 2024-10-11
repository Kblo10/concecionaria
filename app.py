from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Cliente, Veiculo, Funcionario, Venda, PerfilCargo, TesteDrive, Estoque, Galpao, Financiamento, SituacaoFinanciamento

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:senac@localhost/concessionaria' #'mysql+pymysql://dba:Pipoca123@10.160.215.50/concessionaria_auto_prime' 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

f'?connect_timeout=36000'  # Timeout de 36000 segundos


@app.route('/')
def index():
    return render_template('index.html')

# Rota para listar clientes
@app.route('/clientes', methods=['GET'])
def list_clientes():
    clientes = Cliente.query.all()
    return render_template('list_clientes.html', clientes=clientes)

# Rota para adicionar um cliente
@app.route('/clientes/adicionar', methods=['GET', 'POST'])
def add_cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        novo_cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('list_clientes'))
    return render_template('add_cliente.html')

# Rota para editar um cliente
@app.route('/clientes/editar/<int:id>', methods=['GET', 'POST'])
def edit_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.cpf = request.form['cpf']
        cliente.telefone = request.form['telefone']
        cliente.endereco = request.form['endereco']
        db.session.commit()
        return redirect(url_for('list_clientes'))
    return render_template('edit_cliente.html', cliente=cliente)

# Rota para deletar um cliente
@app.route('/clientes/deletar/<int:id>', methods=['POST'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('list_clientes'))

# Rota para listar veículos
@app.route('/veiculos', methods=['GET'])
def list_veiculos():
    veiculos = Veiculo.query.all()
    return render_template('list_veiculos.html', veiculos=veiculos)

# Rota para adicionar um veículo
@app.route('/veiculos/adicionar', methods=['GET', 'POST'])
def add_veiculo():
    if request.method == 'POST':
        modelo = request.form['modelo']
        ano = request.form['ano']
        cor = request.form['cor']
        placa = request.form['placa']
        valor = request.form['valor']
        novo_veiculo = Veiculo(modelo=modelo, ano=ano, cor=cor, placa=placa, valor=valor)
        db.session.add(novo_veiculo)
        db.session.commit()
        return redirect(url_for('list_veiculos'))
    return render_template('add_veiculo.html')

# Rota para editar um veículo
@app.route('/veiculos/editar/<int:id>', methods=['GET', 'POST'])
def edit_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    if request.method == 'POST':
        veiculo.modelo = request.form['modelo']
        veiculo.ano = request.form['ano']
        veiculo.cor = request.form['cor']
        veiculo.placa = request.form['placa']
        veiculo.valor = request.form['valor']
        db.session.commit()
        return redirect(url_for('list_veiculos'))
    return render_template('edit_veiculo.html', veiculo=veiculo)

# Rota para deletar um veículo
@app.route('/veiculos/deletar/<int:id>', methods=['POST'])
def delete_veiculo(id):
    veiculo = Veiculo.query.get_or_404(id)
    db.session.delete(veiculo)
    db.session.commit()
    return redirect(url_for('list_veiculos'))

# Rota para listar funcionários
@app.route('/funcionarios', methods=['GET'])
def list_funcionarios():
    funcionarios = Funcionario.query.all()
    return render_template('list_funcionarios.html', funcionarios=funcionarios)

# Rota para adicionar um funcionário
@app.route('/funcionarios/adicionar', methods=['GET', 'POST'])
def add_funcionario():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        perfil_cargo_id = request.form['perfil_cargo_id']
        novo_funcionario = Funcionario(nome=nome, cpf=cpf, telefone=telefone, endereco=endereco, perfil_cargo_id=perfil_cargo_id)
        db.session.add(novo_funcionario)
        db.session.commit()
        return redirect(url_for('list_funcionarios'))
    return render_template('add_funcionario.html')

# Rota para editar um funcionário
@app.route('/funcionarios/editar/<int:id>', methods=['GET', 'POST'])
def edit_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    if request.method == 'POST':
        funcionario.nome = request.form['nome']
        funcionario.cpf = request.form['cpf']
        funcionario.telefone = request.form['telefone']
        funcionario.endereco = request.form['endereco']
        funcionario.perfil_cargo_id = request.form['perfil_cargo_id']
        db.session.commit()
        return redirect(url_for('list_funcionarios'))
    return render_template('edit_funcionario.html', funcionario=funcionario)

# Rota para deletar um funcionário
@app.route('/funcionarios/deletar/<int:id>', methods=['POST'])
def delete_funcionario(id):
    funcionario = Funcionario.query.get_or_404(id)
    db.session.delete(funcionario)
    db.session.commit()
    return redirect(url_for('list_funcionarios'))

# Rota para listar vendas
@app.route('/vendas', methods=['GET'])
def list_vendas():
    vendas = Venda.query.all()
    return render_template('list_vendas.html', vendas=vendas)

# Rota para adicionar uma venda
@app.route('/vendas/adicionar', methods=['GET', 'POST'])
def add_venda():
    if request.method == 'POST':
        qtd_vendas = request.form['qtd_vendas']
        veiculos_id = request.form['veiculos_id']
        clientes_id = request.form['clientes_id']
        funcionarios_id = request.form['funcionarios_id']
        nova_venda = Venda(qtd_vendas=qtd_vendas, veiculos_id=veiculos_id, clientes_id=clientes_id, funcionarios_id=funcionarios_id)
        db.session.add(nova_venda)
        db.session.commit()
        return redirect(url_for('list_vendas'))
    return render_template('add_venda.html')

# Rota para editar uma venda
@app.route('/vendas/editar/<int:id>', methods=['GET', 'POST'])
def edit_venda(id):
    venda = Venda.query.get_or_404(id)
    if request.method == 'POST':
        venda.qtd_vendas = request.form['qtd_vendas']
        venda.veiculos_id = request.form['veiculos_id']
        venda.clientes_id = request.form['clientes_id']
        venda.funcionarios_id = request.form['funcionarios_id']
        db.session.commit()
        return redirect(url_for('list_vendas'))
    return render_template('edit_venda.html', venda=venda)

# Rota para deletar uma venda
@app.route('/vendas/deletar/<int:id>', methods=['POST'])
def delete_venda(id):
    venda = Venda.query.get_or_404(id)
    db.session.delete(venda)
    db.session.commit()
    return redirect(url_for('list_vendas'))

# Rota para listar perfis de cargos
@app.route('/perfis_cargos', methods=['GET'])
def list_perfis_cargos():
    perfis = PerfilCargo.query.all()
    return render_template('list_perfis_cargos.html', perfis=perfis)

# Rota para adicionar um perfil de cargo
@app.route('/perfis_cargos/adicionar', methods=['GET', 'POST'])
def add_perfil_cargo():
    if request.method == 'POST':
        tipo = request.form['tipo']
        novo_perfil = PerfilCargo(tipo=tipo)
        db.session.add(novo_perfil)
        db.session.commit()
        return redirect(url_for('list_perfis_cargos'))
    return render_template('add_perfil_cargo.html')

# Rota para editar um perfil de cargo
@app.route('/perfis_cargos/editar/<int:id>', methods=['GET', 'POST'])
def edit_perfil_cargo(id):
    perfil = PerfilCargo.query.get_or_404(id)
    if request.method == 'POST':
        perfil.tipo = request.form['tipo']
        db.session.commit()
        return redirect(url_for('list_perfis_cargos'))
    return render_template('edit_perfil_cargo.html', perfil=perfil)

# Rota para deletar um perfil de cargo
@app.route('/perfis_cargos/deletar/<int:id>', methods=['POST'])
def delete_perfil_cargo(id):
    perfil = PerfilCargo.query.get_or_404(id)
    db.session.delete(perfil)
    db.session.commit()
    return redirect(url_for('list_perfis_cargos'))

# Rota para listar teste drive
@app.route('/teste_drive', methods=['GET'])
def list_teste_drive():
    testes = TesteDrive.query.all()
    return render_template('list_teste_drive.html', testes=testes)

# Rota para adicionar um teste drive
@app.route('/teste_drive/adicionar', methods=['GET', 'POST'])
def add_teste_drive():
    if request.method == 'POST':
        agendamento = request.form['agendamento']
        clientes_id = request.form['clientes_id']
        veiculos_id = request.form['veiculos_id']
        novo_teste = TesteDrive(agendamento=agendamento, clientes_id=clientes_id, veiculos_id=veiculos_id)
        db.session.add(novo_teste)
        db.session.commit()
        return redirect(url_for('list_teste_drive'))
    return render_template('add_teste_drive.html')

# Rota para editar um teste drive
@app.route('/teste_drive/editar/<int:id>', methods=['GET', 'POST'])
def edit_teste_drive(id):
    teste = TesteDrive.query.get_or_404(id)
    if request.method == 'POST':
        teste.agendamento = request.form['agendamento']
        teste.clientes_id = request.form['clientes_id']
        teste.veiculos_id = request.form['veiculos_id']
        db.session.commit()
        return redirect(url_for('list_teste_drive'))
    return render_template('edit_teste_drive.html', teste=teste)

# Rota para deletar um teste drive
@app.route('/teste_drive/deletar/<int:id>', methods=['POST'])
def delete_teste_drive(id):
    teste = TesteDrive.query.get_or_404(id)
    db.session.delete(teste)
    db.session.commit()
    return redirect(url_for('list_teste_drive'))

# Rota para listar estoque
@app.route('/estoque', methods=['GET'])
def list_estoque():
    estoque = Estoque.query.all()
    return render_template('list_estoque.html', estoque=estoque)

# Rota para adicionar ao estoque
@app.route('/estoque/adicionar', methods=['GET', 'POST'])
def add_estoque():
    if request.method == 'POST':
        quantidade = request.form['quantidade']
        veiculos_id = request.form['veiculos_id']
        galpao_id = request.form['galpao_id']
        novo_estoque = Estoque(quantidade=quantidade, veiculos_id=veiculos_id, galpao_id=galpao_id)
        db.session.add(novo_estoque)
        db.session.commit()
        return redirect(url_for('list_estoque'))
    return render_template('add_estoque.html')

# Rota para editar um item do estoque
@app.route('/estoque/editar/<int:id>', methods=['GET', 'POST'])
def edit_estoque(id):
    item = Estoque.query.get_or_404(id)
    if request.method == 'POST':
        item.quantidade = request.form['quantidade']
        item.veiculos_id = request.form['veiculos_id']
        item.galpao_id = request.form['galpao_id']
        db.session.commit()
        return redirect(url_for('list_estoque'))
    return render_template('edit_estoque.html', item=item)

# Rota para deletar um item do estoque
@app.route('/estoque/deletar/<int:id>', methods=['POST'])
def delete_estoque(id):
    item = Estoque.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('list_estoque'))

# Rota para listar galpão
@app.route('/galpao', methods=['GET'])
def list_galpao():
    galpoes = Galpao.query.all()
    return render_template('list_galpao.html', galpoes=galpoes)

# Rota para adicionar um galpão
@app.route('/galpao/adicionar', methods=['GET', 'POST'])
def add_galpao():
    if request.method == 'POST':
        unidade = request.form['unidade']
        novo_galpao = Galpao(unidade=unidade)
        db.session.add(novo_galpao)
        db.session.commit()
        return redirect(url_for('list_galpao'))
    return render_template('add_galpao.html')

# Rota para editar um galpão
@app.route('/galpao/editar/<int:id>', methods=['GET', 'POST'])
def edit_galpao(id):
    galpao = Galpao.query.get_or_404(id)
    if request.method == 'POST':
        galpao.unidade = request.form['unidade']
        db.session.commit()
        return redirect(url_for('list_galpao'))
    return render_template('edit_galpao.html', galpao=galpao)

# Rota para deletar um galpão
@app.route('/galpao/deletar/<int:id>', methods=['POST'])
def delete_galpao(id):
    galpao = Galpao.query.get_or_404(id)
    db.session.delete(galpao)
    db.session.commit()
    return redirect(url_for('list_galpao'))

# Rota para listar financiamentos
@app.route('/financiamentos', methods=['GET'])
def list_financiamentos():
    financiamentos = Financiamento.query.all()
    return render_template('list_financiamentos.html', financiamentos=financiamentos)

# Rota para adicionar um financiamento
@app.route('/financiamentos/adicionar', methods=['GET', 'POST'])
def add_financiamento():
    if request.method == 'POST':
        valor_total = request.form['valor_total']
        situacao_financiamento_id = request.form['situacao_financiamento_id']
        vendas_id = request.form['vendas_id']
        novo_financiamento = Financiamento(valor_total=valor_total, situacao_financiamento_id=situacao_financiamento_id, vendas_id=vendas_id)
        db.session.add(novo_financiamento)
        db.session.commit()
        return redirect(url_for('list_financiamentos'))
    return render_template('add_financiamento.html')

# Rota para editar um financiamento
@app.route('/financiamentos/editar/<int:id>', methods=['GET', 'POST'])
def edit_financiamento(id):
    financiamento = Financiamento.query.get_or_404(id)
    if request.method == 'POST':
        financiamento.valor_total = request.form['valor_total']
        financiamento.situacao_financiamento_id = request.form['situacao_financiamento_id']
        financiamento.vendas_id = request.form['vendas_id']
        db.session.commit()
        return redirect(url_for('list_financiamentos'))
    return render_template('edit_financiamento.html', financiamento=financiamento)

# Rota para deletar um financiamento
@app.route('/financiamentos/deletar/<int:id>', methods=['POST'])
def delete_financiamento(id):
    financiamento = Financiamento.query.get_or_404(id)
    db.session.delete(financiamento)
    db.session.commit()
    return redirect(url_for('list_financiamentos'))

# Rota para listar situação de financiamento
@app.route('/situacao_financiamento', methods=['GET'])
def list_situacao_financiamento():
    situacoes = SituacaoFinanciamento.query.all()
    return render_template('list_situacao_financiamento.html', situacoes=situacoes)

# Rota para adicionar uma situação de financiamento
@app.route('/situacao_financiamento/adicionar', methods=['GET', 'POST'])
def add_situacao_financiamento():
    if request.method == 'POST':
        descricao = request.form['descricao']
        nova_situacao = SituacaoFinanciamento(descricao=descricao)
        db.session.add(nova_situacao)
        db.session.commit()
        return redirect(url_for('list_situacao_financiamento'))
    return render_template('add_situacao_financiamento.html')

# Rota para editar uma situação de financiamento
@app.route('/situacao_financiamento/editar/<int:id>', methods=['GET', 'POST'])
def edit_situacao_financiamento(id):
    situacao = SituacaoFinanciamento.query.get_or_404(id)
    if request.method == 'POST':
        situacao.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('list_situacao_financiamento'))
    return render_template('edit_situacao_financiamento.html', situacao=situacao)

# Rota para deletar uma situação de financiamento
@app.route('/situacao_financiamento/deletar/<int:id>', methods=['POST'])
def delete_situacao_financiamento(id):
    situacao = SituacaoFinanciamento.query.get_or_404(id)
    db.session.delete(situacao)
    db.session.commit()
    return redirect(url_for('list_situacao_financiamento'))

if __name__ == '__main__':
    app.run(debug=True)
