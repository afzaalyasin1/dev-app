from dev2il_devops_app.mountains import highest_mountain

def test_highest_mountain():
    mountains = [
        {'name': 'k2', 'height': 1245},
        {'name': 'Gr. Priel', 'height': 2515},
        {'name': 'Schermberg', 'height': 2396}
    ]
    
    
    assert highest_mountain(mountains) == {'name': 'Gr. Priel', 'height': 2515}