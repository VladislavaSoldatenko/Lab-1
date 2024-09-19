def draw_line(offset=0, length=1):
    line = ' ' * length
    print(f'{' * offset}\x1b[48;5;222m{line}\x1b[0m')



def romb():
    height = 30
    offset = 15


    for line in range(height):
        draw line(length=10)
    

if _name_ == '_main_':
    romb()