def render_bar(number):
    #30% [%%%.......]
    if number<100:
        return f"{number}% [{int(number/10)*'%'}{(10-(int(number/10)))*'.'}]\nStill loading..."
    else:
        return f"100% Complete!\n[%%%%%%%%%%]"
    
print(render_bar(int(input())))