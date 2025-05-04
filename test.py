from ipeaindices import get_ipca, get_incc, get_igpm

# Últimos valores
get_ipca()
get_incc()
get_igpm()

# Valores mensais de 2024
get_igpm(2024)

# Média de 2024
get_igpm(2024, average=True)

# Média de 2023 e 2025
get_igpm([2023, 2025], average=True)
