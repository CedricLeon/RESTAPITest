########################################
# Test file to send request to the API #
########################################
#import pickle
from adapter import *

BASE = "http://127.0.0.1:5000/"

# --- Adapter test ---
# adapter = Adapter()
# print(f"{bcolors.HEADER}DELETE Test:{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}Reward = {adapter.inputToEndpoint((0.79, 0.10), 1)}{bcolors.ENDC}")
#
# print(f"{bcolors.HEADER}\nPUT Test:{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}Reward = {adapter.inputToEndpoint((0.29, 0.10), 1)}{bcolors.ENDC}")
#
# print(f"{bcolors.HEADER}\nPATCH Test:{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}Reward = {adapter.inputToEndpoint((0.59, 0.10), 1)}{bcolors.ENDC}")
#
# print(f"{bcolors.HEADER}\nGET Test:{bcolors.ENDC}")
# print(f"{bcolors.OKGREEN}Reward = {adapter.inputToEndpoint((0.09, 0.10), 0)}{bcolors.ENDC}")

db_size = 100
print(f"Print whole database (until client N°{db_size}):")
for i in range(0, db_size):
    response = requests.get(BASE + "client/" + str(i))
    print(response.json())

#pickle.Unpickler("./stgem/mo3k_python_results.pickle").load()
