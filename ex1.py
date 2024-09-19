new_msg = []

while True:
    msg = """*! p@p@! n*&l
&st& @n* &# g*st@r!@ d& g@nh@r #m c*mp#t@d*r p@r@ p*d&r @pr&nd&r @ pr*gr@m@r p@r@ p*d&r @j#d@r * s&nh*r @ r&s*lv&r * &n!gm@ d@ m!nh@ c@rt!nh@ n* @n* q#& v&m
&sp&r* q#& * s&nh*r t&nh@ g*st@d* d* m&# d&s@f!*
f&l!z n@t@l """
    if (len(msg) < 5 or len(msg) > 256):
        break 
    for i in range(len(msg)):
        #print(i)
        if msg[i] == "@":
            new_msg.append("a")
        elif msg[i] == "!":
            new_msg.append("i")
        elif msg[i] == "&":
            new_msg.append("e")
        elif msg[i] == "*":
            new_msg.append("o")
        elif msg [i] == "#":
            new_msg.append("u")
        else:
            new_msg.append(msg[i])
        i += 1
    break
print("".join(new_msg))u
