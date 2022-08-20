
from goto_py import goto
user = str(input('Entre com o usuário: '))
senha = str(input('Entre com a senha: '))

if user == senha:
    print("Usuário não pode ser o mesmo que a senha, entra novamente com os dados.")
    goto(2)
if user != senha:
    print('Alteração de senha feita com sucesso.')
