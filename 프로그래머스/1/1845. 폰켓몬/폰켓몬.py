def solution(nums):
    unique_pokemon = len(set(nums))
    max_pokemon_to_take = len(nums) // 2
    return min(unique_pokemon, max_pokemon_to_take)

# 예시
nums = [3, 1, 2, 3]
print(solution(nums))  # 결과는 2
