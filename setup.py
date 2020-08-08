import cx_Freeze

executables = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name = "SPACE INVADING",
    options = {"build_exe": {"packages": ["pygame"], "include_files": ['background1.jpg', 'background2.jpg', 'player1.png', 'player2.png', 'bullet1.png', 'bulletsound.wav', 'enemy.png', 'enemy1.png', 'explosionsound.wav', 'sp.png', 'sp1.png', 'sp2.png', 'ufo.png', 'ufo2.png', 'ufoicon.png', 'ufoicon2.png'] }},
    executables = executables
)