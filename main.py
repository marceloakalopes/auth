from logic import *;
from ui import *;   

def app():

        print("\nSelect one option: \n")
        print("1. Register")
        print("2. Login")
        print("3. Quit \n")

        try:
            res = int(get_user_input("Insert a number between 1-3: "))
            if res not in [1,2,3]:
                print("Invalid number")
                raise Exception()
        except:
            res = int(get_user_input("Insert a number between 1-3: "))

        match res:
            case 1:
                print("\nRegister\n")
                registered = False
                while not registered:
                    crendentials = get_crendentials()
                    registered = register(crendentials['username'], crendentials['password'])
                    if registered:
                        print("Successfully registered")
            case 2:
                cred = get_crendentials_login()
                login(cred['username'], cred['password'])

            case 3:
                exit()
    


app()