import openmoltools as omt

# =============================================================================================
# OPEN EYE TESTS
# =============================================================================================

# Borrowing the test from the OpenMolTools set
try:
    oechem = omt.utils.import_("openeye.oechem")
    if not oechem.OEChemIsLicensed():
        raise(ImportError("Need License for OEChem!"))
    oequacpac = omt.utils.import_("openeye.oequacpac")
    if not oequacpac.OEQuacPacIsLicensed():
        raise(ImportError("Need License for oequacpac!"))
    oeiupac = omt.utils.import_("openeye.oeiupac")
    if not oeiupac.OEIUPACIsLicensed():
        raise(ImportError("Need License for OEOmega!"))
    oeomega = omt.utils.import_("openeye.oeomega")
    if not oeomega.OEOmegaIsLicensed():
        raise(ImportError("Need License for OEOmega!"))
    HAVE_OE = True
    openeye_exception_message = str()
except Exception as e:
    HAVE_OE = False
    openeye_exception_message = str(e)
