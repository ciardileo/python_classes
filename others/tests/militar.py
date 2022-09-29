#Variaveis
nas = int(input('Em que ano você nasceu? '))
nas2 = nas+18

#Resposta
if nas2>2022:
    falt = nas2-2022
    print(f'Você deverá se alistar daqui {falt} anos')
elif nas2==2022:
    print(f'Você deve se alistar esse ano! Prepare-se para ficar calvo!')
elif nas<2022:
    falt = nas2-2022
    print(f'Você deveria ter se alistado a {falt} anos')
    
