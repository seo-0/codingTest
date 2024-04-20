
nums=[]
def solution(nums):
    unique_pokemon = len(set(nums))
    max_pokemon_to_take = len(nums) // 2
    return min(unique_pokemon, max_pokemon_to_take)


print(solution(nums)) 
