# -*- coding: utf-8 -*-
from flask import Flask, url_for, render_template, request, flash, redirect
import sqlite3 as sql
import os
from wtforms import Form, TextField, validators

DATABASE = "cadastro.db"

app = Flask(__name__)

app.debug = True
app.use_reload = True

# Config. de Chave de Segurança
app.config.from_object(__name__)
app.secret_key = 'a966f91913e180a8794f4c33c2c96d98'

class Registration(Form):
	name = TextField(u'Nome', [validators.Required(message=u'O Nome é requerido!')])
	email = TextField(u'Email', [validators.Required(message=u'O Email é requerido!'), validators.Email(message=u"Formato de email inválido!")])
	escola = TextField(u'Escola', [validators.Required(message=u'A Escola é requerida!')])
	serie = TextField(u'Série', [validators.Required(message=u'A Série é requerida!')])

def conectar():
	return sql.connect("cadastro.db")

@app.route('/', methods=['GET','POST'])
def home():

	form = Registration(request.form)
	if request.method == 'POST' and form.validate():

		name = request.form['name']
		email = request.form['email']
		escola = request.form['escola']
		serie = request.form['serie']

		db = conectar()
		cursor = db.cursor()
		try:
			cursor.execute("""INSERT INTO inscricoes(name,email,escola,serie) VALUES (?,?,?,?)""", (name, email, escola, serie))
			db.commit()
			variavel = u'Obrigado! Você foi inscrito com sucesso!'
		except:
			variavel = u'Ocorreu um erro ao gravar os dados no banco de dados!'
			db.rollback()
			form.formdata = None
		flash(variavel)
		return redirect('/')
	return render_template('testeHtmlSimple.html', form=form)

@app.route('/listaCadastros/')
def listaCadastrados():
	db = conectar()
	cursor = db.cursor()
	dados = cursor.execute("SELECT * FROM inscricoes")

	return render_template('mostrarCadastrados.html', dados=dados)

if __name__ == '__main__':
	app.run()
