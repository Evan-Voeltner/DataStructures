def find_pi_day():
    months = ('January','Febuary','March','April','May','June','July','August','September','October','November','December')
    pi_day = 3.14
    print(months[int(pi_day)-1])


def store_fruits_and_vegggies():
    fruits_and_veggies = {"Carrots","Onions","Apples","Grapes","Pineapple"}
    fruits_and_veggies.update({'Pears','Oranges','Cellery','Peas'})
    for food in fruits_and_veggies:
        print(food)

def store_user_info():
    user_profile = {
        'first_name' : 'Jed',
        'last_name' : 'Bed',
        'email' : 'JedBed2000@yahoo.com',
        'phone_number' : '414-555-6548'

    }
    print(f'{user_profile.get("first_name")} | {user_profile.get("last_name")} | {user_profile.get("email")} | {user_profile.get("phone_number")}')

def print_family_members():
    family_members = [
        {
            'first_name' : 'Marsha',
            'last_name' : 'Voeltner',
            'relation' : 'Mother'

        },
        {
            'first_name' : 'David',
            'last_name' : 'Voeltner',
            'relation' : 'Father'

        },
        {
            'first_name' : 'William',
            'last_name' : 'Voeltner',
            'relation' : 'Grandfather'

        },
        {
            'first_name' : 'Cathy',
            'last_name' : 'Romies',
            'relation' : 'Grandmother'

        },
        {
            'first_name' : 'Guy',
            'last_name' : 'Porth',
            'relation' : 'Grandfather'

        }]

    for person in family_members:
        print(f'{person.get("first_name")} is my {person.get("relation")}.')