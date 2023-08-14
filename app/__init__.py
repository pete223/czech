from .declensions import (
    FirstDeclensionMasculineAnimate,
    FirstDeclensionMasculineInanimate,
    FirstDeclensionFeminine,
    FirstDeclensionNeuter,
    SecondDeclensionMasculineAnimate,
    SecondDeclensionMasculineInanimate,
    SecondDeclensionFeminine,
    SecondDeclensionNeuter,
    ThirdDeclensionMasculineAnimate,
    ThirdDeclensionFeminine,
    ThirdDeclensionNeuter,
)


class FDMA(FirstDeclensionMasculineAnimate):
    pass


class FDMI(FirstDeclensionMasculineInanimate):
    pass


class FDF(FirstDeclensionFeminine):
    pass


class FDN(FirstDeclensionNeuter):
    pass


class SDMA(SecondDeclensionMasculineAnimate):
    pass


class SDMI(SecondDeclensionMasculineInanimate):
    pass


class SDF(SecondDeclensionFeminine):
    pass


class SDN(SecondDeclensionNeuter):
    pass


class TDMA(ThirdDeclensionMasculineAnimate):
    pass


class TDF(ThirdDeclensionFeminine):
    pass


class TDN(ThirdDeclensionNeuter):
    pass
