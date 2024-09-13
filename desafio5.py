def inverte_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string_original = input("Informe uma string: ")
print("String invertida:", inverte_string(string_original))
