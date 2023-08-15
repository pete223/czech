from .nouns_first import (
    fdma_nouns,
    fdmi_nouns,
    fdf_nouns,
    fdn_nouns
)

from .nouns_second import (
    sdma_nouns,
    sdmi_nouns,
    sdf_nouns,
    sdn_nouns
)


from .nouns_third import (
    tdma_nouns,
    tdf_nouns,
    tdn_nouns
)


from .verbs_first import fdv_verbs


ALL_NOUNS = (
     fdma_nouns + fdmi_nouns + fdf_nouns + fdn_nouns
     + sdma_nouns + sdmi_nouns + sdf_nouns + sdn_nouns
     + tdma_nouns + tdf_nouns + tdn_nouns
 )


ALL_VERBS = (fdv_verbs)
