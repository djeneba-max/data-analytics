room_length = 12
room_width = 10

room_area = room_length*room_width
print(f'The area of the room is: {room_area}.')

tile_area = 1*1
tiles_needed = room_area/tile_area

print(f'The number of tiles needed is: {tiles_needed}.')

boxes_needed = tiles_needed / 12
print(f"Boxes needed: {boxes_needed}")

total_tiles = tiles_needed + tiles_needed*0.1
total_boxes = total_tiles/ 12

print(f"Total boxes: {total_boxes}")