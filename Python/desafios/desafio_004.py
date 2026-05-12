algo = input('Digite algo: ')

print(type(algo))
print(f'É letra? {algo.isalpha()}')
print(f'É número? {algo.isnumeric()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'É minúsculo? {algo.islower()}')
print(f'É maiúsculo? {algo.isupper()}')
print(f'É decimal? {algo.isdecimal()}')