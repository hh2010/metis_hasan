def donuts(count):
    return 'Number of donuts: ' + ('many' if count>=10 else str(count))

# Examples
print donuts(5)
print donuts(10)
print donuts(15)

def both_ends(s):
    return (s[:2] + s[-2] + s[-1]) if len(s) > 2 else "\"\""

# Examples
print both_ends('spring')
print both_ends('Hello')
print both_ends('a')
print both_ends('xyz')

def fix_start(s):
    return (s[0] + s[1:].replace(s[0], '*'))


# Examples
print fix_start('babble')
print fix_start('aardvark')
print fix_start('google')
print fix_start('donut')


def mix_up(a, b):
    return ((b[:2] + a[-(len(a)-2):]) + " " + (a[:2] + b[-(len(b)-2):]))

# Examples
print mix_up('mix', 'pod')
print mix_up('dog', 'dinner')
print mix_up('gnash', 'sport')
print mix_up('pezzy', 'firm')

def verbing(s):
    if s[-3:] == 'ing': return (s + 'ly')
    return ((s + 'ing') if len(s) >= 3 else s)

print verbing('hail')
print verbing('swiming')
print verbing('do')

def not_bad(s):
    EOS = ['!', '.', '?']
    s_new = (s[:len(s)-1] if s[-1] in EOS else s)
    if 'not' and 'bad' in s_new.split(): a = s_new.split()
    else: return s
    if a.index('bad') > a.index('not'):
        a[a.index('not'):(a.index('bad')+1)] = ['good']
        if s[-1] in EOS: a[-1] = a[-1] + s[-1]
        return " ".join(a)
    else: return s

# Examples
print not_bad('This movie is not so bad')
print not_bad('This dinner is not that bad!')
print not_bad('This tea is not hot')
print not_bad("It's bad yet not")

def front_back(a, b):
    a_f = a[:int(round((len(a)/2.0),0))]
    a_b = a[-int(round(len(a)/2.0,0))+1:]
    b_f = b[:int(round((len(b)/2.0),0))]
    b_b = b[-int(round(len(b)/2.0,0))+1:]
    return (a_f + b_f + a_b + b_b)

# Examples
print round((len('xyz')/2),0)
print round((len('xyz')/2.0),0)
print front_back('abcd', 'xy')
print front_back('abcde', 'xyz')
print front_back('Kitten', 'Donut')
