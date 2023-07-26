from Room import Room
def main():
    closet = Room(10, 12)
    copy_room = Room(5, 10)
    rug_to_order = closet + copy_room
    print(f"We need to order {rug_to_order} sq feet of rug")

    # copy_room.add_name("Copy Room")
    # if hasattr(copy_room, 'roomName'):
    #     print("Copy Room has an extra variable")
    # print(f"closet needs {closet.get_rug_size()} sq feet of rug")
    # print(f"copy room needs {copy_room.get_rug_size()} sq feet of rug")

if __name__ == '__main__':
    main()