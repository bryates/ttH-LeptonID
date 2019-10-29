import FWCore.ParameterSet.Config as cms

ttHLeptons = cms.EDProducer(
    'LeptonIdentifier',
    rhoParam      = cms.InputTag('fixedGridRhoFastjetAll'),
    electrons     = cms.InputTag('slimmedElectrons'),
    electronMinPt = cms.double(7.0),
    jets          = cms.InputTag('slimmedJets'),
    muons         = cms.InputTag('slimmedMuons'),
    muonMinPt     = cms.double(5.0),
    taus          = cms.InputTag('slimmedTaus'),
    tauMinPt      = cms.double(20.0),
    # See: https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
    LooseCSVWP   = cms.double(0.5803),    # Was 0.46
    MediumCSVWP  = cms.double(0.8838),   # Was 0.80
    LooseDeepWP  = cms.double(0.1522),
    MediumDeepWP = cms.double(0.4941),
    LooseDFWP    = cms.double(0.0521),
    MediumDFWP   = cms.double(0.3033),
    IsHIPSafe    = cms.bool(False),
    JECTag       = cms.string('')
)
