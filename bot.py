import wealthsimple as ws

with open('credentials', 'r') as cred:
    lines = list(l.replace('\n', '') for l in cred.readlines())
    trader = ws.WSTrade(lines[0], lines[1])

trader.get_account