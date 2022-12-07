#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define the configuration for the simulation.

These parameters can be used to configure the top-level simulation graphs `LISA`, `TDIFromFile` and
`LISAWithTDI`.

Parameters are organized in two categories, those which affect the `LISA` simulation graph and
those which affect the `TDI` simulation graph (or subgraphs of either of these).

The parameters defined here are not parameters on nodes or graphs, because
they change the fundamental structure of the simulation graph.

Consequently, one must recompile the `LISA` graph after changing any parameters
in the LISA section, and recompile the `TDIFromFile` graph after
changing any of the parameters in the TDI section. `LISAWithTDI` needs to be recompiled when any of
the parameters are changed, since it contains both `LISA` and `TDI`.

Authors:
    Jean-Baptiste Bayle <jbayle@jpl.nasa.gov>
    Olaf Hartwig <olaf.hartwig@aei.mpg.de>
"""

# Measurement sampling frequency, in Hz
LISA_MEASUREMENT_FS = 4.0

# Measurement downsampling factor
# This is the ratio LISA_PHYSICS_FS / LISA_MEASUREMENT_FS)
LISA_MEASUREMENT_DOWNSAMPLING = 1

# Sampling frequency at which physics is simulated, in Hz
# Deduced from LISA_MEASUREMENT_FS and LISA_MEASUREMENT_DOWNSAMPLING
LISA_PHYSICS_FS = LISA_MEASUREMENT_FS * LISA_MEASUREMENT_DOWNSAMPLING

# Type of orbit, used to compute proper pseudo-ranges (PPRs), one of
#   * ('file', 'ppr') to read PPRs from an orbit file generated with lisaorbits,
#     which include a relativistic treatment of spacecraft reference frames.
#   * ('file', 'tt') to read light TTs from an orbit file generated with lisaorbits,
#     which assume that the spacecraft proper times are identical to the TCB
#   * ('polynomial', N) to compute PPRs as polynomials of order N --
#     coeffficients can be set using parameters `d0_ppr_<i><j>`, `d1_ppr_<i><j>`, etc.
#     Note that PPRs do not contain any relativistic corrections in this case.
#
# Please note that this does not set the TDI generation
LISA_ORBIT_TYPE = ('file', 'ppr')

# Test mass acceleration noise shape
LISA_ACC_NOISE_A_LEVEL = 2.4E-15 #m/s^2/sqrt(Hz)
LISA_ACC_NOISE_F_KNEE = 0.4E-3 #Hz
LISA_ACC_NOISE_USE_PZM = False

# Backlink noise shape
LISA_BACKLINK_NOISE_A_LEVEL = 3.0E-12 #m/sqrt(Hz)
LISA_BACKLINK_NOISE_F_KNEE = 2E-3 #Hz

# Path to glitch file or None
LISA_GLITCH_FILE = None

# Type of gravitational-wave input
# Must be one of the following:
#   * None          no gravitational-wave signals
#   * 'file'        read projected strain from HDF5 file (set path with param `gw_path`)
LISA_GW_TYPE = 'file'

# Gravitational-wave file sampling rate
# Only used if `LISA_GW_TYPE == 'file'`
LISA_GW_FILE_FS = 4.0

# Upsampling factor used for gravitational-wave file
# Only used if `LISA_GW_TYPE == 'file'`
LISA_GW_FILE_UPSAMPLING = LISA_PHYSICS_FS / LISA_GW_FILE_FS

# Central frequency of the lasers, in MHz
# All laser offsets are relative offsets to this value
LISA_LASER_CENTRAL_FREQUENCY = 2.816E8

# Laser locking scheme,
# One of None (6 free-running lasers), 'N1a', 'N1b', 'N1c', 'N2a', 'N2b', or 'N2c',
# following locking schemes naming described in [1]
#
#   [1] Heinzel, G. (2018). LISA Frequency Planning (LISA−AEI−INST−TN−002)
LISA_LOCKING_SCHEME = 'N1c'

# Primary laser for locking
# One of '12', '23', '31', '13', '32', '21'
# This option is ignored if LISA_LOCKING_SCHEME is None
LISA_PRIMARY_LASER = '12'

# Frequency offsets, in MHz
# For free-running lasers, these are relative to the cavity frequency (i.e., laser central frequency),
# or relative to the reference (adjacent or distant) beam otherwise.
LISA_FREQUENCY_OFFSETS = {'12': 8.1, '23': 9.2, '31': 10.3, '13': 1.4, '32': -11.6, '21': -9.5}

# Computation order to solve the implicit time-shift equation when sampling measurements
# according to local clocks (in the ADC), i.e. number of recursive iterations
LISA_ADC_RECURSION_ORDER = 1

# Whether to apply Doppler shifts to laser frequency offsets and fluctuations and offsets
# Doppler shifts are caused by nonvanishing derivatives of the proper pseudo-ranges
LISA_SIMULATE_DOPPLER = False

# Publish clock time offset in SCS and CCS for debug
# Those are not measurements that can be accessed in reality
LISA_DEBUG_CLOCK_OFFSETS = False

# Anti-aliasing on-board filtering
# Attenuation in dB
LISA_AAFILTER_ATTENUATION = 240

# Anti-aliasing on-board filtering
# Transition band: [passband, stopband] in Hz
LISA_AAFILTER_TRANSITION_BAND = [1.1, 2.9]

LISA_PUBLISH_BEATNOTE_COMPONENTS = True

LISA_PUBLISH_TOTAL_BEATNOTE = True

## TDI Offline Processing Options

# Sampling frequency of measurements used as inputs, in Hz
# This value must match LISA_MEASUREMENT_FS
TDI_MEASUREMENT_FS = LISA_MEASUREMENT_FS

# Input file format for TDIFromFile, must be 'text' or 'hdf5'
TDI_INPUT_FORMAT = 'hdf5'

# Whether to use frequency fluctuations or total frequency
# Using total frequency is closer to reality, but yields increased numerical noise
TDI_USE_FREQUENCY_FLUCTUATIONS = True

# Generation of TDI algorithm, must be 1.5 or 2
# This only determines which TDI combination is computed
TDI_GENERATION = 2.0

# Whether intermediary variables should be published as outputs
TDI_PUBLISH_INTERVAR = True

# Whether Michelson X, Y and Z variables should be published as outputs
TDI_PUBLISH_MICHELSON = True

# Whether quasi-orthogonal A, E and T variables should be published as outputs
TDI_PUBLISH_ORTHVAR = True

# Whether Sagnac α, β, and ɣ variables should be publihsed as outputs
TDI_PUBLISH_SAGNAC = False

# Whether clock correction should be carried out on Michelson variables
TDI_CLOCKCOR_MICHELSON = True

# Whether clock correction should be carried out on quasi-orthogonal variables
TDI_CLOCKCOR_ORTHVAR = True

# Whether clock correction should be carried out on Sagnac variables
TDI_CLOCKCOR_SAGNAC = False

# Whether to use exact clock-noise corrections [1]
# [1] Clock-jitter reduction in LISA time-delay interferometry combinations, arXiv:2005.02430
TDI_USE_UPDATED_CLOCKCOR = True

# Whether to compensate for Doppler shifts
# Doppler shifts are caused by nonvanishing derivatives of the proper pseudo-ranges,
# and are corrected using the measured pseudo-range derivatives
TDI_USE_DOPPLER_CORRECTION = False


## Conventions and notations

# Spacecraft indices
SC_INDICES = ['1', '2', '3']

# Optical-bench indices
OB_INDICES = ['12', '23', '31', '13', '32', '21']

# Triplets of spacecraft indices
TRIPLET_INDICES = ['123', '231', '312', '132', '321', '213']
