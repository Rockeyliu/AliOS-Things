src     = Split('''
        board.c
''')

component = aos_board_component('board_esp8266', 'esp8266', src)

linux_only_targets="helloworld"
platform_options="wifi=1"
