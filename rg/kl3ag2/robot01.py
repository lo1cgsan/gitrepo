#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rg


class Robot:

    def act(self, game):

        def czy_wejscie(poz):
            if 'spawn' in rg.loc_types(poz):
                return True
            return False
        # rg.loc_types – zwraca typ pola, np.: spawn, normal, obstacle, invalid

        def czy_wrog(poz):
            if game.robots.get(poz) is not None:
                if game.robots[poz].player_id != self.player_id:
                    return True
            return False

        # print(game.robots)

        print(rg.locs_around(self.location))

        lista_wrogow = []  # wrogowie wokół nas

        for poz, robot in game.robots.iteritems():
            if robot.player_id != self.player_id:
                # if rg.dist(poz, self.location) <= 1:
                lista_wrogow.append(poz)
                # return ['attack', poz]
        # rg.dist()

        wrogowie_obok = []
        for poz in rg.locs_around(self.location):
            if czy_wrog(poz):
                wrogowie_obok.append(poz)

        if len(wrogowie_obok) > 2 and self.hp < 27:
            return ['suicide']
        elif len(wrogowie_obok):
            return ['attack', lista_wrogow[0]]

        if self.location == rg.CENTER_POINT:
            return ['suicide']

        # idź do środka planszy, ruch domyślny
        # print(rg.toward(self.location, rg.CENTER_POINT))
        if czy_wejscie(self.location):
            return ['move', rg.toward(self.location, rg.CENTER_POINT)]
        # rg.CENTER_POINT – środek planszy
        # self.location – położenie robota
        # rg.toward – wyznacza najkrótszą drogę do podanego punktu
