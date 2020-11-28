def convert(number):
    sound_dict = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    sound_list = [str(number)]
    
    for i in sound_dict.keys():
        if number%i == 0:
            sound_list.append(sound_dict[i])
    
    return ''.join(sound_list)