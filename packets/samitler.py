def samitleri_goster(string):
    vowels = ['a','ə','e','ı','i','o','ö','u','ü']
    result = {letter for letter in string if letter.lower() not in vowels and not letter.isdigit() }
   
    return result


