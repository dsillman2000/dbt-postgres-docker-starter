from fire import Fire

import datagen.entrypoints


class Datagen:
    user_events = datagen.entrypoints.user_events
    user_events.__doc__ = "Generate user events"


def main():
    Fire(Datagen)
