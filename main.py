from Classes.LinkedList import LinkedList


def main():
    linked = LinkedList(1)
    linked.listBuilder([3, 5, 2, 3, 3, 2, 10])
    linked.removeDups()

    print(linked)


main()
