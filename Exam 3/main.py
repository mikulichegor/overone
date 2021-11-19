from Tomato import Tomato
from TomatoBush import TomatoBush
from Gardener import Gardener

if __name__ == '__main__':

    Gardener.knowledge_base()
    tomatoBush = TomatoBush(5)
    gardener = Gardener('John')

    print("Tomatoes before gardener's work:")
    for i in tomatoBush.tomatoes:
        print(i.show_ripe())

    gardener.work(tomatoBush.tomatoes[1])
    gardener.work(tomatoBush.tomatoes[3])

    print("\nTomatoes after gardener's work:")
    for i in tomatoBush.tomatoes:
        print(i.show_ripe())

    print("\nTrying to harvest:")
    gardener.harvest(tomatoBush)

    tomatoBush.grow_all()
    tomatoBush.grow_all()
    print("\nTomatoes after growing all:")
    for i in tomatoBush.tomatoes:
        print(i.show_ripe())
    gardener.harvest(tomatoBush)
