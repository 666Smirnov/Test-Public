from api import PetFriends
from settings import email_valid, password_valid

pf = PetFriends()

def test_get_api_key_for_valid_user(email=email_valid, password=password_valid):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_photo_valid_data(name='Цыпа', animal_type='Хедкраб',
                                     age='4', pet_photo='C:\PycharmProjects\Pet_Friends\cypa.jpg'):
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_add_new_pet_without_photo_valid_data(name='Цыпа', animal_type='Хедкраб', age='4'):
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    status, result = pf.post_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_successful_update_self_pet_info(name='Мурзик',
                                         animal_type='Котэ', age='5'):
   _, auth_key = pf.get_api_key(email_valid, password_valid)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
   if len(my_pets['pets']) > 0:
       status, result = pf.put_update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
       assert status == 200
       assert result['name'] == name
       assert result['animal_type'] == animal_type
       assert result['age'] == age
   else:
       raise Exception("There is no my pets")

def test_successful_delete_first_pet():
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        old_pets = len(my_pets['pets'])
        status, result = pf.put_delete_pet(auth_key, my_pets['pets'][0]['id'])
        assert status == 200
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert old_pets == len(my_pets['pets'])
    else:
        raise Exception("No pets")

def test_successful_add_photo_first_pet(pet_photo='C:\PycharmProjects\Pet_Friends\Josef.jpg'):
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.post_add_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
        assert status == 200
    else:
        raise Exception("No pets")

def test_invalid_email(email='666@omen.hell'):
    status, auth_key = pf.get_api_key(email, password_valid)
    assert status == 403
def test_invalid_pass(password='satan'):
    status, auth_key = pf.get_api_key(email_valid, password)
    assert status == 403

def test_invalid_auth_key(auth_key={'key':'666'}):
    status, result = pf.get_list_of_pets(auth_key, filter='')
    assert status == 403
def test_add_new_pet_with_photo_invalid_data(name='12345678!@#$$%^&', animal_type='Demon6666666666666666666666666666666666666',
                                     age='100000000000000000000000000000', pet_photo='C:\PycharmProjects\Pet_Friends\Josef.jpg'):
    _, auth_key = pf.get_api_key(email_valid, password_valid)
    status, result = pf.post_api_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 403
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
