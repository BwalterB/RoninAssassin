import pandas as pd
import random as r
                                                                                    
welcome = input("Ronin Assassin will take you on a journey of life and death. You are a top predator operating in the shadowy world where government and organized crime intersect. Set in the most exotic and exciting cities of world you will face the challenges that are necessary to track, isolate and terminate your target, or lose your life if you fail. Are you ready to play? Type Yes to accept your mission, type no if you are too scared. ").lower()

if welcome == 'yes':
    code_name = input("You have accepted the mission. Select your code name? ")
    sex = input(f'What sex are you {code_name} ?').lower()
    weapon_of_choice = input(f"What is your weapon of choice, {code_name}? ").lower
    country_of_origin = input(f"What is your country of origin? ").lower

else:
    print("Be careful of monsters hiding under your bed.")

completed_profile = {
    'name': code_name,
    'sex': sex,
    'weapon_of_choice': weapon_of_choice,
    'country_of_origin': country_of_origin
}

assassin_profile = print(f"""Your profile is complete. \n Code Name: {code_name} \n Sex: {sex} \n Weapon of Choice: {weapon_of_choice} \n Country of Origin: {country_of_origin}. \n You have no allegience to anyone other than the one who is paying you. Your code of honor forbids you from killing or  
harming innocents. You cannot be outbid by a target once you have accepted a contract, but you will turn on anyone after you have executed a target.
You must deploy your skills of seduction, weapons, poisons, bribery, martial arts, surveillance, deception, manipulation, concealment, disguise,
languages, and computer hacking.""")

mission_profile = input(f"""You are sitting in at a street cafe in {city_of_operation} drinking espresso. Your encrypted messaging app pings you telling you that you 
have received $100,000 USD worth of Bitcoin. A photo of a man in his early 30s follows the message, your target. His current location is North, 1km away.
Type track to 
""")



