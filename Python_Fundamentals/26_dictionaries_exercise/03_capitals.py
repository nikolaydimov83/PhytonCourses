country_list=input().split(', ')
capital_list=input().split(', ')

dictionary={country_capital[0]:country_capital[1] for country_capital in list(zip(country_list,capital_list))}

for key, value in dictionary.items():
    print(f"{key} -> {value}")