from logic import is_username_available

def get_user_input(input_string: str) -> str:
    try:
        user_input = input(input_string)
        return user_input

    except:
        print("Invalid input")
        get_user_input()

def get_crendentials() -> dict:
    usr = input("Type your username: ")

    psw = input("Type your password: ")

    return {"username":usr, "password":psw}
    
    
    
def get_crendentials_login() -> dict:
    usr = input("Type your username: ")

    psw = input("Type your password: ")

    return {"username":usr, "password":psw}

    