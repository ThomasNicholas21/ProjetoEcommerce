from django.core.exceptions import ValidationError

def cpf_validator(cpf):
    if len(cpf) != 11:
        raise ValidationError('O CPF deve ter 11 dígitos')

    if cpf == cpf[::-1]:
        raise ValidationError(f'O CPF {cpf} é inválido')
    
    new_cpf1 = cpf[:9]
    new_cpf2 = new_cpf1 + str(evaluator1(new_cpf1))
    new_cpf3 = new_cpf2 + str(evaluator2(new_cpf2))

    if new_cpf3 != cpf:
        raise ValidationError(f'O CPF {cpf} é inválido')
    
def evaluator1(args):
    total = 0
    reverse = 10
    for i in args:
        total += int(i) * reverse
        reverse -= 1
    
    digit = (total * 10) % 11
    digit = digit if digit <= 9 else 0
    return digit

def evaluator2(args):
    total = 0
    reverse = 11
    for i in args:
        total += int(i) * reverse
        reverse -= 1
    
    digit = (total * 10) % 11
    digit = digit if digit <= 9 else 0
    return digit
