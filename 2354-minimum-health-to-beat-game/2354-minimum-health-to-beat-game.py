class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # n levels in a game
        # damage  for ech level
        # armor max once at any level - reduces damage
        # constraint - health > 0
        # min health to start with to beat the game

        # clarifications
        # health is not reset after every level ?
        # yes
        # with 0 health aand more armor I cannot proceed 
        # when to use armor - optimal position
        # let's say health = 3
        # armoe = 3, damage = 2,1 -> here armor can come anytime
        # health = 2, => armor when most damage occurs
        # can we use a combo of armor and health ? yes

        # base case => armor = 0
        # sum(damages) + 1
        # regular case -
        # tot damage = 16
        # max = 7
        # 16 - armor + 1 = 13
        # ex 2 =
        # 14 - 7 + 1 = 8 is wrong
        # 14 - min (armor, maxdamage) + 1 = 10
        # 6 1 armor can be used only once so we use it on the highest damage simply
        # that's why it's min(armor, maxdamage)

        tot_damage = sum(damage)
        max_damage = max(damage)

        return tot_damage - min(armor, max_damage) + 1

        