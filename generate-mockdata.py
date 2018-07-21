p1 = (8.711647, 49.413287) # parkingspot1 (picked from google maps)
p2 = (8.711660, 49.413250) # parkingspot2 (picked from google maps)

# asume same distance between parking spots and straight road
def next(p1, p2):
    return (p2[0] + p2[0] - p1[0], p2[1] + p2[1] - p1[1])

start_point = p1
end_point = p2
for i in range(18):
    new_point = next(start_point, end_point)
    start_point = end_point
    end_point = new_point
    print('{{"type": "Feature","properties":{{"id": "parkingspot{}"}},"geometry":{{"type": "Point", "coordinates": [{}, {}]}}}},'.format(i+3, new_point[0], new_point[1]))


