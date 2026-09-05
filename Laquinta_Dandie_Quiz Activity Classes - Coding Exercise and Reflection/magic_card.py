"""
MagicCard - An accurate Python OOP model of a Magic: The Gathering creature card.
"""

class MagicCard:
    """Represents a single Magic: The Gathering creature card."""

    # --- Class Attributes (Shared Defaults) -------------------------------
    DEFAULT_SET = "Core Set"
    CARD_TYPE = "Creature"
    SUPERTYPES = ()              # e.g., ("Legendary",) or ("Snow",)
    SUBTYPES = ()                # e.g., ("Elf", "Druid") or ("Dragon",)
    RARITY = "Common"            # Common, Uncommon, Rare, Mythic Rare
    KEYWORDS = ()                # e.g., ("Flying", "Haste", "Trample")
    IS_PERMANENT = True          # Creatures stay on the battlefield
    LEGAL_FORMATS = ("Standard", "Pioneer", "Modern", "Legacy", "Vintage", "Commander")

    # Mana color mapping dictionary for identity lookup
    COLOR_MAP = {
        "W": "White",
        "U": "Blue",
        "B": "Black",
        "R": "Red",
        "G": "Green"
    }

    # --- Constructor -----------------------------------------------------
    def __init__(self, card_name, mana_cost, power=1, toughness=1, subtypes=None, keywords=None):
        self.card_name = card_name
        self.mana_cost = mana_cost
        self.power = power
        self.toughness = toughness
        self.subtypes = tuple(subtypes) if subtypes else self.SUBTYPES
        self.keywords = tuple(keywords) if keywords else self.KEYWORDS

    # --- Dynamic MTG Mechanics (@property) ------------------------------
    @property
    def converted_mana_cost(self):
        """Calculates total Mana Value / Converted Mana Cost (CMC)."""
        total = 0
        for char in self.mana_cost:
            if char.isdigit():
                total += int(char)
            elif char in self.COLOR_MAP:
                total += 1
        return total

    @property
    def color_identity(self):
        """Determines colors from mana symbols in the casting cost."""
        colors = [name for symbol, name in self.COLOR_MAP.items() if symbol in self.mana_cost]
        return colors if colors else ["Colorless"]

    # --- Instance Methods ------------------------------------------------
    def take_damage(self, amount):
        """Simulates in-game combat damage reducing current toughness."""
        self.toughness -= amount

    def __str__(self):
        colors = "/".join(self.color_identity)
        subtypes_str = f" — {' '.join(self.subtypes)}" if self.subtypes else ""
        keywords_str = f" | Keywords: {', '.join(self.keywords)}" if self.keywords else ""
        
        return (
            f"{self.card_name} [{self.mana_cost}] (CMC: {self.converted_mana_cost})\n"
            f"Type: {self.CARD_TYPE}{subtypes_str}\n"
            f"P/T: {self.power}/{self.toughness} | Colors: {colors}{keywords_str}\n"
            f"Set: {self.DEFAULT_SET} | Rarity: {self.RARITY}"
        )


# =========================================================================
# Demonstration
# =========================================================================
if __name__ == "__main__":

    # Instance 1: Basic Creature
    elf = MagicCard(
        "Llanowar Elves", 
        "G", 
        power=1, 
        toughness=1, 
        subtypes=["Elf", "Druid"]
    )

    # Instance 2: Flying / Haste Creature with Shadowed Class Attributes
    dragon = MagicCard(
        "Shivan Dragon", 
        "4RR", 
        power=5, 
        toughness=5, 
        subtypes=["Dragon"], 
        keywords=["Flying"]
    )
    dragon.RARITY = "Rare"  # Shadowing class default rarity for this instance

    print("--- CARD 1 ---")
    print(elf)
    print("\n--- CARD 2 ---")
    print(dragon)