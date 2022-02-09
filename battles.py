def pokemon_battle(pokemon1, pokemon2):
    # who go first
    while(pokemon1.stats[3] > 0 or pokemon2.stats[3] > 0):
        if pokemon1.stats[2] > pokemon2.stats[2]:
            pokemon1.fight(pokemon2)
            pokemon2.fight(pokemon1) 
        else:
            pokemon2.fight(pokemon1)
            pokemon1.fight(pokemon2)             
        print(pokemon1.name + " has " + str(pokemon1.stats[3]) + " hp left!")
        print(pokemon2.name + " has " + str(pokemon2.stats[3]) + " hp left!")

