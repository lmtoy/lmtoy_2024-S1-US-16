# 2024-S1-US-16   

this project uses a single IF, at CO(1-0), on 4 sources in the Abell 262 cluster.



120279 for A262_2:  Cancelled due to a fast increase in Tau, RH and presence of dense fog. 


* A262_1  5  1717.68 63.819 

* A262_2  3  1030.48  81.9352 

* A262_3  4  1373.91  69.8916

* A262_4  26  8931 s  26 mK - good detection

## Mark's info

Based on the HI data in the Apertif cubes (R=7.6 km/s), I find the
folowing frequency, cz and Vrad ranges over which the HI emission is
detected:

        	Frequency [MHz]		cz [km/s]	Vrad [km/s]	W_HI [km/s]

     A262_1	1398.75-1399.08		4570-4761	4499-4687	188
     A262_2	1398.75-1399.74		4426-4641	4362-4571	209
     A262_3	1401.17-1401.97		3942-4116	3891-4060	169
     A262_4	1400.00-1402.23		3886-4370	3836-4307	471


I have also measured the spectral rms noise [K] in the central 1x1
arcmin^2 of the single-scan cubes at the native resolution of 1.0
[km/s], and in the combined cube after straight averaging:

     scan	A262_1	A262_2	A262_3	A262_4

      a 	0.113	0.130	0.127	0.113	[K]
      b 	0.112	0.122	0.123	0.112	[K]
      c 	0.143	0.140	0.115	-----	[K]
      d 	0.123	0.112	0.114	-----	[K]
      e 	0.118	-----	-----	-----	[K]
     ave	0.055	0.063	0.060	0.079	[K]


According to the online sensitivity calculator, the expected spectral
rms noise in a single-scan cube should be around 0.102 [K] so the
observed noise is roughly 10-40% higher than expected.  I suppose this
is due to sub-optimal (day time) observing conditions?

I have attached the technical justification of the proposal in which we
suggest to smooth the spectra to an effective velocity resolution (Reff)
such that we have 10 spectral resolution elements across the full (HI)
line width.  This drives down the noise considerably.  After dong so, I
measure the following spectral noise levels in [mK] given the number of
scans we have so far:

        	A262_1  A262_2  A262_3  A262_4

      Nscns	5	4	4	2
      W_HI	188	209	169	471	[km/s]
      Reff	19	21	17	47	[km/s]
      Srms	13.0	13.9	14.5	11.6	[mK]


Also note in the scientific justification that I had estimated the CO
luminosities based on the 1.4 [GHz] radio continuum fluxes.  I suppose
there is quite a scatter in this relation, so expected S/N levels are
not guaranteed. 

### Non-standard gridding

The default gridding gives nppb=2, but we experimented with nppb=4, but
for this rmax needs to be increased to avoid finding pixels (mostly
near the edge) with no beam passing through.

In addition, there is a bug (aug 2024) that combinations cannot redefine
the gridding, so to fake it, the first obsnum can be quickly patched with
new gridding parameters, after which the combination will inherit them
from that first obsnum. https://github.com/astroumd/lmtoy/issues/56

### Non-standard ON/OFF calibration.

We could/should investigate if using the RAMP as an OFF, instead of the
real OFF. Based on some unstable baselines. https://github.com/astroumd/lmtoy/issues/55
