import matplotlib.pyplot as plt
import random


class Population:
    nb_bad = 1
    nb_nice = 1
    FOOD = 200
    total = nb_bad + nb_nice
    bad = nb_bad
    nice = nb_nice
    food = FOOD

    def no_food(self):
        for n in range(Population.nice + 1):
            Population.nb_nice -= 1 if n > 0 else 0
        for n in range(Population.bad + 1):
            Population.nb_bad -= 1 if n > 0 else 0
        Population.nice = 0
        Population.bad = 0


class Bad(Population):

    def reproduce(self):
        type_of_people = random.randint(0, 1)
        if type_of_people == 1:
            Population.nb_bad += 1

    def eat(self):
        self.food_share()
        Population.bad -= 1
        Population.food -= 1

        if Population.food == 0:
            self.no_food()

        if not self.food_share():
            Population.nb_bad += 1
            return True

        else:
            proba_bad = [0 for x in range(Population.bad+1)]
            proba_nice = [1 for x in range(Population.nice+1)]
            proba_total = proba_bad + proba_nice
            # print(Population.nice)
            # print(Population.bad)
            # print(proba_total)
            share_with = random.choice(proba_total)

            if share_with == 0:  # must share with bad
                Population.nb_bad -= 2
                Population.bad -= 1
                return True
            else:  # must share with nice
                self.reproduce()
                Population.nice -= 1
                c = Nice()
                c.die()

    def food_share(self):

        proba = int((Population.bad + Population.nice)*Population.FOOD/100)  # proba to share in %
        proba_list = [0 for x in range(proba+1)]  # add proba to share
        # print(proba_list)
        for n in range(101 - proba):
            if n >= 0:
                proba_list.append(1)  # add proba to not share

        share_or_not = random.choice(proba_list)  # make the choice
        if share_or_not == 0:
            return True  # must share

        return False  # mustn't share

    def die(self):
        die_or_survive = random.randint(0, 1)
        if die_or_survive == 1:
            Population.nb_bad -= 1  # die


class Nice(Population):

    def reproduce(self):
        type_of_people = random.randint(0, 1)
        if type_of_people == 1:
            Population.nb_nice += 1
            return True  # reproduce worked
        return False  # reproduce didn't work

    def eat(self):
        Population.nice -= 1
        Population.food -= 1

        if Population.food == 0:
            self.no_food()

        if not self.food_share():
            Population.nb_nice += 1  # if mustn't share -> reproduce
            return True

        else:
            proba_bad = [0 for x in range(Population.bad+1)]
            proba_nice = [1 for x in range(Population.nice+1)]
            proba_total = proba_bad + proba_nice
            share_with = random.choice(proba_total)
            # print(Population.nice)
            # print(Population.bad)
            # print(proba_total)

            if share_with == 0:  # must share with bad
                self.die()
                Population.bad -= 1
                d = Bad()
                d.reproduce()
            else:
                Population.nice -= 1
                return False  # must share with nice

    def food_share(self):
        proba = int((Population.bad + Population.nice)/Population.FOOD*100)  # proba to share in %
        proba_list = [0 for x in range(proba+1)]
        for n in range(101 - proba):
            if n >= 0:
                proba_list.append(1)  # add proba to not share
        # print(proba_list)

        share_or_not = random.choice(proba_list)  # make the choice
        if share_or_not == 0:
            return True  # must share

        return False  # mustn't share

    def die(self):
        die_or_survive = random.randint(0, 1)
        if die_or_survive == 1:
            Population.nb_nice -= 1  # die


a = Nice()
b = Bad()

# set the data
Day = list()
Inhabitants_nice = list()
Inhabitants_bad = list()
Total = list()

for n in range(100):
    # update the data
    Day.extend(f'Day {n}')
    Inhabitants_nice.append(Population.nb_nice)
    Inhabitants_bad.append(Population.nb_bad)
    Total.append(Population.total)

    Population.bad = Population.nb_bad
    Population.nice = Population.nb_nice

    for n in range(Population.bad + Population.nice + 1):
        if Population.nice > 0 and Population.bad > 0:
            a.eat()
            b.eat()
            print('a')
            continue
        elif Population.nice > 0:
            a.eat()
            print('b')
            continue
        elif Population.bad > 0:
            b.eat()
            print('c')
            continue
        else:
            break

    Population.food = Population.FOOD
    Population.total = Population.nb_nice + Population.nb_bad

fig, ax = plt.subplots()
ax.set(xlim=(0, 100), ylim=(0, Population.food*2))
ax.plot(Inhabitants_nice, label='Nice')
ax.plot(Inhabitants_bad, label='Hawk')
ax.plot(Total, label='Sum')
ax.set_xlabel('NUmber of day')
ax.set_ylabel('Inhabitants')
ax.set_title("Simulation of aggression")
ax.legend()
plt.show()
