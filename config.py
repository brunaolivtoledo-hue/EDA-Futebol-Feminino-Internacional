"""Listas de classificação usadas no notebook principal.

São decisões analíticas (não de limpeza): mudar uma lista aqui não exige rodar a limpeza de novo.
Os nomes de torneios são os já corrigidos pelo `_limpeza.ipynb`
(ex.: 'Tri-Nation Cup', 'World Cup (pre-FIFA)').
"""

# Torneios NÃO competitivos: amistosos avulsos e torneios por convite.
# Classificação por exclusão: todo torneio fora desta lista é tratado como competitivo.
# Uso: resultados['is_competitive'] = ~resultados['tournament'].isin(NAO_COMPETITIVOS)
NAO_COMPETITIVOS = {
    # amistosos avulsos
    'Friendly',
    # torneios por convite
    'Algarve Cup', 'Cyprus Cup', 'SheBelieves Cup', 'Turkish Women\'s Cup',
    'Istria Cup', 'Pinatar Cup', 'U.S. Cup', 'Aphrodite Cup', 'Four Nations Tournament',
    'International Tournament', 'Tournoi de France', 'Arnold Clark Cup', 'Tournament of Nations',
    'Yongchuan International Tournament', 'Peace Queen Cup', 'Chunghua Cup', 'Pink Ladies Cup',
    'FIFA Series', 'FIFA Unites Women\'s Series', 'Mundialito', 'Australian Cup', 'Slavic Cup',
    'MS&AD Cup', 'Kirin Challenge Cup', 'Malta International Tournament', 'VisitMalta Women\'s Trophy',
    'Valais Women\'s Cup', 'Matchworld Women\'s Cup', 'Women\'s Revelations Cup', 'Aisha Buhari Cup',
    'MSG Prime Minister\'s Cup', 'Gold Cup India', 'Cup of Nations',
    'Armenia International Friendly Tournament', 'Caribbean Queen\'s Friendly Tournament',
    'SAFF Women\'s Friendly Tournament', 'CONCACAF Invitational Tournament',
    'FIFA Women\'s Invitation Tournament', 'International Women\'s Championship',
    'Tri-Nation Cup', 'Tri-Nations Series', 'Bangladesh Tri-Nations Cup',
    'Three Nations Tournament', 'Three Nations',
}


# Proxy de confederação: torneios organizados por cada confederação.
# Cada seleção recebe a confederação dos torneios que mais disputou.
TORNEIOS_CONFEDERACAO = {
    'UEFA': [
        'UEFA Euro', 'UEFA Euro qualification', 'Euro', 'European Championship',
        'UEFA Nations League', "UEFA Women's Nations League",
        'UEFA Olympic Qualifying Tournament', 'UEFA Olympic Qualifying play-off',
        'Nordic Championship', 'Baltic Cup'
    ],
    'AFC': [
        'AFC Asian Cup', 'AFC Asian Cup qualification', 'AFC Championship',
        'AFC Olympic Qualifying Tournament', 'AFC Olympic qualification',
        'AFF Championship', "AFF Women's Cup", 'ASEAN Championship',
        'EAFF Championship', 'EAFF E-1 Championship', 'EAFF E-1 Championship qualification',
        'EAFF East Asian Cup', 'SAFF Championship', 'WAFF Championship',
        "WAFF Women's Championship", 'CAFA Championship', 'Asian Games',
        'South Asian Games', 'Southeast Asian Games'
    ],
    'CAF': [
        'African Championship', 'African Championship qualification',
        'African Cup of Nations', 'Africa Cup of Nations qualification',
        'CAF Olympic Qualifying Tournament', 'COSAFA Championship',
        'CECAFA Championship', 'UNAF Tournament', 'UNIFFAC Cup',
        'WAFU Zone A Cup', 'WAFU Zone B Cup', 'African Games', 'Indian Ocean Island Games'
    ],
    'CONCACAF': [
        'CONCACAF Championship', 'CONCACAF Championship qualification',
        'CONCACAF Gold Cup', 'CONCACAF Gold Cup qualification',
        'CONCACAF Olympic Qualifying Tournament', 'CONCACAF Olympic Qualifying Tournament qualification',
        'CONCACAF Pre-Olympic Tournament', 'CONCACAF Pre-Olympic Tournament qualification',
        'CONCACAF Invitational Tournament', 'Central American Games', 'Windward Islands Tournament'
    ],
    'CONMEBOL': ['Copa América', 'CONMEBOL Nations League'],
    'OFC': [
        'OFC Championship', 'OFC Nations Cup', 'OFC Nations Cup qualification',
        'OFC Olympic Qualifying Tournament', 'Pacific Games'
    ]
}