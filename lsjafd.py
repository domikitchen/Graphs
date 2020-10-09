arr = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def thing(arr):
    for i in arr:
        if isinstance(i, list):
            thing(i)
        else:
            print(i)

thing(arr)
