# conversão de tipos, coerção
# str, int, float, bool
print(int('100')+100) #200
print(float('10.0')+10) #20.0
print('x'+'y'+'z') #xyz
print(int('2025'), type(int('2025'))) #2025 <class 'int'>
print(type(float('2520') + 2520)) #<class 'float'>
print(bool(' ')) #True
print(str(2000) + 'a') #2000a
#print('1' + 1) o Python não concatena int com string dessa forma.
