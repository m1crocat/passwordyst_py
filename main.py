from random import randint

print("Passwordyst Python is a generator passwords! \n Copyright (C) 2024 m1crocat & Rodion Mern\n\n This program is free software: you can redistribute it and/or modify\n it under the terms of the GNU General Public License as published by\n the Free Software Foundation, either version 3 of the License, or\n (at your option) any later version.\n\n This program is distributed in the hope that it will be useful,\n MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n GNU General Public License for more details.\n\n You should have received a copy of the GNU General Public License\n along with this program.  If not, see <https://www.gnu.org/licenses/>.\n")

alph = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"@#$%^&*'
pass1 = ""

passLength = int(input(" Value symbols of password? \n "))
for i in range(passLength):
            pass1 += alph[randint(0, len(alph)-1)]

print(" Your pass is: ", pass1)
