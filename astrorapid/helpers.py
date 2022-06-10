import numpy as np


def find_nearest(array, value):
    """
    Find the index nearest to a given value.
    Adapted from: https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    """

    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()

    return idx


def delete_indexes(deleteindexes, *args):
    newarrs = []
    for arr in args:
        newarr = np.delete(arr, deleteindexes)
        newarrs.append(newarr)

    return newarrs


def convert_lists_to_arrays(*args):
    output = []
    for arg in args:
        out_array = np.asarray(arg)
        output.append(out_array)

    return output


def calc_luminosity(flux, fluxerr, mu):
    """ Normalise flux light curves with distance modulus.

    Parameters
    ----------
    flux : array
        List of floating point flux values.
    fluxerr : array
        List of floating point flux errors.
    mu : float
        Distance modulus from luminosity distance.

    Returns
    -------
    fluxout : array
        Same shape as input flux.
    fluxerrout : array
        Same shape as input fluxerr.

    """

    d = 10 ** (mu/5 + 1)
    dsquared = d**2

    norm = 1e18

    fluxout = flux * (4 * np.pi * dsquared/norm)
    fluxerrout = fluxerr * (4 * np.pi * dsquared/norm)

    return fluxout, fluxerrout


#def get_sntypes():
#    sntypes_map = {1: 'SNIa-norm',
#                   11: 'SNIa-norm',
#                   2: 'SNII',
#                  12: 'SNIIpca',
#                   14: 'SNIIn',
#                   3: 'SNIbc',
#                   13: 'SNIbc',
#                   5: 'SNIbc',
#                   6: 'SNII',
#                   41: 'SNIa-91bg',
#                   43: 'SNIa-x',
#                   45: 'point-Ia',
#                   50: 'Kilonova-GW170817',
#                   51: 'Kilonova',
#                   60: 'SLSN-I',
#                   61: 'PISN',
#                   62: 'ILOT',
#                   63: 'CART',
#                   64: 'TDE',
#                   70: 'AGN',
#                   80: 'RRLyrae',
#                   81: 'Mdwarf',
#                   83: 'EBE',
#                   84: 'Mira',
#                   90: 'uLens-BSR',
#                   91: 'uLens-1STAR',
#                   92: 'uLens-String',
#                   93: 'uLens - Point',
#                   99: 'Rare'}
#    return sntypes_map

# elasticc taxonomy tree for retrain_elasticc.py
# 'Static/Other' is only one without 9.
def get_sntypes():
    sntypes_map = {
                0: 'Static/Other',
                19: 'Non-Recurring',
                109: 'Non-Recurring/Other',
                119: 'SN-like',
                11190: 'Ia',
                11191: 'Ia',
                11290: 'Ib/c',
                11291: 'Ib/c',
                11292: 'Ib/c',
                11293: 'Ib/c',
                11294: 'Ib/c',
                11390: 'II',
                11391: 'II',
                11392: 'II',
                11393: 'II',
                11394: 'II',
                11395: 'II',
                11490: 'Iax',
                11590: '91bg',
                129: 'Fast',
                1209: 'Fast/Other',
                12190: 'KN',
                12191: 'KN',
                12290: 'M-dwarf Flare',
                12390: 'Dwarf Novae',
                12490: 'uLens',
                12491: 'uLens',
                12492: 'uLens',
                139: 'Long',
                1309: 'Long/Other',
                13190: 'SLSN',
                13191: 'SLSN',
                132: 'TDE',
                133: 'ILOT',
                134: 'CART',
                135: 'PISN',
                29: 'Recurring',
                209: 'Recurring/Other',
                219: 'Periodic',
                210: 'Periodic/Other',
                21190: 'Cepheid',
                21290: 'RR Lyrae',
                21390: 'Delta Scuti',
                21490: 'EB',
                21590: 'LPV/Mira',
                229: 'Non-Periodic',
                2209: 'Non-Periodic/Other',
                22190: 'AGN'}
    return sntypes_map