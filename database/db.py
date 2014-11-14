# -*- coding: utf-8 -*-

import dataset
import os

db = dataset.connect('sqlite:///database/cadastro.db')
inscricoes = db['inscricoes']