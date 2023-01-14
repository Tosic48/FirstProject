things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
sorted_values = sorted(things.values())
print(sorted_values)
# weight = int(input()) * 1000
#
# answer = []
# for i in things.values():
#     print(i)

#     if weight - i >= 0:
#         weight -= i
#         answer += sort_things[i] + ' '
#     elif weight - i < 0:
#         continue
#
# print(answer)