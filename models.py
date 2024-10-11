# models.py
from flask_sqlalchemy import SQLAlchemy

# Crie a instância do SQLAlchemy aqui
db = SQLAlchemy()


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)  # Tamanho ajustado para CPF
    telefone = db.Column(db.String(15), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)  # Tamanho ajustado para endereço
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Cliente {self.nome}>'


class Veiculo(db.Model):
    __tablename__ = 'veiculos'
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.String(10), nullable=False)
    cor = db.Column(db.String(20))
    placa = db.Column(db.String(15), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Veiculo {self.modelo}>'


class Funcionario(db.Model):
    __tablename__ = 'funcionarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)  # Tamanho ajustado para CPF
    telefone = db.Column(db.String(20), nullable=False)
    endereco = db.Column(db.String(50), nullable=False)
    perfil_cargo_id = db.Column(db.Integer, db.ForeignKey('perfis_cargos.id'))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Funcionario {self.nome}>'


class Venda(db.Model):
    __tablename__ = 'vendas'
    id = db.Column(db.Integer, primary_key=True)
    qtd_vendas = db.Column(db.Integer, nullable=False)
    veiculos_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'))
    clientes_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    funcionarios_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Venda ID: {self.id}>'


class PerfilCargo(db.Model):
    __tablename__ = 'perfis_cargos'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<PerfilCargo {self.tipo}>'


class TesteDrive(db.Model):
    __tablename__ = 'teste_drive'
    id = db.Column(db.Integer, primary_key=True)
    agendamento = db.Column(db.DateTime)
    clientes_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    veiculos_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<TesteDrive ID: {self.id}>'


class Estoque(db.Model):
    __tablename__ = 'estoque'
    id = db.Column(db.Integer, primary_key=True)
    quantidade = db.Column(db.Integer, nullable=False)
    veiculos_id = db.Column(db.Integer, db.ForeignKey('veiculos.id'))
    galpao_id = db.Column(db.Integer, db.ForeignKey('galpoes.id'))  # Ajustado para galpoes
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Estoque ID: {self.id}>'


class Galpao(db.Model):
    __tablename__ = 'galpoes'  # Ajustado para plural
    id = db.Column(db.Integer, primary_key=True)
    unidade = db.Column(db.String(20))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Galpao {self.unidade}>'


class Financiamento(db.Model):
    __tablename__ = 'financiamentos'
    id = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)
    situacao_financiamento_id = db.Column(db.Integer, db.ForeignKey('situacao_financiamento.id'))
    vendas_id = db.Column(db.Integer, db.ForeignKey('vendas.id'))

    def __repr__(self):
        return f'<Financiamento ID: {self.id}>'


class SituacaoFinanciamento(db.Model):
    __tablename__ = 'situacao_financiamento'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50))
    data_criacao = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<SituacaoFinanciamento {self.descricao}>'
