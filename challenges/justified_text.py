'''
Hacer un programa en python que "justifique" un texto con fuente monoespaciada.
no usar ninguna librería, solo Python puro

### Input
- Un string de una sola linea
- El ancho de la línea esperada
- Ninguna palabra del string será más larga que el ancho de línea esperado.

### Output
Mostrar por standard output el texto justificado, de acuerdo a las siguientes reglas:
- Use espacios para separar las palabras
- Cada línea deberá contener la mayor cantidad de palabras posibles
- Usar \n para separar líneas
- El máximo y el mínimo gap de una misma fila no puede diferir en más de 1 espacio
    - Incorrecto: Lorem-----ipsum--dolor
    - Correcto: Lorem----ipsum---dolor
- Las líneas deberán terminar en una palabra, no un espacio
- '\n' no está incluido en el largo de una línea
- Espacios más largos van primero, luego los espacios más pequeños.
    - Correcto: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 espacios).
    - Incorrecto: 'Lorem--ipsum--dolor---sit---amet' (2, 2, 3, 3 espacios).
- La última línea no estará justificada, sólo un espacio entre palabras
- Líneas con una sola palabra larga no necesitan espacios ('unapalabralarga\n').

## Ejemplo:
    ### Input:
    Texto: La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera.
    Largo de la línea: 30

### Output:

    ```
    La  historia de la ópera tiene
    una   duración   relativamente
    corta  dentro  del contexto de
    la  historia  de  la música en
    general   apareció   en  1597,
    fecha   en   que  se  creó  la
    primera ópera.
    ```
'''

# usefull methods
def get_lenght(words: list, spacer: str):
    words_lenght = sum([len(w) for w in words])
    spacers_lenght = len(spacer) * ((len(words) - 1) or 1)
    return  words_lenght + spacers_lenght

def is_next_word_fitting(actual_words: list, new_word: str, spacing: str, expected_lenght: int):
    future_lenght = get_lenght(actual_words, spacing) + len(new_word + spacing)
    return future_lenght <= expected_lenght

def is_line_valid(actual_words: list, spacer: str, expected_lenght: int):
    min_lenght = get_lenght(actual_words, spacer)
    max_lenght = get_lenght(actual_words, spacer + ' ')
    return min_lenght <= expected_lenght and max_lenght > expected_lenght

def create_line(actual_words: list, spacer: str, expected_lenght: int):
    final_line = spacer.join(actual_words)
    if spacer in final_line:
        idx = 0
        while len(final_line) < expected_lenght:
            letter = final_line[idx]
            if letter == ' ' and not final_line[idx+1] == ' ':
                final_line = final_line[:idx] + ' ' + final_line[idx:]
                idx += 1
            idx += 1
            if idx + 1 > len(final_line):
                idx = 0
    return final_line + '\n'


# brute script
if __name__ == '__main__':
    expected_lenght =  int(input("Define max line lenght: ") or 30)
    text = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general apareció en 1597, fecha en que se creó la primera ópera."
    print(f"Processing with {expected_lenght} max lenght...")

    spacer = ' '
    actual_words = []
    output_text = ''
    remaining_words = text.split(' ')
    while remaining_words:
        if is_next_word_fitting(actual_words, remaining_words[0], spacer, expected_lenght):
            word = remaining_words[0]
            remaining_words = remaining_words[1:]
            if actual_words:
                print(f"Appending: '{word}' to: {spacer.join(actual_words)}")
            actual_words.append(word)

        elif is_line_valid(actual_words, spacer, expected_lenght):
            print(f"Valid line found with words: {actual_words} using spacer: {len(spacer)}\n")
            output_text += create_line(actual_words, spacer, expected_lenght)
            actual_words = []
            spacer = ' '

        elif get_lenght(actual_words, spacer + ' ') <= expected_lenght:
            print(f"Increasing spacer to {len(spacer)} for {actual_words}, next word was: {remaining_words[0]}")
            spacer += ' '

        else:
            print(f"Too long combination, going one word backward...")
            spacer = spacer[:-1]
            word = actual_words.pop()
            remaining_words = [word] + remaining_words

    output_text += ' '.join(actual_words)
    print(f"\nFinal result:\n{output_text}")
