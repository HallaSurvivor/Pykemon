'''Deals with the class required to print stuff to a screen.'''
import required_lists as r

Pokemon = object

class PrintingStuff(object):
    '''Handles printing and things that happen alongside printing.'''
    def __init__(self, text, style = r.Style.NULL, required_pokemon = [Pokemon], target = Pokemon, damage = 0, status = "none", modifier = 0, modified_stat = "none", to_switch_in = Pokemon):
        self.text = text
        self.style = style
        self.required_pokemon = required_pokemon
        self.target = target
        self.damage = damage
        self.status = status
        self.modifier = modifier
        self.modified_stat = modified_stat
        self.to_switch_in = to_switch_in

    def cause_damage(self):
        '''Deals damage to the target.'''
        self.target.hp -= self.damage

    def cause_status_ailment(self):
        '''Causes a nonvolatile status ailment to the target.'''
        self.target.status_counter = 1
        self.target.status_nonvolatile = self.status

        if self.status == "badly poisoned":
            self.target.status_counter = 1

        elif self.status == "alseep":
            self.target.status_counter = randint(1, 3)

    def cause_status(self):
        '''Causes a volatile status to the target.'''
        self.target.volatile[self.status] = True

        if self.status == "partially trapped":
            self.target.trapped_counter = randint(2, 5)

    def switch(self):
        '''Switches a pokemon.'''
        pass


    def print_text(self):
        '''Actually prints the text, and decides which other method to run.'''
        r.box5data = self.text
        if self.style == r.Style.damage:
            self.cause_damage()

        elif self.style == r.Style.status:
            self.cause_status()

        elif self.style == r.Style.nonvolatile:
            self.cause_status_ailment()

        elif self.style == r.Style.modify:
            if self.target.stages[self.modified_stat] + self.modifier > 6:
                self.target.stages[self.modified_stat] = 6

            elif self.target.stages[self.modified_stat] + self.modifier < -6:
                self.target.stages[self.modified_stat] = -6

            else:
                self.target.stages[self.modified_stat] += self.modifier

        elif self.style == r.Style.switch_out:
            pass

def add_to_print_buffer(text, style = r.Style.NULL, required_pokemon = [Pokemon], target = Pokemon, damage = 0, status = "none", modifier = 0, modified_stat = "none", to_switch_in = Pokemon):
    r.to_do.append(PrintingStuff(text, style, required_pokemon, target, damage, status, modifier, modified_stat, to_switch_in))

def insert_in_print_buffer(position, text, style = r.Style.NULL, required_pokemon = [Pokemon], target = Pokemon, damage = 0, status = "none", modifier = 0, modified_stat = "none", to_switch_in = Pokemon):
    r.to_do.insert(position, PrintingStuff(text, style, required_pokemon, target, damage, status, modifier, modified_stat, to_switch_in))