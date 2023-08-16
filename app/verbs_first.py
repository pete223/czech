from .verbs import FDV

fdv_verbs = [
    FDV("vstávat", "to get up", False),
    FDV("mít", "to have", True),
    FDV("snídat", "to have breakfast", False),
    FDV("odpočivat", "to rest", False),
    FDV("čekat", "to wait", True), # always followed by na eg. cěkám na autobus
    FDV("obědvat", "to have lunch", False)
]
