import FWCore.ParameterSet.Config as cms

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(7000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettings = cms.vstring('MSTJ(11)=3     ! Choice of the fragmentation function', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(51)=10042     ! CTEQ6L1 structure function chosen', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'MSTP(81)=1     ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model', 
            'MSTU(21)=1     ! Check on possible errors during program execution', 
            'PARP(82)=1.8387   ! pt cutoff for multiparton interactions', 
            'PARP(89)=1960. ! sqrts for which PARP82 is set', 
            'PARP(83)=0.5   ! Multiple interactions: matter distrbn parameter', 
            'PARP(84)=0.4   ! Multiple interactions: matter distribution parameter', 
            'PARP(90)=0.16  ! Multiple interactions: rescaling power', 
            'PARP(67)=2.5    ! amount of initial-state radiation', 
            'PARP(85)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(86)=1.0  ! gluon prod. mechanism in MI', 
            'PARP(62)=1.25   ! ', 
            'PARP(64)=0.2    ! ', 
            'MSTP(91)=1     !', 
            'PARP(91)=2.1   ! kt distribution', 
            'PARP(93)=15.0  ! '),
        processParameters = cms.vstring('MSEL=39', 
            'IMSS(1)=1', 
            'IMSS(3)=1', 
            'IMSS(51)=0', 
            'IMSS(52)=0', 
            'IMSS(53)=3', 
            'RVLAMB(1,1,2)=.005', 
            'RMSS(1)=10000.0', 
            'RMSS(2)=10000.0', 
            'RMSS(4)=10000.0', 
            'RMSS(3)=250', 
            'RMSS(5)=5.00', 
            'RMSS(8)=2000.0', 
            'RMSS(9)=2000.0', 
            'RMSS(10)=2000.0', 
            'RMSS(11)=2000.0', 
            'RMSS(12)=2000.0', 
            'RMSS(6)=10000.0', 
            'RMSS(7)=10000.0', 
            'RMSS(13)=10000.0', 
            'RMSS(14)=10000.0', 
            'RMSS(15)=2.4', 
            'RMSS(16)=-3.3', 
            'RMSS(17)=1.0', 
            'RMSS(18)=-0.1020', 
            'RMSS(19)=10000.0'),
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)
