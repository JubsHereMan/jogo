andarilho = {
    'nome': 'Andarilho',
    'nivel': 1,
    'vida': 20,
    'dano': 4,
    'defesa': 2,
    'agilidade': 3,
    'habilidade_especial': 'Ataque Rápido',  # Pode atacar duas vezes em um turno
    'descricao': 'Um viajante sombrio que ataca furtivamente com rapidez.'
}

urso = {
    'nome': 'Urso',
    'nivel': 1,
    'vida': 35,
    'dano': 6,
    'habilidade_especial': 'Investida',  # Pode causar dano extra em um único ataque
    'descricao': 'Um urso poderoso com uma força bruta capaz de esmagar seus inimigos.'
}

mortovivo = {
    'nome': 'Mortovivo',
    'nivel': 1,
    'vida': 25,
    'dano': 3,
    'agilidade': 2,
    'habilidade_especial': 'Regeneração',  # Regenera um pouco de vida a cada turno
    'descricao': 'Uma criatura reanimada que pode se curar lentamente enquanto luta.'
}

corrupitor={
    'nome': 'Corrupitor',
    'nivel': 2,
    'vida': 30,
    'dano': 9,
    'habilidade_especial':'corromper',
    'descricao':'um ser terrivel que plorifera um tipo de doença capaz de infectar tudo e todos ao seu redor'
}


inimigosFloresta=[andarilho, mortovivo,urso]
bossFloresta=[corrupitor]