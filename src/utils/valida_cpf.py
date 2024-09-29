from .constants import INVALID_CPF


def valida_cpf(cpf):
  if len(cpf) == 11 and cpf.isdigit():
    return True
  else:
    print(INVALID_CPF)
    return False